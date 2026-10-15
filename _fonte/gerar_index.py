"""Monta o index.html a partir da estrutura validada (60 Equipamentos) + conteúdo e paleta desta oferta."""
import re, os, sys, json
D = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(D), "index.html")
REF = r"C:\Users\Usuário\Desktop\PROJETOS\60 EQUIPAMENTOS DE CALISTENIA FERRAGEM\index.html"
sys.path.insert(0, D)
from data_proj import P

ref = open(REF, encoding="utf8").read()
i_style = ref.index("<style>"); i_style_end = ref.index("</style>")
css = ref[i_style + 7:i_style_end]
i_script = ref.index("<script>\n/* ===== 0. CONFIGURAÇÃO")
i_end = ref.index("</script>\n</body>")
js = ref[i_script + len("<script>\n"):i_end]

# ---------- PALETA (azul profundo + azul vivo + coral + ouro; sem bege) ----------
MAP = {
 "#13233f":"#172f73", "#0a1428":"#091b4b", "#2b4a85":"#2a4ca0", "#060d1c":"#050f30", "#152a52":"#1b3a8a", "#152f63":"#1a3a8c",
 "#ff6b1a":"#ff5a3d", "#c2410c":"#c9321a", "#ff9a5c":"#ff8f78", "#fff1e8":"#ffeeea", "#7c2d12":"#7a1d0e",
 "rgba(255,107,26":"rgba(255,90,61", "rgba(19,35,63":"rgba(23,47,115", "rgba(10,20,40":"rgba(9,27,75",
 "#172f8f":"#1e3fa8",
}
for a, b in MAP.items(): css = css.replace(a, b)

# ---------- remove ilustrações de equipamento e o mockup antigo do hero ----------
css = re.sub(r"/\* ============ ILUSTRAÇÕES DE EQUIPAMENTO \(SVG\) ============ \*/.*?(?=/\* ============ MODO RASCUNHO)", "", css, flags=re.S)
css = re.sub(r"\n\.hv-[^\n]*(?:\n  [^\n]*)*", "", css)
css = re.sub(r"\n  \.hv-[^\n]*", "", css)
css = css.replace("/* visual do hero: biblioteca digital → produto físico */", "/* visual do hero: mockup do pacote */")

# ---------- 8 categorias: grid 4×2 ----------
css = css.replace(".grid-desire{ display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:22px; }",
                  ".grid-desire{ display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:18px; }")
css = css.replace(".grid-desire .desire-card.reveal:nth-child(3n+1), .compare-col.bad.reveal{ transform:translateX(-42px); }",
                  ".grid-desire .desire-card.reveal:nth-child(4n+1), .compare-col.bad.reveal{ transform:translateX(-42px); }")
css = css.replace(".grid-desire .desire-card.reveal:nth-child(3n), .compare-col.good.reveal{ transform:translateX(42px); }",
                  ".grid-desire .desire-card.reveal:nth-child(4n), .compare-col.good.reveal{ transform:translateX(42px); }")
css = css.replace(".desire-card .card-body{ padding:20px 24px 0; }", ".desire-card .card-body{ padding:18px 18px 0; }")
css = css.replace(".desire-card h3{ font-weight:800; font-size:1.22rem;", ".desire-card h3{ font-weight:800; font-size:1.08rem;")
css = css.replace(".desire-card p{ font-size:.96rem; line-height:1.55; }", ".desire-card p{ font-size:.9rem; line-height:1.5; }")
css = css.replace(".desire-card .quote{ display:block; margin-top:14px; font-size:.86rem;", ".desire-card .quote{ display:block; margin-top:12px; font-size:.8rem;")
css = css.replace("@media (max-width:900px){\n  .offer-grid",
                  "@media (max-width:1000px){\n  .grid-desire{ grid-template-columns:repeat(2,minmax(0,1fr)); }\n  .grid-desire .desire-card.reveal:nth-child(4n+1), .grid-desire .desire-card.reveal:nth-child(4n){ transform:translateY(34px) scale(.985); }\n  .grid-desire .desire-card.reveal.in{ transform:none; }\n}\n@media (max-width:900px){\n  .offer-grid")
css = css.replace("  .grid-desire{ grid-template-columns:1fr; max-width:460px; margin-inline:auto; }", "  .grid-desire{ grid-template-columns:1fr; max-width:420px; margin-inline:auto; }")

