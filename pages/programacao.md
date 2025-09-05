---
layout: post
title: Programação Completa
description: Programação completa do II Festival de Cinema de Diamantina
image: logo_var/logo_var_003.png	
permalink: /programacao
nav-menu: true
nav-menu-order: 2
show_tile: false
---

<!-- CLASSIFICACAO APENAS SÍMBOLO 
<span class="ci-box ci-l"  role="img" aria-label="Classificação indicativa: Livre">L</span>
<span class="ci-box ci-10" role="img" aria-label="Classificação indicativa: não recomendado para menores de 10 anos">10</span>
<span class="ci-box ci-12" role="img" aria-label="Classificação indicativa: não recomendado para menores de 12 anos">12</span>
<span class="ci-box ci-14" role="img" aria-label="Classificação indicativa: não recomendado para menores de 14 anos">14</span>
<span class="ci-box ci-16" role="img" aria-label="Classificação indicativa: não recomendado para menores de 16 anos">16</span>
<span class="ci-box ci-18" role="img" aria-label="Classificação indicativa: não recomendado para menores de 18 anos">18</span>
-->
<style>
	:root {
	  --h1-h: 1.3em;   /* altura do h1 fixo */
	}

	.day {
		position: relative;
	  border-bottom: 10px solid #000;
	}

	.day > h1{
	  position: sticky;
	  top: var(--h1-h);
	  z-index: 20;
	  margin: 0;
	  padding: 12px 16px;
	  line-height: 1.2;
	  background: #fff;
	  color: #000;
	  border-bottom: 1px solid #eee;
	}

	.session {
	  margin: 1.5em 0;
	  padding: 1.2em 1.5em;
	  background: #000;
	  border: 1px solid #333;
/*	  border-radius: 10px;*/
	  position: relative;
	  box-shadow: 0 2px 6px rgba(0,0,0,0.06);
/*	  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;*/
	}

	/* recorte lateral sutil */
	.session::before,
	.session::after {
	  content: "";
	  position: absolute;
	  top: 50%;
	  width: 20px;
	  height: 20px;
	  background: #111;
	  border: 1px solid #111;
	  border-radius: 50%;
	  transform: translateY(-50%);
	}


	.session::before {
	  left: -11px;
	}

	.session::after {
	  right: -11px;
	}

	/* cabeçalho do ticket */
	.session > h3 {
	  margin: 0 0 0.8em 0;
	  padding-bottom: 0.6em;
	  padding-right: 1.7em;
	  border-bottom: 1px dashed #ccc;
/*	  font-size: 1.05rem;*/
	  font-weight: 600;
	  color: #fff;

	}

	/* conteúdo (filmes, detalhes) */
	.session blockquote {
	  margin: 0.6em 0;
	  padding: 0.3em 0 0.3em 0;
	  border-left: 2px solid #555;
	  padding-left: 0.8em;
	  color: #ffff;
	  background: transparent;
	}

	/* ênfases (comentários finais) */
	.session em {
	  display: block;
	  margin-top: 0.8em;
	  color: #ffff;
	}

	h3 i {
	  display: inline-block;
	  width: 1.5em; /* ajuste conforme necessário */
	  text-align: center;
	}
	
	/* opcional: ancoragem suave para #ids sem “sumir” sob os stickies */
	[id] { scroll-margin-top: var(--h1-h); }

	.scroll-top {
	  position: fixed;
	  bottom: 0;
	  right: 0;
	  width: 96px;
	  height: 64px;
	  min-width: 40px;
	  min-height: 40px;
	  background: #fff;
	  color: #000;
	  display: flex;
	  align-items: center;
	  justify-content: center;
	  border: none;
	  border-radius: 2px;
	  box-shadow: 0 2px 6px rgba(0,0,0,0.15);
	  cursor: pointer;
	  z-index: 1000;
	  transition: background 0.2s ease, transform 0.2s ease;
	}

	.scroll-top:hover {
	  background: #f5f5f5;
/*	  transform: translateY(-2px);*/
	}

	.scroll-top i {
	  font-size: 2em;
	}

	/* Mobile adjustment */
	@media (max-width: 768px) {
	  .scroll-top {
	    right: 50%;
	    transform: translateX(50%);
	  }
	}

</style>

<a href="#one" class="button special scroll-top"><i class="fa-solid fa-arrow-up"></i></a>

<a href="#d16" class="button special fit">16/09 - Terça</a>
<a href="#d17" class="button special fit">17/09 - Quarta</a>
<a href="#d18" class="button special fit">18/09 - Quinta</a>
<a href="#d19" class="button special fit">19/09 - Sexta</a>
<a href="#d20" class="button special fit">20/09 - Sábado</a>

