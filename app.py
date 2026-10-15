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
    .hero {
      min-height: 440px; position: relative; display: flex; align-items: center;
      overflow: hidden; isolation: isolate;
      background:
        linear-gradient(90deg, rgba(3,13,23,.83) 0%, rgba(3,13,23,.48) 48%, rgba(3,13,23,.13) 100%),
        linear-gradient(0deg, rgba(7,21,34,.8), transparent 45%),
        url("https://images.unsplash.com/photo-151968 sal?auto=format&fit=crop&w=2000&q=85");
      background-image:
        linear-gradient(90deg, rgba(3,13,23,.82) 0%, rgba(3,13,23,.42) 52%, rgba(3,13,23,.18) 100%),
        linear-gradient(0deg, rgba(7,21,34,.78), transparent 50%),
        url("https://images.unsplash.com/photo-1558981806-ec527fa84c39?auto=format&fit=crop&w=2000&q=85");
      background-position: center, center, center 54%; background-size: cover;
    }
    .hero::after { content:""; position:absolute; inset:0; background:linear-gradient(0deg,var(--bg),transparent 24%); z-index:-1; }
    .topbar {
      position: absolute; top: 0; left: 0; right: 0; padding: 20px clamp(20px, 6vw, 84px);
      display:flex; justify-content:space-between; align-items:center; gap:20px;
      border-bottom: 1px solid rgba(255,255,255,.12); background:rgba(3,14,24,.28); backdrop-filter:blur(8px);
    }
    .brand { font-size: clamp(1.7rem, 4vw, 2.35rem); font-weight: 900; letter-spacing:-.06em; font-style:italic; }
    .brand span { color:var(--cyan); }
    .topnote { color:#d8e6ef; font-size:.9rem; letter-spacing:.13em; text-transform:uppercase; }
    .hero-content { width:min(1180px, 100%); margin:0 auto; padding:125px 28px 80px; }
    .eyebrow { color:var(--cyan); text-transform:uppercase; letter-spacing:.22em; font-weight:800; font-size:.78rem; }
    h1 { font-size:clamp(2.8rem, 7vw, 5.8rem); line-height:.98; margin:15px 0 18px; max-width:720px; letter-spacing:-.055em; }
    h1 em { color:var(--cyan); font-style:normal; }
    .intro { max-width:530px; color:#d6e3ec; font-size:clamp(1rem, 2vw, 1.15rem); line-height:1.7; }
    .cta { display:inline-flex; align-items:center; gap:10px; margin-top:20px; text-decoration:none; font-weight:800; padding:14px 22px; border-radius:999px; background:linear-gradient(110deg,var(--blue),#0873d5); box-shadow:0 10px 28px #008bff3b; transition:transform .2s,filter .2s; }
    .cta:hover { transform:translateY(-2px); filter:brightness(1.12); }
    nav { position:relative; z-index:2; width:min(1120px, calc(100% - 32px)); margin:-29px auto 0; display:grid; grid-template-columns:repeat(5,minmax(0,1fr)); gap:10px; }
    .nav-btn { cursor:pointer; border:1px solid var(--line); border-radius:15px; padding:15px 12px; background:rgba(16,40,58,.94); color:var(--text); font:inherit; font-weight:750; display:flex; justify-content:center; align-items:center; gap:9px; box-shadow:0 10px 24px #0003; transition:background .2s,transform .2s,border-color .2s; }
    .nav-btn:hover { transform:translateY(-3px); border-color:#45d7e8a0; }
    .nav-btn.active { background:linear-gradient(120deg,#168ff0,#0873d5); border-color:transparent; box-shadow:0 8px 24px #0788f74a; }
    main { width:min(1120px, calc(100% - 32px)); margin:38px auto 70px; }
    .section-head { display:flex; justify-content:space-between; align-items:end; gap:16px; margin-bottom:18px; }
    .section-head h2 { margin:0; font-size:clamp(1.5rem,3vw,2rem); letter-spacing:-.035em; }
    .section-head p { margin:0; color:var(--muted); font-size:.92rem; }
    .content-panel { min-height:300px; border:1px solid var(--line); border-radius:24px; padding:clamp(28px,6vw,64px) 24px; display:grid; place-items:center; text-align:center; background:radial-gradient(ellipse at 50% 0%, #17415a 0%, #0d2435 48%, #091a28 100%); box-shadow:0 22px 60px #0002; }
    .content-inner { max-width:570px; }
    .content-icon { width:70px; height:70px; display:grid; place-items:center; margin:0 auto 22px; border:1px solid #45d7e86b; border-radius:22px; color:var(--cyan); background:#45d7e812; font-size:2rem; }
    .content-panel h3 { margin:0 0 12px; font-size:clamp(1.6rem,4vw,2.3rem); }
    .content-panel p { color:var(--muted); font-size:1.08rem; margin:0; }
    .loading-line { height:3px; width:64px; border-radius:10px; margin:25px auto 0; background:linear-gradient(90deg,var(--blue),var(--cyan)); }
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
      .section-head { align-items:start; flex-direction:column; }
      .content-panel { min-height:270px; border-radius:20px; }
      .footer-inner { justify-content:center; text-align:center; flex-direction:column; }
    }
    @media (prefers-reduced-motion:reduce) { * { scroll-behavior:auto !important; transition:none !important; } }
  </style>
</head>
<body>
  <header class="hero" id="inicio">
    <div class="topbar">
      <a class="brand" href="#inicio" aria-label="Riders página inicial">Riders<span>.</span></a>
      <div class="topnote">Mais estrada. Mais histórias.</div>
    </div>
    <div class="hero-content">
      <div class="eyebrow">A liberdade começa aqui</div>
      <h1>Uma mota.<br>Mil <em>aventuras.</em></h1>
      <p class="intro">Estradas incríveis, paisagens de montanha e boas histórias para partilhar entre amigos. Escolhe o próximo destino.</p>
      <a class="cta" href="#rotas" id="explore">Explorar as rotas <span aria-hidden="true">→</span></a>
    </div>
  </header>

  <nav id="rotas" aria-label="Menu de rotas">
    <button class="nav-btn active" type="button" data-section="N2">⌁ <span>N2</span></button>
    <button class="nav-btn" type="button" data-section="Rota Norte">✧ <span>Rota Norte</span></button>
    <button class="nav-btn" type="button" data-section="Rota Sul">◈ <span>Rota Sul</span></button>
    <button class="nav-btn" type="button" data-section="Picos Europa">△ <span>Picos Europa</span></button>
    <button class="nav-btn" type="button" data-section="Party">✦ <span>Party</span></button>
  </nav>

  <main>
    <div class="section-head">
      <h2 id="section-title">A próxima aventura</h2>
      <p>Escolhe um menu para explorar.</p>
    </div>
    <section class="content-panel" aria-live="polite">
      <div class="content-inner">
        <div class="content-icon" id="section-icon" aria-hidden="true">⌁</div>
        <h3 id="content-title">N2</h3>
        <p id="content-message">á espera de conteudo ....</p>
        <div class="loading-line"></div>
      </div>
    </section>
  </main>

  <footer>
    <div class="footer-inner">
      <span class="footer-brand">RIDERS<span style="color:var(--cyan)">.</span></span>
      <span>© <span id="year"></span> Riders · Feito para quem vive a estrada</span>
      <a href="mailto:hugoxala@gmail.com">✉ hugoxala@gmail.com</a>
    </div>
  </footer>
  <script>
    const icons = { "N2": "⌁", "Rota Norte": "✧", "Rota Sul": "◈", "Picos Europa": "△", "Party": "✦" };
    const buttons = document.querySelectorAll(".nav-btn");
    const title = document.getElementById("content-title");
    const icon = document.getElementById("section-icon");
    const sectionTitle = document.getElementById("section-title");
    buttons.forEach(button => {
      button.addEventListener("click", () => {
        buttons.forEach(item => {
          item.classList.remove("active");
          item.setAttribute("aria-pressed", "false");
        });
        button.classList.add("active");
        button.setAttribute("aria-pressed", "true");
        const section = button.dataset.section;
        title.textContent = section;
        sectionTitle.textContent = section === "N2" ? "A próxima aventura" : section;
        icon.textContent = icons[section];
        document.getElementById("content-message").textContent = "á espera de conteudo ....";
      });
      button.setAttribute("aria-pressed", button.classList.contains("active") ? "true" : "false");
    });
    document.getElementById("year").textContent = new Date().getFullYear();
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