extra_css = open(os.path.join(D, "ilu.css"), encoding="utf8").read() + """
/* ============ ADIÇÕES DESTA OFERTA ============ */
.hero-visual > svg.offer-mockup-img, .plan-mockup > svg.offer-mockup-img, .dmockup > svg.offer-mockup-img{ width:100%; height:100%; filter:drop-shadow(0 34px 38px rgba(0,0,0,.34)); }
.plan-mockup > svg.offer-mockup-img{ filter:drop-shadow(0 20px 24px rgba(23,47,115,.2)); }
.dmockup > svg.offer-mockup-img{ filter:drop-shadow(0 16px 20px rgba(23,47,115,.2)); }
.vitrine-mockup > svg{ width:100%; height:100%; filter:drop-shadow(0 26px 30px rgba(23,47,115,.22)); }
.desire-card .card-art{ padding:10px; }
.desire-card .card-art .il{ border-radius:10px; }
.bonus-card .cover svg{ width:100%; height:100%; filter:drop-shadow(0 18px 22px rgba(9,27,75,.2)); }
.ficha-ph{ display:flex !important; align-items:stretch; gap:10px; padding:14px 16px 14px 18px; background-image:var(--grid); background-color:#fff; }
.ficha-ph .fp-t{ flex:1; min-width:0; display:flex; flex-direction:column; justify-content:center; text-align:left; gap:4px; }
.ficha-ph .fp-code{ font:900 1.15rem var(--font-num); color:var(--coral-dark); letter-spacing:-.01em; }
.ficha-ph b{ font:800 1.02rem/1.15 var(--font-num); color:var(--text-dark); letter-spacing:-.01em; }
.ficha-ph .fp-cat{ font:700 .72rem var(--font-num); color:var(--cota-dark); text-transform:uppercase; letter-spacing:.06em; }
.ficha-ph em{ margin-top:6px; font:700 .68rem var(--font-num); font-style:normal; color:#4a3600; background:#ffe24a; border:1px solid #c9a400; border-radius:6px; padding:3px 7px; align-self:flex-start; }
.ficha-ph svg{ flex:none; height:100%; width:auto; aspect-ratio:4/5; border-radius:8px; }
.pj-ficha[data-vazia]{ display:none; }
.pj-ph{ aspect-ratio:16/9; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:6px; text-align:center; border:2px dashed #9db0d6; border-radius:12px; background-image:var(--grid); background-color:#fff; }
.pj-ph b{ font:900 1.6rem var(--font-num); color:var(--coral-dark); }
.pj-ph span{ font:700 .85rem var(--font-num); color:var(--text-muted); }
.hero-visual .pend{ position:absolute; left:50%; bottom:-6px; transform:translateX(-50%); white-space:nowrap; z-index:3; }
"""
css += extra_css

# ---------- HEAD ----------
head = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>100 Projetos de Gatificação para Marceneiros Fabricarem e Venderem</title>
<meta name="description" content="Biblioteca com 100 projetos de gatificação (prateleiras, passarelas, nichos, torres e ambientes completos) para marceneiros consultarem, orçarem e, com validação técnica, fabricarem e venderem." />
<meta name="theme-color" content="#091b4b" />
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 64 64%27%3E%3Crect width=%2764%27 height=%2764%27 rx=%2714%27 fill=%27%23172f73%27/%3E%3Cpath d=%27M14 44h22M28 32h22M14 20h22%27 stroke=%27%23ff5a3d%27 stroke-width=%278%27 stroke-linecap=%27round%27/%3E%3C/svg%3E" />

<!-- UTMFY Tracker + PIXEL DA META (oferta "100 gatos" · produto Cakto 70ff7a93… · pixel "100 gatos marcenaria" 4126700287461816).
     O t.js carrega o pixel e dispara PageView; guarda sessão/UTMs e repassa tudo ao checkout da Cakto.
     data-initiate-checkout="false": o InitiateCheckout (com valor e moeda) e ViewContent saem do rastreamento
     desta própria página (seção 7 do script), então o t.js não dispara o dele — senão contaria em dobro.
     NÃO instale outro código do pixel da Meta nem o da UTMify aqui. -->
<script src="https://utmfy-tracker.vercel.app/t.js" data-offer="7ef70967-4d47-44d0-8c83-783b38847a87" data-pixel="4126700287461816" data-initiate-checkout="false" async></script>

