import csv, re, unicodedata, sys
from datetime import datetime

# ---------- Configs assumidas (mude se quiser) ----------
ENCODING = "utf-8"
SEPARADOR = None  # None = auto-detect; force "\t" se quiser
DATE_IN_FMT = ["%d/%m/%Y", "%d/%m/%Y %H:%M:%S", "%d/%m/%Y %H:%M"]  # tenta na ordem
DATE_OUT_FMT = "%Y-%m-%d"

# Mapeamento de cabeçalhos -> chaves normalizadas
MAP = {
    "Carimbo de data/hora": "timestamp",
    "Endereço de e-mail": "email_envio",
    "Título original": "titulo_original",
    "Título internacional": "titulo_internacional",
    "Data de finalização": "data_finalizacao",
    "Metragem": "metragem",
    "Duração (em minutos)": "duracao_bruta",
    "Estado de produção": "estado_producao",
    "A obra possui diálogos?": "tem_dialogos",
    "Possui lista de diálogos?": "tem_lista_dialogos",
    "Gênero": "genero",
    "Sinopse curta": "sinopse",
    "Diretoras / Diretores": "direcao",
    "Produtoras / Produtores": "producao",
    "Roteiristas": "roteiro",
    "Elenco": "elenco",
    "Distribuidora": "distribuidora",
    "Possui os direitos das músicas utilizadas na obra?": "direitos_musicais_ok",
    "Link de visualização": "link_visualizacao",
    "Senha": "senha",
    "Fotografia para divulgação": "foto_divulgacao",
    "Telefone de contato": "telefone",
    "E-mail": "email_contato",
    "Qual identidade étnico-racial é declarada pela pessoa responsável pela direção do filme": "identidade_etnico_racial",
    "Com qual identidade de gênero a pessoa responsável pela direção do filme se identifica?": "identidade_genero",
    "Cavaram uma cova no meu coração": "campo_extra_opcional",
    "Confirmação": "confirmacao",
    # alguns campos no sample aparecem com pequenas variações, adiciono aliases:
    "Duração": "duracao_bruta",
}

BOOL_MAP = {
    "sim": True, "não": False, "nao": False, "n/a": None, "": None, None: None
}

UF_FIX = {
    # quando vêm "RJ e CE" ou "Minas Gerais" eu guardo como string bruta mesmo
}

def slugify(texto: str) -> str:
    if not texto or not texto.strip():
        return "sem-titulo"
    t = unicodedata.normalize('NFKD', texto).encode('ascii', 'ignore').decode('ascii')
    t = re.sub(r"[^a-zA-Z0-9]+", "-", t).strip("-").lower()
    return t or "sem-titulo"

def to_bool(val):
    if val is None: return None
    v = str(val).strip().lower()
    return BOOL_MAP.get(v, None)

def parse_date(val):
    if not val or not str(val).strip():
        return None
    s = str(val).strip()
    for fmt in DATE_IN_FMT:
        try:
            return datetime.strptime(s, fmt).strftime(DATE_OUT_FMT)
        except ValueError:
            continue
    # tenta corrigir "01/04/2024 " com lixo:
    s2 = re.sub(r"[^\d/ :]", "", s)
    for fmt in DATE_IN_FMT:
        try:
            return datetime.strptime(s2, fmt).strftime(DATE_OUT_FMT)
        except ValueError:
            continue
    return s  # devolve como veio se não parsear

def parse_duration(val):
    """
    Aceita: "17", "23min", "8m9s", "20min40s", "21", "1min,30s", "27 min"
    Retorna (minutes, seconds)
    """
    if val is None: return (None, None)
    s = str(val).strip().lower().replace(" ", "")
    s = s.replace(",", "")  # "1min,30s" -> "1min30s"
    if re.fullmatch(r"\d+", s):
        return (int(s), 0)
    m = re.match(r"(?:(\d+)min)?(?:(\d+)s)?", s)
    if not m or (m.group(1) is None and m.group(2) is None):
        m2 = re.match(r"(?:(\d+)m)?(?:(\d+)s)?", s)
        if m2 and (m2.group(1) or m2.group(2)):
            mins = int(m2.group(1) or 0)
            secs = int(m2.group(2) or 0)
            return (mins + secs // 60, secs % 60)
        return (None, None)
    mins = int(m.group(1) or 0)
    secs = int(m.group(2) or 0)
    return (mins + secs // 60, secs % 60)

def normalize_row(header, row):
    d = {}
    for h, v in zip(header, row):
        key = MAP.get(h.strip(), slugify(h.strip()))
        d[key] = (v or "").strip()
    # Normalizações
    d["data_finalizacao"] = parse_date(d.get("data_finalizacao"))
    # dialogos
    d["tem_dialogos"] = to_bool(d.get("tem_dialogos"))
    d["tem_lista_dialogos"] = to_bool(d.get("tem_lista_dialogos"))
    d["direitos_musicais_ok"] = to_bool(d.get("direitos_musicais_ok"))
    # duração
    mins, secs = parse_duration(d.get("duracao_bruta"))
    d["duration_minutes"] = mins
    d["duration_seconds"] = secs
    # título e slug
    titulo = d.get("titulo_original") or d.get("titulo_internacional")
    d["slug"] = slugify(titulo)
    # estado de produção sem mexer demais
    return d

def sniff_delimiter(sample):
    try:
        dialect = csv.Sniffer().sniff(sample, delimiters="\t,;|")
        return dialect.delimiter
    except Exception:
        return "\t"

def read_and_preview(path, preview=5):
    with open(path, "r", encoding=ENCODING, newline="") as f:
        sample = f.read(2048)
        delim = SEPARADOR or sniff_delimiter(sample)
        f.seek(0)
        reader = csv.reader(f, delimiter=delim)
        header = next(reader)
        print(f"# Detected delimiter: {repr(delim)} — colunas: {len(header)}")
        print("# Primeiras linhas normalizadas:")
        count = 0
        for row in reader:
            norm = normalize_row(header, row)
            # mostra um resumo enxuto:
            resumo = {
                "slug": norm["slug"],
                "titulo_original": norm.get("titulo_original"),
                "titulo_internacional": norm.get("titulo_internacional"),
                "data_finalizacao": norm.get("data_finalizacao"),
                "duration_minutes": norm.get("duration_minutes"),
                "duration_seconds": norm.get("duration_seconds"),
                "estado_producao": norm.get("estado_producao"),
                "tem_dialogos": norm.get("tem_dialogos"),
                "tem_lista_dialogos": norm.get("tem_lista_dialogos"),
                "email_contato": norm.get("email_contato"),
                "telefone": norm.get("telefone"),
            }
            print(resumo)
            count += 1
            if count >= preview:
                break

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python parse_filmes.py caminho/para/arquivo.tsv")
        sys.exit(1)
    read_and_preview(sys.argv[1])
