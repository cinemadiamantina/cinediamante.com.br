import csv, re, unicodedata, sys, os
from datetime import datetime
from pathlib import Path
import requests
from urllib.parse import urlparse, parse_qs

# ---------- Configs ----------
ENCODING = "utf-8"
SEPARADOR = None  # None = auto-detect; force "\t" se quiser
OUT_DIR = Path("_filmes")
PRESS_DIR = Path("assets/press")
DATE_IN_FMT = ["%d/%m/%Y", "%d/%m/%Y %H:%M:%S", "%d/%m/%Y %H:%M"]
DATE_OUT_FMT = "%Y-%m-%d"

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
    "Duração": "duracao_bruta",
}

BOOL_MAP = {"sim": True, "não": False, "nao": False, "n/a": None, "": None, None: None}

# ---------- Utils ----------
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
    s2 = re.sub(r"[^\d/ :]", "", s)
    for fmt in DATE_IN_FMT:
        try:
            return datetime.strptime(s2, fmt).strftime(DATE_OUT_FMT)
        except ValueError:
            continue
    return None

def parse_duration(val):
    if val is None: return (None, None)
    s = str(val).strip().lower().replace(" ", "")
    s = s.replace(",", "")
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

def sniff_delimiter(sample):
    try:
        dialect = csv.Sniffer().sniff(sample, delimiters="\t,;|")
        return dialect.delimiter
    except Exception:
        return "\t"

def is_gdrive_folder(url: str) -> bool:
    # detecta URLs tipo /folders/ID
    return "drive.google.com" in url and "/folders/" in url

def extract_gdrive_file_id(url: str):
    """
    Suporta:
    - https://drive.google.com/file/d/FILE_ID/view?usp=...
    - https://drive.google.com/uc?export=download&id=FILE_ID
    - https://drive.google.com/open?id=FILE_ID
    - https://drive.google.com/thumbnail?id=FILE_ID
    Retorna None para links de pasta.
    """
    if not url: return None
    if is_gdrive_folder(url): 
        return None
    try:
        parsed = urlparse(url)
        if "/file/d/" in parsed.path:
            m = re.search(r"/file/d/([^/]+)/?", parsed.path)
            if m:
                return m.group(1)
        qs = parse_qs(parsed.query)
        if "id" in qs and qs["id"]:
            return qs["id"][0]
    except Exception:
        pass
    return None

def guess_ext_from_ct(content_type: str, fallback=".jpg"):
    if not content_type: 
        return fallback
    ct = content_type.lower().split(";")[0].strip()
    return {
        "image/jpeg": ".jpg",
        "image/jpg": ".jpg",
        "image/png": ".png",
        "image/webp": ".webp",
        "image/gif": ".gif",
        "image/tiff": ".tif",
        "image/bmp": ".bmp",
    }.get(ct, fallback)

def download_gdrive_file(file_id: str, dest_path: Path, timeout=60):
    """
    Baixa arquivo público do Google Drive contornando o aviso de vírus.
    """
    if not file_id:
        return False, "file_id vazio"
    URL = "https://docs.google.com/uc?export=download"
    with requests.Session() as s:
        try:
            resp = s.get(URL, params={"id": file_id}, stream=True, timeout=timeout)
        except Exception as e:
            return False, f"erro na conexão inicial: {e}"

        def _get_confirm_token(r):
            for k, v in r.cookies.items():
                if k.startswith("download_warning"):
                    return v
            return None

        token = _get_confirm_token(resp)
        if token:
            try:
                resp = s.get(URL, params={"id": file_id, "confirm": token}, stream=True, timeout=timeout)
            except Exception as e:
                return False, f"erro confirm download: {e}"

        if resp.status_code != 200:
            return False, f"http {resp.status_code}"

        # escolhe extensão
        ext = guess_ext_from_ct(resp.headers.get("Content-Type"), fallback=dest_path.suffix or ".jpg")
        if dest_path.suffix.lower() != ext.lower():
            dest_path = dest_path.with_suffix(ext)

        try:
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            with open(dest_path, "wb") as f:
                for chunk in resp.iter_content(32768):
                    if chunk:
                        f.write(chunk)
        except Exception as e:
            return False, f"erro ao salvar: {e}"

    return True, str(dest_path)

def normalize_row(header, row):
    d = {}
    for h, v in zip(header, row):
        key = MAP.get(h.strip(), slugify(h.strip()))
        d[key] = (v or "").strip()
    d["data_finalizacao"] = parse_date(d.get("data_finalizacao"))
    d["tem_dialogos"] = to_bool(d.get("tem_dialogos"))
    d["tem_lista_dialogos"] = to_bool(d.get("tem_lista_dialogos"))
    d["direitos_musicais_ok"] = to_bool(d.get("direitos_musicais_ok"))
    mins, secs = parse_duration(d.get("duracao_bruta"))
    d["duration_minutes"] = mins
    d["duration_seconds"] = secs
    titulo = d.get("titulo_original") or d.get("titulo_internacional")
    d["slug"] = slugify(titulo)
    return d