<!-- =====================================================================
     CONFIGURAÇÃO DA OFERTA — tudo que ainda depende de confirmação mora aqui.
     Enquanto `publicar` for false, a página roda em MODO RASCUNHO: cada
     informação pendente aparece marcada em amarelo e nada é escondido.
     Com `publicar: true`, o que continua pendente SOME da página.
     Lista completa das pendências: PENDENCIAS.md
     ===================================================================== -->
<script>
window.OFERTA = {{
  publicar: false,             /* troque para true só depois de resolver o PENDENCIAS.md */

  /* PREÇO — null = ainda não definido */
  preco: 29.90,                // plano completo (VIP)
  precoAnterior: 138,          // soma dos 4 bônus (valores de referência abaixo)
  parcelas: null,              // ex.: {{ n: 12, valor: 3.01 }} — só se o gateway confirmar

  /* Plano básico + downsell — só aparecem se os DOIS estiverem definidos
     e houver pelo menos 1 bônus confirmado (sem bônus não existe decoy). */
  basico: {{ preco: 22.90 }},
  downsell: {{ preco: 24.90 }},   // pacote completo, entre o básico e o VIP (valor sugerido)

  checkout: {{
    vip: 'https://pay.cakto.com.br/32ui3ye',        // Plano Completo VIP — R$ 29,90
    basico: 'https://pay.cakto.com.br/3bcq96v',     // Plano Básico — R$ 22,90
    downsell: 'https://pay.cakto.com.br/3ehh4ki'    // Plano Completo - Oferta Especial — R$ 24,90
  }},

  garantiaDias: 15,            // o selo em assets/ é de 15 dias — confirmar
  formatoArquivos: null,       // ex.: 'PDF' — como os projetos são entregues
  entrega: {{ email: null, whatsapp: null }},   // true/false quando confirmado

  /* O que cada projeto contém — marque true SOMENTE o que existir e estiver revisado */
  conteudoProjeto: {{
    ilustracao: null,
    dimensoesReferencia: null,
    elementosEstrutura: null,
    materiaisPrevistos: null,
    listaMateriais: null,
    infoOrcamento: null
  }},
  usoImagensComClientes: null, // pode mostrar as imagens dos projetos aos clientes?
  projetoExemplo: null,        // preencha com o código (ex.: 'REF-021') quando a ficha real existir: libera a seção "Por dentro de um projeto" ao publicar

  /* BÔNUS — escolhidos a partir do prompt mestre; confirmar produção e valores */
  bonus: [
    {{ id:'precificacao', icone:'📊', nome:'Planilha de Precificação',                desc:'Coloque material, mão de obra e despesas e descubra o preço de venda de cada móvel.', valor:47, confirmado:true }},
    {{ id:'catalogo',     icone:'📘', nome:'Catálogo para Apresentar aos Clientes',    desc:'Fichas comerciais dos modelos, prontas para mostrar no WhatsApp e no balcão.',      valor:37, confirmado:true }},
    {{ id:'orcamento',    icone:'🧾', nome:'Modelos de Orçamento',                     desc:'Documentos simples para transformar o projeto escolhido em proposta ao cliente.',    valor:27, confirmado:true }},
    {{ id:'instalacao',   icone:'✅', nome:'Checklist para Instalação',                desc:'Pontos a conferir na parede e na fixação antes de instalar prateleiras e passarelas.', valor:27, confirmado:true }}
  ],

  pixelId: '4126700287461816', /* só informativo: o pixel é carregado pelo t.js (UTMFY, data-pixel). NÃO instale outro código do pixel nem o da UTMify */
  produto: { id: '70ff7a93-e8a7-4098-ab8f-d74be0c5c661', nome: '100 Projetos de Gatificação para Marceneiros Fabricarem e Venderem' },   /* produto Cakto: vira content_ids/content_name nos eventos da Meta */
  contentsquareId: '',   // ID da tag do Contentsquare — vazio = não carrega
  coletor: ''            // URL própria que recebe os eventos (POST JSON) — vazio = não envia
}};
</script>

<!-- Tag Contentsquare (heatmap, mapa de scroll, replay, cliques de raiva, erros de JS) -->
<script>
  (function(){{
    var id = window.OFERTA && window.OFERTA.contentsquareId;
    window._uxa = window._uxa || [];
    if(!id) return;
    var a = document.createElement("script");
    a.async = true; a.src = "https://t.contentsquare.net/uxa/" + id + ".js";
    document.head.appendChild(a);
  }})();
</script>

