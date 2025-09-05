---
layout: landing
title: Mostras
description: 'Com duas mostras competitivas, de longas e curtas-metragens, o II Festival de Cinema de Diamantina '
image: lens_flare/FCD25_lensflare-red_2160x1920_35x150.png
permalink: /mostras
nav-menu: true
show_tile: true
nav-menu-order: 3
---

<!-- Main -->
<div id="main">

<!-- Two -->
<section id="two" class="spotlights">
	<section>
		<a href="{{ '/mostra/competitiva/curtas/' | relative_url }}" class="image">
			<img src="/assets/press/a-sua-imagem-na-minha-caixa-de-correio.jpg" alt="" data-position="25% 25%" />
		</a>
		<div class="content">
			<a href="{{ '/mostra/competitiva/curtas/' | relative_url }}">
				<div class="inner">
					<header class="major">
						<h3>Mostra Competitiva de Curtas</h3>
					</header>
					{% assign curtas_page = site.pages | where: "url", "/mostra/competitiva/curtas/" | first %}
					<p>{{ curtas_page.description }}</p>
					<ul class="actions">
						<li><a href="{{ '/mostra/competitiva/curtas/' | relative_url }}" class="button">Saiba mais...</a></li>
					</ul>
				</div>
			</a>
		</div>
	</section>
	<section>
		<a href="{{ '/mostra/competitiva/longas/' | relative_url }}" class="image">
			<img src="/assets/press/macas-no-escuro.jpg" alt="" data-position="center center" />
		</a>
		<div class="content">
			<a href="{{ '/mostra/competitiva/longas/' | relative_url }}">
				<div class="inner">
					<header class="major">
						<h3>Mostra Competitiva de Longas</h3>
					</header>
					{% assign longas_page = site.pages | where: "url", "/mostra/competitiva/longas/" | first %}
					<p>{{ longas_page.description }}</p>
					<ul class="actions">
						<li><a href="{{ '/mostra/competitiva/longas/' | relative_url }}" class="button">Saiba mais...</a></li>
					</ul>
				</div>
			</a>
		</div>
	</section>
	<section>
		<a href="{{ '/mostra/paralela/curtas/' | relative_url }}" class="image">
			<img src="/assets/press/javyju-bom-dia.jpg" alt="" data-position="center center" />
		</a>
		<div class="content">
			<a href="{{ '/mostra/paralela/curtas/' | relative_url }}">
				<div class="inner">
					<header class="major">
						<h3>Mostra Paralela de Curtas</h3>
					</header>
					{% assign curtas_page = site.pages | where: "url", "/mostra/paralela/curtas/" | first %}
					<p>{{ curtas_page.description }}</p>
					<ul class="actions">
						<li><a href="{{ '/mostra/paralela/curtas/' | relative_url }}" class="button">Saiba mais...</a></li>
					</ul>
				</div>
			</a>
		</div>
	</section>
	<section>
		<a href="{{ '/mostra/mineira' | relative_url }}" class="image">
			<img src="/assets/press/ressaca.jpg" alt="" data-position="center center" />
		</a>
		<div class="content">
			<a href="{{ '/mostra/mineira' | relative_url }}">
				<div class="inner">
					<header class="major">
						<h3>Mostra Mineira</h3>
					</header>
					{% assign mineira_page = site.pages | where: "url", "/mostra/mineira" | first %}
					<p>{{ mineira_page.description }}</p>
					<ul class="actions">
						<li><a href="{{ '/mostra/mineira' | relative_url }}" class="button">Saiba mais...</a></li>
					</ul>
				</div>
			</a>
		</div>
	</section>


</section>

</div>