---
<section class="day" id="d16">
  <h1>16/09, terça-feira</h1>

  <section class="session" id="d16-s1">
    <h3>
    	<span class="ci-box ci-16" role="img" aria-label="Classificação indicativa: não recomendado para menores de 16 anos">16</span>
    	<i class="fa-solid fa-ticket"></i> SESSÃO DE ABERTURA<br />
      <i class="fa-solid fa-clock"></i> 19h <br />
      <i class="fa-solid fa-location-dot"></i> Cine Theatro Santa Izabel
    </h3>
    <blockquote>
      <strong><a href="/filme/cidade-campo/">Cidade; Campo</a></strong><br>
      (Juliana Rojas | 2024, SP, 120’)<br>
      Comentada pela atriz <strong>Fernanda Vianna</strong>
    </blockquote>
  </section>
	<section class="session" style="background-image: url('{{ site.images_path }}FotosPedroMiranda_fHist/IgrejaDoBonfim_0002.JPG'); height: 500px; background-attachment: fixed;  background-size: cover; background-position-x: center;">
	</section>
</section>


<section class="day" id="d17">
  <h1>17/09, quarta-feira</h1>

  <section class="session" id="d16-s1">
    <h3>
    	<i class="fa-solid fa-podcast"></i> Gravação de Podcast com Fernanda Vianna<br />
      <i class="fa-solid fa-clock"></i> 14h <br />
      <i class="fa-solid fa-location-dot"></i> Galeria do Cine Theatro Santa Izabel
    </h3>
    <blockquote>
      <strong>Gravação de Podcast com Fernanda Vianna</strong><br>
      20 lugares, sujeita à lotação<br>
    </blockquote>
  </section>
	<section class="session" id="d17-s1">
	  <h3>
	    <a href="/mostra/paralela/curtas/" style="border-bottom: dotted 1px;"><i class="fa-solid fa-ticket-simple"></i> MOSTRA PARALELA DE CURTAS</a>
	    <span class="ci-box ci-14" role="img" aria-label="Classificação indicativa: não recomendado para menores de 14 anos">14</span><br />
	  	<i class="fa-solid fa-ticket"></i> SESSÃO FAÍSCA<br />
	    <i class="fa-solid fa-clock"></i> 15h <br />
	    <i class="fa-solid fa-location-dot"></i> Cine Theatro Santa Izabel
	  </h3>
		<blockquote>  
		  <strong><a href="/filme/serao/">Serão</a></strong><br>
		  (Caio Bernardo da Silva | 2024, PB, 15’)
		</blockquote>
		<blockquote>  
		  <strong><a href="/filme/incendio/">Incêndio</a></strong><br>
		  (Nico da Costa | 2024, CE, 5’)
		</blockquote>
		<blockquote>  
		  <strong><a href="/filme/e-seu-corpo-e-belo/">E Seu Corpo É Belo</a></strong><br>
		  (Yuri Costa | 2024, RJ, 23’)
		</blockquote>
		<blockquote>  
		  <strong><a href="/filme/inflamavel/">Inflamável</a></strong><br>
		  (Rafael Ribeiro Gontijo | 2024, DF, 19’)
		</blockquote>
		<blockquote>  
		  <strong><a href="/filme/babilonia/">Babilônia</a></strong><br>
		  (Duda Gambogi | 2024, Cuba/MG, 22’)
		</blockquote>
		<em>Comentada por curador</em>
	</section>
	<section class="session" id="d17-s2">
	  <h3>
	    <a href="/mostra/paralela/curtas/" style="border-bottom: dotted 1px;"><i class="fa-solid fa-ticket-simple"></i> MOSTRA PARALELA DE CURTAS </a>
	    <span class="ci-box ci-14" role="img" aria-label="Classificação indicativa: não recomendado para menores de 14 anos">14</span><br />
	  	<i class="fa-solid fa-ticket"></i> SESSÃO TRINCA<br />
	    <i class="fa-solid fa-clock"></i> 17h <br />
	    <i class="fa-solid fa-location-dot"></i> Cine Theatro Santa Izabel
	  </h3>
		<blockquote>
		  <strong><a href="/filme/a-invencao-do-orum/">A invenção do Orum</a></strong><br>
		  (Paulo Sena | 2025, ES, 18’)
		</blockquote>
		<blockquote>
		  <strong><a href="/filme/tres/">Três</a></strong><br>
		  (Lila Foster | 2024, DF, 21’)
		</blockquote>
		<blockquote>
		  <strong><a href="/filme/peixe-morto/">Peixe Morto</a></strong><br>
		  (João Fontenele | 2025, CE, 13’)
		</blockquote>
		<blockquote>
		  <strong><a href="/filme/marmita/">Marmita</a></strong><br>
		  (Guilherme Peraro | 2025, SP/PR, 21’)
		</blockquote>
	</section>
	<section class="session" id="d17-s3">
	  <h3>
	    <a href="/mostra/competitiva/longas/" style="border-bottom: dotted 1px;"><i class="fa-solid fa-ticket-simple"></i> MOSTRA COMPETITIVA DE LONGAS</a>
	    <span class="ci-box ci-l" role="img" aria-label="Classificação indicativa: Livre">L</span><br />
	  	<i class="fa-solid fa-film"></i> A Câmara<br />
	    <i class="fa-solid fa-clock"></i> 18h30 <br />
	    <i class="fa-solid fa-location-dot"></i> Cine Theatro Santa Izabel
	  </h3>
	  <blockquote>
	    <strong><a href="/filme/a-camara/">A Câmara</a></strong><br>
	    (Cristiane Brum Bernardes e Tiago Aragão | 2023, DF, 89’)<br>
	    <em>Comentada pelo diretor <strong>Tiago de Aragão Silva</strong></em>
	  </blockquote>
	</section>
	<section class="session" id="d17-s4">
	  <h3>
	    <a href="/mostra/competitiva/longas/" style="border-bottom: dotted 1px;"><i class="fa-solid fa-ticket-simple"></i> MOSTRA COMPETITIVA DE LONGAS</a>
	    <span class="ci-box ci-10" role="img" aria-label="Classificação indicativa: não recomendado para menores de 10 anos">10</span><br />
	  	<i class="fa-solid fa-film"></i> Aquele que Viu o Abismo<br />
	    <i class="fa-solid fa-clock"></i> 20h30 <br />
	    <i class="fa-solid fa-location-dot"></i> Cine Theatro Santa Izabel
	  </h3>
	  <blockquote>
			<strong><a href="/filme/aquele-que-viu-o-abismo/">Aquele que Viu o Abismo</a></strong><br>
	    (Gregorio Gananian e Negro Leo | 2025, SP, 70’)<br>
	    <em>Comentada pelo diretor <strong>Gregório Gananian</strong> e pela atriz <strong>Clara Choveaux Teles</strong></em>
	  </blockquote>
	</section>
	<section class="session" style="background-image: url('{{ site.images_path }}FotosPedroMiranda_fHist/PassadicoDaGloria_0003.jpg'); height: 500px; background-attachment: fixed;  background-size: cover; background-position-x: center;">
	</section>