def compose_front_matter(d: dict, local_press_path: str | None) -> str:
    year = None
    if d.get("data_finalizacao"):
        try: year = int(d["data_finalizacao"][:4])
        except: pass

    mins, secs = d.get("duration_minutes"), d.get("duration_seconds")
    runtime_str = None
    if mins is not None:
        runtime_str = f"{mins} min" if not secs else f"{mins} min {secs}s"

    # Campos SANEADOS: sem telefone/email/senhas
    fields = {
        "title": d.get("titulo_original") or d.get("titulo_internacional"),
        "title_intl": d.get("titulo_internacional") or "",
        "slug": d.get("slug"),
        "year": year,
        "length_min": mins,
        "length_sec": secs,
        "runtime_str": runtime_str,
        "format": d.get("metragem") or "",
        "state": d.get("estado_producao") or "",
        "has_dialogue": d.get("tem_dialogos"),
        "has_dialogue_list": d.get("tem_lista_dialogos"),
        "genre": d.get("genero") or "",
        "directors": d.get("direcao") or "",
        "producers": d.get("producao") or "",
        "writers": d.get("roteiro") or "",
        "cast": d.get("elenco") or "",
        "distributor": d.get("distribuidora") or "",
        "music_rights_ok": d.get("direitos_musicais_ok"),
        "screening_link": d.get("link_visualizacao") or "",
        "press_photo": local_press_path or (d.get("foto_divulgacao") or ""),
        "ethnicity_director": d.get("identidade_etnico_racial") or "",
        "gender_director": d.get("identidade_genero") or "",
        "confirmation": d.get("confirmacao") or "",
        "finalized_at": d.get("data_finalizacao") or "",
    }

    lines = ["---"]
    for k, v in fields.items():
        if isinstance(v, bool):
            lines.append(f"{k}: {'true' if v else 'false'}")
        elif v is None or v == "":
            lines.append(f"{k}: ")
        else:
            if isinstance(v, int):
                lines.append(f"{k}: {v}")
            else:
                val = str(v)
                if "\n" in val:
                    lines.append(f"{k}: |")
                    for ln in val.splitlines():
                        lines.append(f"  {ln}")
                else:
                    if any(c in val for c in [":", "{", "}", "[", "]", "#", "&", ">", "|", "%", "@", "`", "\"", "'"]):
                        val = "\"" + val.replace("\"", "\\\"") + "\""
                    lines.append(f"{k}: {val}")
    lines.append("---")
    return "\n".join(lines)

def read_rows(path):
    with open(path, "r", encoding=ENCODING, newline="") as f:
        sample = f.read(4096)
        delim = SEPARADOR or sniff_delimiter(sample)
        f.seek(0)
        reader = csv.reader(f, delimiter=delim)
        header = next(reader)
        for row in reader:
            if not any(cell.strip() for cell in row):
                continue
            yield normalize_row(header, row)

def main():
    if len(sys.argv) < 2:
        print("Uso: python build_catalog.py caminho/para/arquivo.tsv")
        sys.exit(1)

    in_path = sys.argv[1]
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    PRESS_DIR.mkdir(parents=True, exist_ok=True)

    created = 0
    for d in read_rows(in_path):
        slug = d.get("slug") or "sem-titulo"

        # tenta baixar press_photo se for GDrive de arquivo
        local_press_url = None
        photo_url = d.get("foto_divulgacao") or ""
        if photo_url:
            if is_gdrive_folder(photo_url):
                print(f"[{slug}] press_photo é pasta do Drive — ignorando download, mantendo link.")
            else:
                file_id = extract_gdrive_file_id(photo_url)
                if file_id:
                    dest_guess = PRESS_DIR / f"{slug}.jpg"
                    ok, info = download_gdrive_file(file_id, dest_guess)
                    if ok:
                        # usa caminho relativo para o site
                        rel = "/" + str(Path(info).as_posix())
                        local_press_url = rel
                        print(f"[{slug}] press_photo baixado -> {rel}")
                    else:
                        print(f"[{slug}] falha ao baixar press_photo: {info}. Mantendo link original.")
                else:
                    print(f"[{slug}] link press_photo não é reconhecido do Drive (arquivo). Mantendo link original.")

        front = compose_front_matter(d, local_press_url)
        sinopse = (d.get("sinopse") or "").strip()

        md_path = OUT_DIR / f"{slug}.md"
        with open(md_path, "w", encoding="utf-8") as fp:
            fp.write(front + "\n")
            if sinopse:
                fp.write("\n" + sinopse + "\n")

        created += 1

    print(f"✓ Criados/atualizados {created} arquivos em {OUT_DIR.resolve()}")

if __name__ == "__main__":
    main()
