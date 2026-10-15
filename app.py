from flask import Flask, render_template_string
 
app = Flask(__name__)
 
PAGE = r"""
<!doctype html>
<html lang="pt-PT">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#071522">
  <meta name="description" content="Riders — aventuras, estradas e viagens de mota.">
  <!-- >>> EDITAR: título que aparece no separador do browser -->
  <title>Riders | Estradas e aventuras</title>
  <style>
    :root {
      --bg: #071522; --panel: #10283a; --panel2: #16364b;
      --text: #f4f8fc; --muted: #a9bdcc; --blue: #1597f5;
      --cyan: #45d7e8; --line: rgba(255,255,255,.13);
    }
    * { box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body {
      margin: 0; color: var(--text); background: var(--bg);
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }
    a { color: inherit; }
    .nowrap { white-space: nowrap; } /* impede que o texto dentro mude de linha */
 
    .hero {
      min-height: 440px; position: relative; display: flex; align-items: center;
      overflow: hidden; isolation: isolate;
      background-image:
        linear-gradient(90deg, rgba(3,13,23,.82) 0%, rgba(3,13,23,.42) 52%, rgba(3,13,23,.18) 100%),
        linear-gradient(0deg, rgba(7,21,34,.78), transparent 50%),
        /* >>> EDITAR: link da imagem de fundo do topo (só mudas o endereço dentro de url("...")) */
        url("https://images.unsplash.com/photo-1558981806-ec527fa84c39?auto=format&fit=crop&w=2000&q=85");
      background-position: center, center, center 54%; background-size: cover;
    }
    .hero::after { content:""; position:absolute; inset:0; background:linear-gradient(0deg,var(--bg),transparent 24%); z-index:-1; }
    .topbar {
      position: absolute; top: 0; left: 0; right: 0; padding: 20px clamp(20px, 6vw, 84px);
      display:flex; justify-content:space-between; align-items:center; gap:20px;
      border-bottom: 1px solid rgba(255,255,255,.12); background:rgba(3,14,24,.28); backdrop-filter:blur(8px);
    }
    .brand { font-size: clamp(1.7rem, 4vw, 2.35rem); font-weight: 900; letter-spacing:-.06em; font-style:italic; text-decoration:none; }
    .brand span { color:var(--cyan); }
    .topnote { color:#d8e6ef; font-size:.9rem; letter-spacing:.13em; text-transform:uppercase; }
    .hero-content { width:min(1180px, 100%); margin:0 auto; padding:125px 28px 80px; }
    .eyebrow { color:var(--cyan); text-transform:uppercase; letter-spacing:.22em; font-weight:800; font-size:.78rem; }
 
    /* Título principal: fica sempre numa só linha.
       O tamanho da letra adapta-se à largura do ecrã (entre 1.7rem e 5rem). */
    h1 {
      font-size: clamp(1.7rem, 6.4vw, 5rem);
      line-height: 1.02; margin: 15px 0 18px;
      letter-spacing: -.055em; white-space: nowrap;
    }
    h1 em { color:var(--cyan); font-style:normal; }
    .intro { max-width:530px; color:#d6e3ec; font-size:clamp(1rem, 2vw, 1.15rem); line-height:1.7; }
    .cta { display:inline-flex; align-items:center; gap:10px; margin-top:20px; text-decoration:none; font-weight:800; padding:14px 22px; border-radius:999px; background:linear-gradient(110deg,var(--blue),#0873d5); box-shadow:0 10px 28px #008bff3b; transition:transform .2s,filter .2s; }
    .cta:hover { transform:translateY(-2px); filter:brightness(1.12); }
    nav { position:relative; z-index:2; width:min(1120px, calc(100% - 32px)); margin:-29px auto 0; display:grid; grid-template-columns:repeat(5,minmax(0,1fr)); gap:10px; }
    .nav-btn { cursor:pointer; border:1px solid var(--line); border-radius:15px; padding:15px 12px; background:rgba(16,40,58,.94); color:var(--text); font:inherit; font-weight:750; display:flex; justify-content:center; align-items:center; gap:9px; box-shadow:0 10px 24px #0003; transition:background .2s,transform .2s,border-color .2s; }
    .nav-btn:hover { transform:translateY(-3px); border-color:#45d7e8a0; }
    .nav-btn:focus-visible { outline:2px solid var(--cyan); outline-offset:3px; }
    .nav-btn.active { background:linear-gradient(120deg,#168ff0,#0873d5); border-color:transparent; box-shadow:0 8px 24px #0788f74a; }
    main { width:min(1120px, calc(100% - 32px)); margin:38px auto 70px; }
    .section-head { display:flex; justify-content:center; align-items:end; gap:16px; margin-bottom:18px; }
    .section-head h2 { margin:0; font-size:clamp(1.5rem,3vw,2rem); letter-spacing:-.035em; }
 
    /* Painel de conteúdo */
    .content-panel {
      border:1px solid var(--line); border-radius:24px;
      padding:clamp(22px,4vw,44px);
      background:radial-gradient(ellipse at 50% 0%, #17415a 0%, #0d2435 48%, #091a28 100%);
      box-shadow:0 22px 60px #0002;
    }
    .content-inner { animation:entrada .35s ease; }
    @keyframes entrada { from { opacity:0; transform:translateY(8px); } to { opacity:1; transform:none; } }
    .content-panel h3 { margin:0 0 14px; font-size:clamp(1.5rem,3.4vw,2.2rem); letter-spacing:-.03em; }
    .content-text { max-width:72ch; margin:0 0 28px; color:#d3e1ea; font-size:1.05rem; line-height:1.75; }
    .gallery { display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:12px; margin:0; padding:0; list-style:none; }
    .gallery li { margin:0; }
    .gallery img {
      display:block; width:100%; aspect-ratio:4/3; object-fit:cover;
      border-radius:14px; border:1px solid var(--line); background:var(--panel2);
      cursor:zoom-in; transition:transform .2s, border-color .2s;
    }
    .gallery img:hover { transform:scale(1.03); border-color:#45d7e8a0; }

 /* >>> EDITAR: aspeto do botão "Voltar ao início" */
.btn-voltar {
  display:flex; margin:28px auto 0; cursor:pointer;
  border:1px solid var(--line); border-radius:999px; padding:12px 22px;
  background:rgba(16,40,58,.94); color:var(--text);
  font:inherit; font-weight:750; transition:background .2s, border-color .2s, transform .2s;
}

.btn-voltar:hover { transform:translateY(-2px); border-color:#45d7e8a0; }
.btn-voltar:focus-visible { outline:2px solid var(--cyan); outline-offset:3px; }
    /* Imagem inicial (antes de clicar em qualquer rota) */
    .inicial-img {
  display:block; width:100%; max-height:70vh; object-fit:contain;
  margin:0 auto;
  border-radius:16px; border:1px solid var(--line); background:var(--panel2);
}
 
    /* Ampliar foto */
    .lightbox { position:fixed; inset:0; z-index:50; display:none; place-items:center; padding:20px; background:rgba(3,10,17,.92); cursor:zoom-out; }
    .lightbox.open { display:grid; }
    .lightbox img { max-width:100%; max-height:90vh; border-radius:12px; }
 
    footer { border-top:1px solid var(--line); background:#04101a; padding:24px 20px; }
    .footer-inner { width:min(1120px,100%); margin:auto; display:flex; justify-content:space-between; align-items:center; gap:14px; flex-wrap:wrap; color:var(--muted); font-size:.92rem; }
    footer a { color:var(--text); text-decoration:none; } footer a:hover { color:var(--cyan); }
    .footer-brand { font-weight:900; color:var(--text); letter-spacing:-.04em; }
    @media (max-width:720px) {
      .hero { min-height:450px; background-position:center,center,62% center; }
      .topbar { padding:17px 20px; } .topnote { display:none; }
      .hero-content { padding:130px 22px 75px; }
      nav { grid-template-columns:repeat(2,minmax(0,1fr)); margin-top:-22px; gap:8px; }
      .nav-btn { padding:14px 8px; font-size:.92rem; }
      .nav-btn:last-child { grid-column:1 / -1; }
      main { margin-top:32px; }
      .section-head { align-items:center; flex-direction:column; }
      .content-panel { border-radius:20px; }
      .gallery { grid-template-columns:repeat(2,minmax(0,1fr)); }
      .footer-inner { justify-content:center; text-align:center; flex-direction:column; }
    }
    @media (prefers-reduced-motion:reduce) {
      * { scroll-behavior:auto !important; transition:none !important; animation:none !important; }
    }
  </style>
</head>
<body>
  <header class="hero" id="inicio">
    <div class="topbar">
      <a class="brand" href="#inicio" aria-label="Riders página inicial">Riders<span>.</span></a>
      <!-- >>> EDITAR: frase pequena no canto superior direito -->
      <div class="topnote">Mais estrada, Mais histórias.</div>
    </div>
    <div class="hero-content">
      <!-- >>> EDITAR: texto pequeno por cima do título -->
      <!--<div class="eyebrow">A liberdade .....</div>-->
      <!-- >>> EDITAR: título principal (a palavra dentro de <em> fica a azul) -->
      <h1>8 <em>motas.</em> Mil <em>aventuras.</em></h1>
      <!-- >>> EDITAR: texto de apresentação. O que estiver dentro de <span class="nowrap"> fica sempre na mesma linha -->
      <p class="intro"> <span> Estradas incríveis, paisagens sem fim e histórias para partilhar entre amigos.</span></p>
      
      <!-- <a class="cta" href="#rotas" id="explore">As nossas rotas <span aria-hidden="true">→</span></a> -->
      
    </div>
  </header>
 
  <!-- >>> EDITAR: botões das rotas.
       Se mudares o nome de um botão, muda também o data-section="..."
       e o nome correspondente no bloco CONTEUDO (mais abaixo, no script). -->
  <nav id="rotas" aria-label="Menu de rotas">
    <button class="nav-btn" type="button" data-section="N2">⌁ <span>N2</span></button>
    <button class="nav-btn" type="button" data-section="Rota Norte">✧ <span>Rota Norte</span></button>
    <button class="nav-btn" type="button" data-section="Rota Sul">◈ <span>Rota Sul</span></button>
    <button class="nav-btn" type="button" data-section="Picos Europa">△ <span>Picos Europa</span></button>
    <button class="nav-btn" type="button" data-section="Party">✦ <span>Party</span></button>
  </nav>
 
  <main>
    <div class="section-head">
      <!-- O texto deste título muda no script; o que está aqui é só o inicial (ver TITULO_INICIAL no script) -->
      <h2 id="section-title"></h2>
    </div>
    <section class="content-panel" aria-live="polite" id="content-panel"></section>
  </main>
 
  <div class="lightbox" id="lightbox" aria-hidden="true">
    <img id="lightbox-img" alt="">
  </div>
 
  <footer>
    <div class="footer-inner">
      <span class="footer-brand">RIDERS<span style="color:var(--cyan)">.</span></span>
      <span>© <span id="year"></span> Riders · Feito para quem vive a estrada</span>
      <!-- >>> EDITAR: email de contacto (altera nos dois sítios: no mailto: e no texto) -->
      <a href="mailto:hugoxala@gmail.com">✉ hugoxala@gmail.com</a>
    </div>
  </footer>
 
  <script>
    /* ===========================================================
       >>> EDITAR (1/4): ESTADO INICIAL
       O que aparece quando o site abre, antes de clicar em qualquer rota.
       =========================================================== */
    const TITULO_INICIAL = "Aventuras";                                   // título por cima do painel
    const IMAGEM_INICIAL = "/static/fotos/1.jpg"; // <<< troca pelo link ou caminho da tua imagem
    const DESCRICAO_IMAGEM_INICIAL = "Imagem de apresentação dos Riders";  // texto alternativo (acessibilidade)
 
    /* ===========================================================
       >>> EDITAR (2/4): CONTEÚDO DAS ROTAS
       "padrao" aparece em todas as rotas que não tenham conteúdo próprio.
       Para uma rota ter o seu conteúdo, acrescenta uma entrada com o nome
       exato do botão (igual ao data-section), por exemplo:
         "Rota Norte": { titulo: "...", texto: "...", fotos: ["f1.jpg","f2.jpg","f3.jpg","f4.jpg"] },
       Cada rota mostra 4 fotos.
       =========================================================== */
    const CONTEUDO = {
      "padrao": {
        titulo: "Um fim de tarde em Porto",
        texto: "Estou nos meus últimos dias no Porto, a aproveitar o encanto desta cidade que consegue ser antiga e moderna ao mesmo tempo. Conheci cantos que pareciam distantes de mim até há poucos meses. O que mais me impressionou foi a facilidade de ter contacto direto com uma história viva — caminhar por ruas de granito, ouvir o som do Douro e ver a luz dourada a refletir nos telhados. Numa viagem, a rotina desaparece e cada esquina torna-se uma pequena descoberta.",
        fotos: [
          "https://picsum.photos/seed/riders1/800/600",   // <<< foto 1
          "https://picsum.photos/seed/riders2/800/600",   // <<< foto 2
          "https://picsum.photos/seed/riders3/800/600",   // <<< foto 3
          "https://picsum.photos/seed/riders4/800/600"    // <<< foto 4
        ]
      }
      // Exemplo de conteúdo próprio (tira as barras // para usar e não te esqueças da vírgula na linha de cima):
      // "Rota Norte": { titulo: "Título da rota", texto: "O teu texto...", fotos: ["img1.jpg", "img2.jpg", "img3.jpg", "img4.jpg"] }
    };
 
    /* ===========================================================
       >>> EDITAR (3/4): TÍTULO POR CIMA DO PAINEL
       Se uma rota não estiver aqui, usa o nome do próprio botão.
       =========================================================== */
    const TITULOS = {
      "N2": "Nacional 2 - 2024"
      // "Rota Norte": "Rota Norte - 2025",
    };
 
    /* ===========================================================
       (4/4) DAQUI PARA BAIXO É O FUNCIONAMENTO — normalmente não é preciso mexer
       =========================================================== */
    const buttons = document.querySelectorAll(".nav-btn");
    const sectionTitle = document.getElementById("section-title");
    const panel = document.getElementById("content-panel");
    const lightbox = document.getElementById("lightbox");
    const lightboxImg = document.getElementById("lightbox-img");
 
    function mostrarInicial() {
      sectionTitle.textContent = TITULO_INICIAL;
      panel.innerHTML = "";
      const inner = document.createElement("div");
      inner.className = "content-inner";
      const img = document.createElement("img");
      img.className = "inicial-img";
      img.src = IMAGEM_INICIAL;
      img.alt = DESCRICAO_IMAGEM_INICIAL;
      inner.appendChild(img);
      panel.appendChild(inner);
    }
 
     // Volta ao estado inicial, como se o site tivesse acabado de abrir
function voltarInicio() {
  buttons.forEach(item => {
    item.classList.remove("active");
    item.setAttribute("aria-pressed", "false");
  });
  mostrarInicial();
  window.scrollTo({ top: 0, behavior: "smooth" });
}

    function mostrar(secao) {
      const c = CONTEUDO[secao] || CONTEUDO["padrao"];
      sectionTitle.textContent = TITULOS[secao] || secao;
 
      panel.innerHTML = "";
      const inner = document.createElement("div");
      inner.className = "content-inner";
 
      const h3 = document.createElement("h3");
      h3.textContent = c.titulo;
 
      const p = document.createElement("p");
      p.className = "content-text";
      p.textContent = c.texto;
 
      const ul = document.createElement("ul");
      ul.className = "gallery";
      c.fotos.slice(0, 4).forEach((src, i) => {
        const li = document.createElement("li");
        const img = document.createElement("img");
        img.src = src;
        img.loading = "lazy";
        img.alt = c.titulo + " — foto " + (i + 1);
        img.addEventListener("click", () => {
          lightboxImg.src = src;
          lightboxImg.alt = img.alt;
          lightbox.classList.add("open");
          lightbox.setAttribute("aria-hidden", "false");
        });
        li.appendChild(img);
        ul.appendChild(li);
      });
 
      // >>> EDITAR: texto do botão que volta ao início
const voltar = document.createElement("button");
voltar.type = "button";
voltar.className = "btn-voltar";
voltar.textContent = "← Voltar ao início";
voltar.addEventListener("click", voltarInicio);

inner.append(h3, p, ul, voltar);

      panel.appendChild(inner);
    }
 
    buttons.forEach(button => {
      button.setAttribute("aria-pressed", "false");
      button.addEventListener("click", () => {
        buttons.forEach(item => {
          item.classList.remove("active");
          item.setAttribute("aria-pressed", "false");
        });
        button.classList.add("active");
        button.setAttribute("aria-pressed", "true");
        mostrar(button.dataset.section);
      });
    });
 
    function fecharLightbox() {
      lightbox.classList.remove("open");
      lightbox.setAttribute("aria-hidden", "true");
    }
    lightbox.addEventListener("click", fecharLightbox);
    document.addEventListener("keydown", e => { if (e.key === "Escape") fecharLightbox(); });
 
    document.getElementById("year").textContent = new Date().getFullYear();
    mostrarInicial();   // ao abrir o site, nenhuma rota está ativa: mostra só a imagem inicial
  </script>
</body>
</html>
"""
 
@app.route("/")
def home():
    return render_template_string(PAGE)
 
if __name__ == "__main__":
    # Acessível na rede local; para partilhar com amigos fora de casa, publica o site online.
    app.run(host="0.0.0.0", port=5000, debug=True)