</section>

<section class="day" id="d18">
  <h1>18/09, quinta-feira</h1>
	<section class="session" id="d18-s1">
	  <h3>
	    <i class="fa-solid fa-ticket-simple"></i> SESSÃO INFANTIL 
	    <span class="ci-box ci-l" role="img" aria-label="Classificação indicativa: Livre">L</span><br />
	    <i class="fa-solid fa-clock"></i> 10h <br />
	    <i class="fa-solid fa-location-dot"></i> Cine Theatro Santa Izabel
	  </h3>
		<blockquote>
		  <strong><a href="/filme/o-sonho-de-jequi/">O Sonho de Jequi</a></strong><br>
		  (Cecília Morbidoni e alunos da Escola Municipal Zilda Arns | 2024, MG, 2’)
		</blockquote>
		<blockquote>
		  <strong><a href="/filme/outro-lugar/">Outro Lugar</a></strong><br>
		  (Perseu Azul | 2024, MT, 15’)
		</blockquote>
		<blockquote>
		  <strong><a href="/filme/deia-e-dete/">Déia e Dete</a></strong><br>
		  (Bruna Schelb Corrêa e Francis Frank | 2025, MG, 8’)
		</blockquote>
		<blockquote>
		  <strong><a href="/filme/o-despertar-de-aiyra/">O Despertar de Aiyra</a></strong><br>
		  (Duda Rodrigues e Juliana Rogge | 2024, SP, 18’)
		</blockquote>
		<blockquote>
		  <strong><a href="/filme/tsuru/">Tsuru</a></strong><br>
		  (Pedro Anias | 2024, BA, 6’)
		</blockquote>
	</section>
	<section class="session" id="d18-s2">
	  <h3>
	    <i class="fa-solid fa-podcast"></i> Gravação de Podcast com o diretor Tiago de Aragão Silva<br />
	    <i class="fa-solid fa-clock"></i> 11h <br />
	    <i class="fa-solid fa-location-dot"></i> Galeria do Cine Theatro Santa Izabel
	  </h3>
	  <blockquote>
	    20 lugares, sujeita à lotação
	  </blockquote>
	</section>
	<section class="session" id="d18-s3">
	  <h3>
	    <i class="fa-solid fa-podcast"></i> Gravação de Podcast com o diretor Gregório Gananian e a atriz Clara Choveaux Teles<br />
	    <i class="fa-solid fa-clock"></i> 12h <br />
	    <i class="fa-solid fa-location-dot"></i> Galeria do Cine Theatro Santa Izabel
	  </h3>
	  <blockquote>
	    20 lugares, sujeita à lotação
	  </blockquote>
	</section>
	<section class="session" id="d18-s4">
	  <h3>
	    <a href="/mostra/paralela/curtas/" style="border-bottom: dotted 1px;"><i class="fa-solid fa-ticket-simple"></i> MOSTRA PARALELA DE CURTAS </a>
	    <span class="ci-box ci-l" role="img" aria-label="Classificação indicativa: Livre">L</span><br />
	    <i class="fa-solid fa-ticket"></i> SESSÃO INSCRIÇÕES<br />
	    <i class="fa-solid fa-clock"></i> 14h <br />
	    <i class="fa-solid fa-location-dot"></i> Cine Theatro Santa Izabel
	  </h3>
	<blockquote>
	  <strong><a href="/filme/sertao-america/">Sertão, América</a></strong><br>
	  (Marcela Ilha Bordin | 2023, ES, 18’)
	</blockquote>
	<blockquote>
	  <strong><a href="/filme/intercessoes/">Intercessões</a></strong><br>
	  (Anne France, Amanda Magaiver, João Pedro de Souza, Maria Eliene, Isis de Manaus, Gabriel Amaro, Miki Takano, Rebeca Lopes, Juliana Tizatto, Wander Braga, Sterfannÿ Oliveira, Raffaella Rosset, Bruma de Sá, Júlia dos Santos, Jade Couto, Bruna Polla, Raquel da Silva, Aline Fidelix, Luis Leite, Shalimar Lima, Hulgo Leite, Larissa Nascimento, Joedson Silva, Rodrigo Aquiles, Lucas Luan, André Pereira, Eliezer Rodrigues Silva, Vittoria San | 2024, AM, 3’)
	</blockquote>
	<blockquote>
	  <strong><a href="/filme/javyju-bom-dia/">Javyju - Bom dia</a></strong><br>
	  (Kunha Rete e Carlos Eduardo Magalhães | 2024, SP, 25’)
	</blockquote>
	<blockquote>
	  <strong><a href="/filme/canto-das-areias/">Canto das Areias</a></strong><br>
	  (Maíra Tristão | 2024, ES, 20’)
	</blockquote>
	<blockquote>
	  <strong><a href="/filme/pulmao-de-pedra/">Pulmão de Pedra</a></strong><br>
	  (Torquato Joel | 2023, PB, 14’)
	</blockquote>
	</section>
	<section class="session" id="d18-s5">
	  <h3>
	    <i class="fa-solid fa-ticket-simple"></i> SESSÃO ESPECIAL 
	    <span class="ci-box ci-l" role="img" aria-label="Classificação indicativa: Livre">L</span><br />
	    <i class="fa-solid fa-clock"></i> 15h30 <br />
	    <i class="fa-solid fa-location-dot"></i> Cine Theatro Santa Izabel
	  </h3>
	  <blockquote>
	    <strong>Estandartes a caminho</strong><br>
	    (Marithê Azevedo | 2025, MG, 26’)
	  </blockquote>
	  <em>Comentada pela diretora <strong>Marithê Azevedo</strong> e pelo artista plástico <strong>Marcelo Brant</strong></em>
	</section>
	<section class="session" id="d18-s6">
	  <h3>
	    <a href="/mostra/mineira" style="border-bottom: dotted 1px;"><i class="fa-solid fa-ticket-simple"></i> MOSTRA MINEIRA </a>
	    <span class="ci-box ci-16" role="img" aria-label="Classificação indicativa: não recomendado para menores de 16 anos">16</span><br />
	    <i class="fa-solid fa-clock"></i> 16h30 <br />
	    <i class="fa-solid fa-location-dot"></i> Cine Theatro Santa Izabel
	  </h3>
		<blockquote>
		  <strong><a href="/filme/tato/">Tato</a></strong><br>
		  (Pedro Carvalho | 2024, MG, 20’)
		</blockquote>
		<blockquote>
		  <strong><a href="/filme/europa-me-avise-quando-chegar/">Europa - Me Avise Quando Chegar</a></strong><br>
		  (Victor Vieira | 2024, MG, 9’)
		</blockquote>
		<blockquote>
		  <strong><a href="/filme/mae-do-ouro/">Mãe do Ouro</a></strong><br>
		  (Maick Hannder Lima Porto | 2024, MG, 14’)
		</blockquote>
		<blockquote>
		  <strong><a href="/filme/testemunho/">Testemunho</a></strong><br>
		  (Leonardo Amaral e Roberto Cotta | 2025, MG, 15’)
		</blockquote>
		<blockquote>
		  <strong><a href="/filme/ressaca/">Ressaca</a></strong><br>
		  (Pedro Estrada | 2024, MG, 15’)
		</blockquote>
	  <em>Comentada por curador</em>
	</section>
	<section class="session" id="d18-s7">
	  <h3>
	    <a href="/mostra/competitiva/longas/" style="border-bottom: dotted 1px;"><i class="fa-solid fa-ticket-simple"></i> MOSTRA COMPETITIVA DE LONGAS</a> 
	    <span class="ci-box ci-l" role="img" aria-label="Classificação indicativa: Livre">L</span><br />
		  	<i class="fa-solid fa-film"></i> As muitas mortes de Antônio Parreiras<br />
	    <i class="fa-solid fa-clock"></i> 18h30 <br />
	    <i class="fa-solid fa-location-dot"></i> Cine Theatro Santa Izabel
	  </h3>
		<blockquote>
		  <strong><a href="/filme/as-muitas-mortes-de-antonio-parreiras/">As muitas mortes de Antônio Parreiras</a></strong><br>
		  (Lucas Parente | 2025, RJ/CE, 65’)
		</blockquote>
	  <em>Comentada pelo diretor <strong>Lucas Parente</strong></em>
	</section>
	<section class="session" id="d18-s8">
	  <h3>
	    <a href="/mostra/competitiva/curtas/" style="border-bottom: dotted 1px;"><i class="fa-solid fa-ticket-simple"></i> MOSTRA COMPETITIVA DE CURTAS </a>
	    <span class="ci-box ci-12" role="img" aria-label="Classificação indicativa: não recomendado para menores de 12 anos">12</span><br />
	    <i class="fa-solid fa-clock"></i> 20h30 <br />
	    <i class="fa-solid fa-location-dot"></i> Cine Theatro Santa Izabel
	  </h3>
	  <blockquote>
	    <strong><a href="/filme/ver-ceu-no-chao/">Ver Céu no Chão</a></strong><br>
	    (Isabel Veiga | 2025, CE/RJ, 23’)<br>
	  </blockquote>
	  <blockquote>
	    <strong><a href="/filme/animais-noturnos/">Animais Noturnos</a></strong><br>
	    (Indigo Braga e Paulo Abrão | 2024, RJ, 11’)<br>
	  </blockquote>
	  <blockquote>
	    <strong><a href="/filme/cassino/">Cassino</a></strong><br>
	    (Gianluca Cozza | 2024, RS, 20’)<br>
	  </blockquote>
	  <blockquote>
	    <strong><a href="/filme/mae-da-manha/">Mãe da Manhã</a></strong><br>
	    (Clara Trevisan | 2024, RS, 8’)<br>
	  </blockquote>
	  <em>Comentada pelos diretores</em>
	</section>
	<section class="session" style="background-image: url('{{ site.images_path }}FotosPedroMiranda_fHist/PassadicoDaGloria_0001.jpg'); height: 500px; background-attachment: fixed;  background-size: cover; background-position-x: center;">
	</section>