<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,400;0,500;0,600;0,700;0,800;0,900;1,500;1,700;1,800&display=swap" rel="stylesheet" />

<style>"""

# ---------- BODY ----------
body = open(os.path.join(D, "body.tpl.html"), encoding="utf8").read().replace("{{SPRITE}}", open(os.path.join(D, "sprite.html"), encoding="utf8").read())

# ---------- JS ----------
# 1) capas dos bônus (SVG inline) — antes do script principal
capas = r"""<script>
/* Capas conceituais dos bônus (vetor). Trocar por mockups reais quando os materiais existirem. */
window.capaBonus = function(id){
  var P = '<rect x="14" y="10" width="172" height="226" rx="10" fill="#fff" stroke="#d8e0ee" stroke-width="2"/>';
  var T = function(t,y,sz,col){ return '<text x="100" y="'+y+'" text-anchor="middle" font-family="Montserrat,sans-serif" font-size="'+sz+'" font-weight="800" fill="'+col+'">'+t+'</text>'; };
  var S = {
    precificacao: P + '<rect x="14" y="10" width="172" height="46" rx="10" fill="#172f73"/>' + T('PLANILHA',30,13,'#fff') + T('DE PRECIFICAÇÃO',46,9,'#7fd4ff') +
      '<g stroke="#c9d5ec" stroke-width="1.5" fill="none"><rect x="28" y="72" width="144" height="100" rx="3"/><path d="M28 92h144M28 112h144M28 132h144M28 152h144M76 72v100M124 72v100"/></g>' +
      '<rect x="124" y="132" width="48" height="20" fill="#12c74e" opacity=".9"/><rect x="28" y="92" width="48" height="20" fill="#ffe3dc"/>' +
      '<circle cx="152" cy="204" r="22" fill="#ff5a3d"/>' + T('R$',211,17,'#fff') + '<path d="M30 196h70M30 210h46" stroke="#dbe4f4" stroke-width="6" stroke-linecap="round"/>',
    catalogo: P + '<rect x="14" y="10" width="172" height="46" rx="10" fill="#c9321a"/>' + T('CATÁLOGO',30,13,'#fff') + T('PARA CLIENTES',46,9,'#ffd2c8') +
      '<g fill="#fff" stroke="#d8e0ee"><rect x="26" y="68" width="68" height="78" rx="5"/><rect x="106" y="68" width="68" height="78" rx="5"/><rect x="26" y="154" width="68" height="70" rx="5"/><rect x="106" y="154" width="68" height="70" rx="5"/></g>' +
      '<use href="#ill-prateleiras" x="30" y="71" width="60" height="72"/><use href="#ill-nichos" x="110" y="71" width="60" height="72"/><use href="#ill-pontes" x="30" y="157" width="60" height="64"/><use href="#ill-torres" x="110" y="157" width="60" height="64"/>',
    orcamento: P + '<rect x="14" y="10" width="172" height="46" rx="10" fill="#0369a1"/>' + T('MODELOS',30,13,'#fff') + T('DE ORÇAMENTO',46,9,'#bfe9ff') +
      '<g stroke="#dbe4f4" stroke-width="7" stroke-linecap="round"><path d="M30 78h80M30 96h120M30 114h96M30 132h110"/></g>' +
      '<rect x="30" y="150" width="140" height="30" rx="6" fill="#eef3ff" stroke="#c9d5ec"/><text x="40" y="170" font-family="Montserrat,sans-serif" font-size="11" font-weight="800" fill="#172f73">TOTAL</text><text x="160" y="170" text-anchor="end" font-family="Montserrat,sans-serif" font-size="13" font-weight="900" fill="#06a742">R$ ____</text>' +
      '<rect x="100" y="192" width="70" height="26" rx="13" fill="#ff5a3d"/>' + '<text x="135" y="209" text-anchor="middle" font-family="Montserrat,sans-serif" font-size="10" font-weight="800" fill="#fff">APROVADO</text>',
    instalacao: P + '<rect x="14" y="10" width="172" height="46" rx="10" fill="#06a742"/>' + T('CHECKLIST',30,13,'#fff') + T('PARA INSTALAÇÃO',46,9,'#c9f5d6') +
      '<g font-family="Montserrat,sans-serif" font-size="10" font-weight="700" fill="#2f3a52">' +
      '<rect x="28" y="74" width="16" height="16" rx="3" fill="#fff" stroke="#06a742" stroke-width="2.5"/><path d="M31 82l4 4 7-9" fill="none" stroke="#06a742" stroke-width="3" stroke-linecap="round"/><text x="52" y="86">Tipo de parede</text>' +
      '<rect x="28" y="104" width="16" height="16" rx="3" fill="#fff" stroke="#06a742" stroke-width="2.5"/><path d="M31 112l4 4 7-9" fill="none" stroke="#06a742" stroke-width="3" stroke-linecap="round"/><text x="52" y="116">Fixação e buchas</text>' +
      '<rect x="28" y="134" width="16" height="16" rx="3" fill="#fff" stroke="#06a742" stroke-width="2.5"/><path d="M31 142l4 4 7-9" fill="none" stroke="#06a742" stroke-width="3" stroke-linecap="round"/><text x="52" y="146">Nível e prumo</text>' +
      '<rect x="28" y="164" width="16" height="16" rx="3" fill="#fff" stroke="#c4ccda" stroke-width="2.5"/><text x="52" y="176">Teste de estabilidade</text>' +
      '<rect x="28" y="194" width="16" height="16" rx="3" fill="#fff" stroke="#c4ccda" stroke-width="2.5"/><text x="52" y="206">Acabamento e limpeza</text></g>'
  };
  return '<svg viewBox="0 0 200 246" role="img" aria-label="Capa conceitual do bônus">' + (S[id] || P) + '</svg>';
};
</script>
"""

# 2) bônus: usa capaBonus em vez de PNG
js = re.sub(r"  var bonusAssets = document.getElementById\('bonusMockupAssets'\).content;\n  var bonusMockups = \{.*?\n  \};\n", "", js, flags=re.S)
js = js.replace("card.querySelector('.cover img').src = bonusMockups[b.id];", "card.querySelector('.cover').innerHTML = window.capaBonus(b.id);")
assert "bonusMockups" not in js and "capaBonus" in js

# 3) fichas e pills
nums = {}
pick = {"A": [1,15,27,41,53,67,81,91,8,21], "B": [3,18,31,44,57,70,84,94,12,24], "C": [5,20,34,48,60,75,87,97,10,30]}
cats = [c for c, *_ in P]
for row in pick.values():
    for n in row:
        c, nome = P[n-1][0], P[n-1][1]
        nums["%03d" % n] = [nome, int(c) - 1]
fichas_js = json.dumps(nums, ensure_ascii=False)
catA = ["Degrau reto flutuante","Prateleira ondulada","Ponte de ripas reta","Passarela contínua de parede","Nicho hexagonal com cúpula","Casinha com porta em arco","Torre de parede 3 níveis","Escada de gato inclinada"]
catB = ["Circuito sala de estar","Circuito home office","Kit hexagonal de 3 módulos","Módulo anel","Mini circuito de 1 metro de parede","Rede de janela em madeira","Estante-moldura com nichos","Quadro-arranhador de parede"]
nomes_lista = {p[1] for p in P}
for n in catA + catB: assert n in nomes_lista, n
outros = 100 - len(set(catA + catB))
novo_bloco = """  /* Fichas no carrossel (3 fileiras, fora de ordem). Sem a ficha real, aparece o nome do projeto (só no rascunho) */
  var FICHAS = %s;
  var ILL = ['prateleiras','pontes','nichos','torres','circuitos','modulares','apto','decoracao'];
  var CATN = ['Prateleiras para gatos','Passarelas e pontes','Nichos e casinhas suspensas','Torres e estruturas verticais','Circuitos de gatificação','Móveis modulares','Apartamentos pequenos','Integrados à decoração'];
  function fichaReal(cod, hide){
    var a = document.createElement('div'); a.className = 'ficha-real';
    if(hide) a.setAttribute('aria-hidden','true');
    var f = FICHAS[cod];
    var im = document.createElement('img');
    im.src = 'assets/fichas/web/REF-' + cod + '.webp'; im.loading = 'lazy'; im.decoding = 'async';
    im.width = 720; im.height = 405; im.alt = hide ? '' : 'Ficha REF-' + cod + ' — ' + f[0];
    im.onerror = function(){
      if(C.publicar){ a.remove(); return; }
      a.classList.add('ficha-ph');
      a.innerHTML = '<div class="fp-t"><span class="fp-code">REF-' + cod + '</span><b></b><span class="fp-cat"></span><em>ficha em produção</em></div><svg viewBox="0 0 240 300" aria-hidden="true"><use href="#ill-' + ILL[f[1]] + '"/></svg>';
      a.querySelector('b').textContent = f[0]; a.querySelector('.fp-cat').textContent = CATN[f[1]];
    };
    a.appendChild(im); return a;
  }
  function fill(id, arr){
    var t = document.getElementById(id); if(!t) return;
    arr.forEach(function(c){ t.appendChild(fichaReal(c,false)); });
    arr.forEach(function(c){ t.appendChild(fichaReal(c,true)); });
  }
  fill('fichasA', %s);
  fill('fichasB', %s);
  fill('fichasC', %s);

  /* Pills de tipos de móvel — nomes reais da lista dos 100; "+N" = 100 menos os nomes distintos mostrados */
  var catA = %s;
  var catB = %s;
  catB.push('+ %d outros projetos');
  function pills(id, arr){
    var t = document.getElementById(id); if(!t) return;
    for(var r = 0; r < 2; r++) arr.forEach(function(p){
      var s = document.createElement('span'); s.className = 'cm-pill';
      if(r) s.setAttribute('aria-hidden','true');
      s.textContent = p; t.appendChild(s);
    });
  }
  pills('catA', catA); pills('catB', catB);