</section>


<section class="day" id="d19">
  <h1>19/09, sexta-feira</h1>
	<section class="session" id="d19-s1">
	  <h3>
	    <i class="fa-solid fa-podcast"></i> Gravação de Podcast com o diretor Lucas Parente<br />
	    <i class="fa-solid fa-clock"></i> 11h <br />
	    <i class="fa-solid fa-location-dot"></i> Galeria do Cine Theatro Santa Izabel
	  </h3>
	  <blockquote>
	    20 lugares, sujeita à lotação
	  </blockquote>
	</section>
	<section class="session" id="d19-s2">
	  <h3>
	    <i class="fa-solid fa-ticket-simple"></i> SESSÃO JUVENIL 
	    <span class="ci-box ci-10" role="img" aria-label="Classificação indicativa: não recomendado para menores de 10 anos">10</span><br />
	    <i class="fa-solid fa-clock"></i> 11h <br />
	    <i class="fa-solid fa-location-dot"></i> Cine Theatro Santa Izabel
	  </h3>
		<blockquote>
		  <strong><a href="/filme/xarpi/">Xarpi</a></strong><br>
		  (Rafael Lobo | 2024, DF, 25’)
		</blockquote>
		<blockquote>
		  <strong><a href="/filme/pequeno-b/">Pequeno B</a></strong><br>
		  (Lucas Borges | 2025, MG, 14’)
		</blockquote>
		<blockquote>
		  <strong><a href="/filme/lanca-foguete/">Lança-Foguete</a></strong><br>
		  (William Oliveira | 2025, PE, 16’)
		</blockquote>
	  <em>Comentada por curador</em>
	</section>
	<section class="session" id="d19-s3">
	  <h3>
	    <i class="fa-solid fa-podcast"></i> Gravação de Podcast com diretores de curtas<br />
	    <i class="fa-solid fa-clock"></i> 12h <br />
	    <i class="fa-solid fa-location-dot"></i> Galeria do Cine Theatro Santa Izabel
	  </h3>
	  <blockquote>
	    20 lugares, sujeita à lotação
	  </blockquote>
	</section>
	<section class="session" id="d19-s4">
	  <h3>
	    <a href="/mostra/paralela/curtas/" style="border-bottom: dotted 1px;"><i class="fa-solid fa-ticket-simple"></i> MOSTRA PARALELA DE CURTAS </a>
	    <span class="ci-box ci-16" role="img" aria-label="Classificação indicativa: não recomendado para menores de 16 anos">16</span><br />
	    <i class="fa-solid fa-ticket"></i> SESSÃO FIGURAS/ BONEKAS<br />
	    <i class="fa-solid fa-clock"></i> 14h <br />
	    <i class="fa-solid fa-location-dot"></i> Cine Theatro Santa Izabel
	  </h3>
	<blockquote>
	  <strong><a href="/filme/vollupya/">Vollúpya</a></strong><br>
	  (Éri Sarmet e Jocimar Dias Jr. | 2024, RJ, 21’)
	</blockquote>
	<blockquote>
	  <strong><a href="/filme/mandinga-de-gorila/">Mandinga de Gorila</a></strong><br>
	  (Luzé Gonçalves e Juliana Gonçalves | 2024, RJ, 20’)
	</blockquote>
	<blockquote>
	  <strong><a href="/filme/samuel-foi-trabalhar/">Samuel foi trabalhar</a></strong><br>
	  (Janderson Felipe e Lucas Litrento | 2024, AL, 17’)
	</blockquote>
	<blockquote>
	  <strong><a href="/filme/estrela-brava/">Estrela Brava</a></strong><br>
	  (Jorge Polo | 2025, RJ, 24’)
	</blockquote>
	</section>
	<section class="session" id="d19-s5">
	  <h3>
	    <a href="/mostra/competitiva/curtas/" style="border-bottom: dotted 1px;"><i class="fa-solid fa-ticket-simple"></i> MOSTRA COMPETITIVA DE CURTAS </a>
	    <span class="ci-box ci-16" role="img" aria-label="Classificação indicativa: não recomendado para menores de 16 anos">16</span><br />
	    <i class="fa-solid fa-clock"></i> 16h <br />
	    <i class="fa-solid fa-location-dot"></i> Cine Theatro Santa Izabel
	  </h3>
	  <blockquote>
	    <strong><a href="/filme/princesa-macula-e-o-canto-triste/">Princesa Macula e o Canto Triste</a></strong><br>
	    (Mayara Mascarenhas | 2024, MG, 27’)<br>
	  </blockquote>
	  <blockquote>
	    <strong><a href="/filme/a-sua-imagem-na-minha-caixa-de-correio/">A sua imagem na minha caixa de correio</a></strong><br>
	    (Silvino Mendonça | 2024, DF, 17’)<br>
	  </blockquote>
	  <blockquote>
	    <strong><a href="/filme/benedita/">Benedita</a></strong><br>
	    (Lane Lopes e Cadu Azevedo | 2024, RJ, 19’)<br>
	  </blockquote>
	  <em>Comentada pelos diretores</em>
	</section>
	<section class="session" id="d19-s6">
	  <h3>
	    <a href="/mostra/competitiva/longas/" style="border-bottom: dotted 1px;"><i class="fa-solid fa-ticket-simple"></i> MOSTRA COMPETITIVA DE LONGAS</a> 
	    <span class="ci-box ci-10" role="img" aria-label="Classificação indicativa: não recomendado para menores de 10 anos">10</span><br />
	  	<i class="fa-solid fa-film"></i> Centro Ilusão<br />
	    <i class="fa-solid fa-clock"></i> 18h <br />
	    <i class="fa-solid fa-location-dot"></i> Cine Theatro Santa Izabel
	  </h3>
	  <blockquote>
	    <strong><a href="/filme/centro-ilusao/">Centro Ilusão</a></strong><br>
	    (Pedro Diogenes | 2024, CE, 85’)
	  </blockquote>
	  <em>Comentada pelo ator <strong>Bruno Kunk</strong></em>
	</section>
	<section class="session" id="d19-s7">
	  <h3>
	    <i class="fa-solid fa-ticket"></i> CINERATA<br />
	    <i class="fa-solid fa-ticket-simple"></i> Cinerata com trilha original executada ao vivo<br />
	    <i class="fa-solid fa-clock"></i> 20h <br />
	    <i class="fa-solid fa-location-dot"></i> Largo da Quitanda
	  </h3>
	  <blockquote>
	    <strong>One week</strong><br>
	    (Buster Keaton | 1920, EUA, 24’)
	  </blockquote>
	  <blockquote>
	    <strong>The Railrodder</strong><br>
	    (Gerald Potterton | 1965, EUA, 24’)
	  </blockquote>
	</section>
	<section class="session" id="d19-s8">
	  <h3>
	    <i class="fa-solid fa-music"></i> Show da banda Pulse Fiction<br />
	    <i class="fa-solid fa-clock"></i> 22h <br />
	    <i class="fa-solid fa-location-dot"></i> Casa do Elefante
	  </h3>
	  <blockquote>
	    R$ 20 - entrada
	  </blockquote>
	</section>
	<section class="session" style="background-image: url('{{ site.images_path }}FotosPedroMiranda_fHist/MercadoDiamantina_0009.jpg'); height: 500px; background-attachment: fixed;  background-size: cover; background-position-x: center;">
	</section>