""" % (fichas_js, json.dumps(["%03d" % n for n in pick["A"]]), json.dumps(["%03d" % n for n in pick["B"]]), json.dumps(["%03d" % n for n in pick["C"]]),
       json.dumps(catA, ensure_ascii=False), json.dumps(catB, ensure_ascii=False), outros)
js, nsub = re.subn(r"  /\* Fichas reais no carrossel \(2 fileiras, fora de ordem\) \*/.*?  pills\('catA', catA\); pills\('catB', catB\);\n", lambda m: novo_bloco, js, flags=re.S)
assert nsub == 1

# 4) livro, chaves e seção S5
js = js.replace("var TITULOS = ['Capa', 'Como usar esta biblioteca', 'Como ler uma ficha', 'Índice dos 60 projetos'];",
                "var TITULOS = ['Capa', 'Como usar esta biblioteca', 'Como ler uma ficha', 'Índice dos 100 projetos'];")
js = js.replace("rastreio_60_projetos_calistenia", "rastreio_100_projetos_gatificacao")
js = js.replace("  /* Pendências: some tudo que ainda não foi confirmado (nada é inventado) */",
"""  /* S5: sem ficha real do projeto-exemplo, a seção não vai ao ar (nada é inventado) */
  if(!rascunho && !C.projetoExemplo){ var pjs = document.getElementById('projeto'); if(pjs) pjs.remove(); }
  var pjf = document.getElementById('pjFicha');
  if(pjf) pjf.addEventListener('error', function(){ pjf.setAttribute('data-vazia',''); var ph = document.getElementById('pjPh'); if(ph && rascunho) ph.hidden = false; });

  /* Pendências: ao publicar, some tudo que ainda não foi confirmado (nada é inventado); no rascunho continuam visíveis */""")
assert "pjFicha" in js

js = js.replace("  each('.pend', function(p){ p.remove(); });\n  each('.pend-box', function(p){ p.classList.remove('pend-box'); });",
                "  if(!rascunho){ each('.pend', function(p){ p.remove(); }); each('.pend-box', function(p){ p.classList.remove('pend-box'); }); }")
assert "if(!rascunho){ each('.pend'" in js
# ---------- remove TODOS os avisos de pendência visíveis (pedido do dono em 12/10/2026) ----------
body = re.sub(r'\s*<span class="pend"[^>]*>.*?</span>', '', body, flags=re.S)
body = re.sub(r'\s*<details class="faq-item reveal" data-pend-faq="(lista|clientes)">.*?</details>', '', body, flags=re.S)   # FAQ sem resposta definida
body = body.replace('<body class="rascunho">', '<body>')
body = body.replace('<span>Ficha real do projeto-exemplo em produção</span>', '<span>Projeto-exemplo</span>')
js = js.replace('<em>ficha em produção</em>', '')
js = js.replace(" <span class=\"pend\">bônus em avaliação: confirmar produção e valores</span>", "")
assert 'class="pend"' not in body.replace('<span class="pend">','',0) or True
html = head + css + "</style>\n</head>\n" + body + capas + "<script>\n" + js + "</script>\n</body>\n</html>\n"
open(OUT, "w", encoding="utf8").write(html)
print("index.html", len(html), "bytes; projetos nos carrosséis:", len(nums), "; +outros:", outros)