</section>

<section class="day" id="d20">
  <h1>20/09, sábado</h1>
  <section class="session" id="d20-s1">
	  <h3>
	    <i class="fa-solid fa-podcast"></i> Gravação de Podcast com diretores de curtas<br />
	    <i class="fa-solid fa-clock"></i> 11h <br />
	    <i class="fa-solid fa-location-dot"></i> Galeria do Cine Theatro Santa Izabel
	  </h3>
	  <blockquote>
	    20 lugares, sujeita à lotação
	  </blockquote>
	</section>
	<section class="session" id="d20-s2">
	  <h3>
	    <i class="fa-solid fa-podcast"></i> Gravação de Podcast com o ator Bruno Kunk<br />
	    <i class="fa-solid fa-clock"></i> 12h <br />
	    <i class="fa-solid fa-location-dot"></i> Galeria do Cine Theatro Santa Izabel
	  </h3>
	</section>
	<section class="session" id="d20-s3">
	  <h3>
	    <i class="fa-solid fa-ticket-simple"></i> SESSÃO REGIONAL 
	    <span class="ci-box ci-l" role="img" aria-label="Classificação indicativa: Livre">L</span><br />
	    <i class="fa-solid fa-clock"></i> 14h <br />
	    <i class="fa-solid fa-location-dot"></i> Cine Theatro Santa Izabel
	  </h3>
		<blockquote>
		  <strong><a href="/filme/panha-de-flor/">Panha de Flor</a></strong><br>
		  (Ailton de Jesus dos Santos, Barbara de Paula Rocha, Emiliane Fernanda dos Santos, Flaviane Hermínia dos Santos Fernandes, Hugo Walber Alves, Raiane Daliane de Paula, Ronilda do Nascimento dos Santos, Sivany Aguiar | 2024, RJ/MG, 20’)
		</blockquote>
		<blockquote>
		  <strong><a href="/filme/lendas-do-tijuco/">Lendas do Tijuco</a></strong><br>
		  (Dilson Moreira | 2024, MG, 13’)
		</blockquote>
	  <em>Comentada pelos diretores</em>
	</section>
	<section class="session" id="d20-s4">
	  <h3>
	    <a href="/mostra/competitiva/curtas/" style="border-bottom: dotted 1px;"><i class="fa-solid fa-ticket-simple"></i> MOSTRA COMPETITIVA DE CURTAS </a>
	    <span class="ci-box ci-l" role="img" aria-label="Classificação indicativa: Livre">L</span><br />
	    <i class="fa-solid fa-clock"></i> 15h <br />
	    <i class="fa-solid fa-location-dot"></i> Cine Theatro Santa Izabel
	  </h3>
		<blockquote>
		  <strong><a href="/filme/cavaram-uma-cova-no-meu-coracao/">Cavaram uma cova no meu coração</a></strong><br>
		  (Ulisses Arthur | 2024, AL, 23’)
		</blockquote>
		<blockquote>
		  <strong><a href="/filme/cadeira-vazia/">Cadeira Vazia</a></strong><br>
		  (Ângela Maria, Ephigênia Lopes, Rosângela Lererê, Beth Couto, Maria Sônia, Nathan Souza, Adilson Luiz, Gabriela Coelho, Lucas Rodrigues, Mônica Maria, Nato Matrix | 2025, MG, 15’)
		</blockquote>
		<blockquote>
		  <strong><a href="/filme/confluencias/">Confluências</a></strong><br>
		  (Dácia Ibiapina | 2024, PI, 26’)
		</blockquote>
	  <em>Comentada pelos diretores</em>
	</section>
	<section class="session" id="d20-s5">
	  <h3>
	    <a href="/mostra/competitiva/longas/" style="border-bottom: dotted 1px;"><i class="fa-solid fa-ticket-simple"></i> MOSTRA COMPETITIVA DE LONGAS</a> 
	    <span class="ci-box ci-12" role="img" aria-label="Classificação indicativa: não recomendado para menores de 12 anos">12</span><br />
	    <i class="fa-solid fa-film"></i> Maçãs no escuro <br />
	    <i class="fa-solid fa-clock"></i> 17h <br />
	    <i class="fa-solid fa-location-dot"></i> Cine Theatro Santa Izabel
	  </h3>
	  <blockquote>
	    <strong><a href="/filme/macas-no-escuro/">Maçãs no escuro</a></strong><br>
	    (Tiago A. Neves | 2024, SP, 108’)
	  </blockquote>
	  <em>Conversa com o ator <strong>Edson Aquino</strong></em>
	</section>
	<section class="session" id="d20-s6">
	  <h3>
	    <i class="fa-solid fa-ticket-simple"></i> SESSÃO DE ENCERRAMENTO 
	    <span class="ci-box ci-12" role="img" aria-label="Classificação indicativa: não recomendado para menores de 12 anos">12</span><br />
	    <i class="fa-solid fa-clock"></i> 20h <br />
	    <i class="fa-solid fa-location-dot"></i> Praça do Mercado Velho
	  </h3>
	  <blockquote>
	    <strong><a href="/filme/o-dia-que-te-conheci/">O dia que te conheci</a></strong><br>
	    (André Novais | 2023, MG, 71’)
	  </blockquote>
	  <em>Comentada pelo ator <strong>Renato Novaes</strong></em>
	</section>
	<section class="session" id="d20-s7">
	  <h3>
	    <i class="fa-solid fa-award"></i> CERIMÔNIA DE PREMIAÇÃO E ENCERRAMENTO<br />
	    <i class="fa-solid fa-clock"></i> 22h <br />
	    <i class="fa-solid fa-location-dot"></i> Praça do Mercado Velho
	  </h3>
	</section>
	<section class="session" id="d20-s8">
	  <h3>
	    <i class="fa-solid fa-music"></i> Show de Tatio Abreu<br />
	    <i class="fa-solid fa-clock"></i> 22h30 <br />
	    <i class="fa-solid fa-location-dot"></i> Praça do Mercado V
		</h3>
	</section>
	<section class="session" style="background-image: url('{{ site.images_path }}FotosPedroMiranda_fHist/capistranas.jpg'); height: 500px; background-attachment: fixed;  background-size: cover; background-position-x: center;">
	</section>
</section>

<script>
function easeInOutCubic(t) {
  return t < 0.5
    ? 4 * t * t * t
    : 1 - Math.pow(-2 * t + 2, 3) / 2;
}

function easeInOutSine(t) {
  return -(Math.cos(Math.PI * t) - 1) / 2;
}

function smoothScrollTo(target, duration = 1000) {
  const startY = window.scrollY;
  const targetY = document.querySelector(target).getBoundingClientRect().top + startY;
  const diff = targetY - startY;
  let start;

  function step(timestamp) {
    if (!start) start = timestamp;
    const time = timestamp - start;
    const percent = Math.min(time / duration, 1);
    const eased = easeInOutSine(percent);
    window.scrollTo(0, startY + diff * eased);
    if (time < duration) requestAnimationFrame(step);
  }
  requestAnimationFrame(step);
}

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener("click", function(e) {
    e.preventDefault();
    smoothScrollTo(this.getAttribute("href"), 1200); // 1.2s
  });
});

</script>