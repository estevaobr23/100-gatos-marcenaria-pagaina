# Pendências — 100 Projetos de Gatificação para Marceneiros Fabricarem e Venderem

Atualizado em 12/10/2026. A página está em **modo rascunho** (`OFERTA.publicar: false`, `<body class="rascunho">`):
cada pendência aparece em amarelo. Quando tudo abaixo estiver resolvido, troque para `publicar: true` e retire
`class="rascunho"` do `<body>` — a partir daí o que continua pendente **some** da página (nada é inventado).

## 1. Oferta, checkout e rastreio (atualizado em 12/10/2026)
- [x] Preços: Completo **R$ 29,90** · Básico **R$ 22,90** · Downsell **R$ 24,90** (o downsell foi sugestão minha; o dono não objetou)
- [x] **Produto criado na Cakto**: `70ff7a93-e8a7-4098-ab8f-d74be0c5c661` — "100 Projetos de Gatificação para Marceneiros Fabricarem e Venderem" (R$ 29,90, garantia 15 dias, produtor "100 Projetos de Gatificação")
- [x] **3 ofertas no mesmo produto**, já com checkout renderizado e conferido (título + preço):
      Plano Completo VIP `32ui3ye` (R$ 29,90) · Plano Básico `3bcq96v` (R$ 22,90) · Plano Completo - Oferta Especial `3ehh4ki` (R$ 24,90)
- [x] Links em `OFERTA.checkout`, com repasse de UTM (testado: `utm_*` + `callback` chegam nos 3 links)
- [x] Webhook **Recuperação WhatsApp (71145)**: produto adicionado à lista (8 → 9 produtos, nenhum removido)
- [x] Webhook **Rastreio UTMFY #73792** criado e vinculado à oferta UTMFY `100 gatos` (slug `100-gatos-marcenaria`, que já existia vazia e ativa — reaproveitada em vez de duplicar)
- [x] `t.js` do UTMFY instalado no `<head>` (`data-offer` + `data-pixel` + `data-initiate-checkout="false"`)
- [x] **Pixel da Meta exclusivo desta oferta** (13/10/2026): pixel `4126700287461816` ("100 gatos marcenaria", já existia na Meta) **vinculado à oferta UTMFY** e instalado no `t.js` (`data-pixel`). O `t.js` dispara PageView; a página dispara ViewContent e InitiateCheckout (com valor, moeda e produto) e todos os demais eventos de comportamento como eventos personalizados (fila até o pixel carregar; telemetria técnica `erro_js`/`erro_recurso`/`performance` fica de fora). `data-initiate-checkout="false"` evita IC em dobro.
- [ ] **Pixel no checkout da Cakto** (a API não grava — só pelo painel): Produto → Pixels → Facebook → ID `4126700287461816` + token da API de Conversões deste pixel (já existe um salvo no UTMFY, final …ZDZD, mas ele não é legível; gere/copie no Gerenciador de Eventos). É o que manda o **Purchase** para a Meta. Depois, no Meta Pixel Helper, veja se o checkout também dispara InitiateCheckout: se sim, desligue o do site removendo `checkout_clique` do mapa `STD` no script da seção 7 (o clique continua indo como evento personalizado).
- [ ] **No painel da Cakto** (a API não grava): imagem do produto (1000×1000 JPEG) · **PIX como método padrão** · **entrega de conteúdo** (marcar "Acesso por e-mail" ou "Link de pagamento")
- [ ] **Hospedar a página** e trocar a `salesPage` do produto (hoje provisória: `https://100-projetos-gatificacao.vercel.app/`)
- [ ] Webhook de **acesso (área de membros)**: este produto ainda não tem área de membros; criar junto com ela (skill `area-de-membros`)
- [ ] Aparência do checkout casando com a página (opcional, ver `references/checkout-visual.md` da skill criar-produto-cakto)
- [ ] `parcelas` — o checkout da Cakto já oferece até 6x no cartão; a página diz "Pagamento único". Decidir se mostra o parcelamento.
- [ ] Nome do produtor, CPF/CNPJ e e-mail de suporte no rodapé da página.
- [ ] 1ª venda real (ou `node ~/.utmfy/utmfy.mjs simular --confirmar`) para provar o webhook de rastreio.

## 2. Valores e escolhas que EU assumi (o dono precisa confirmar)
- [x] **Os 4 bônus** foram definidos pelo dono em 13/10/2026: Catálogo Pet Premium · Pack Divulgação Pet (30 artes) · Gatificação Compacta (15 soluções) · Kit Orçamento Profissional.
- [ ] **Valores riscados dos bônus** (R$ 37 / 47 / 27 / 27 = **R$ 138**, que vira o "De R$ 138" do plano completo) — valores de referência meus (reaproveitei os anteriores), **não vêm de mercado**. As descrições curtas dos cards só repetem o que o nome já diz.
- [ ] Os 4 bônus precisam ser **produzidos** (e ganhar capa real no lugar da ilustração).
- [ ] **Garantia de 15 dias** (`garantiaDias: 15`, porque o selo da skill é de 15 dias).
- [ ] **Entrega por WhatsApp e e-mail** (`entrega` está `null`; o hero mostra os dois canais até confirmar).

## 3. Produto (o que realmente existe)
- [ ] **A lista dos 100 projetos é uma proposta minha** (`../lista-100-projetos.md`) — revisar, cortar e trocar. O livro (página 4, índice) e os carrosséis usam os nomes e faixas dela (001–014 prateleiras · 015–026 pontes · 027–040 nichos · 041–052 torres · 053–066 circuitos · 067–080 modulares · 081–090 apartamento pequeno · 091–100 decoração). Se a lista mudar, refazer `_fonte/paginas.tpl.html` e `_fonte/data_proj.py`.
- [ ] **O que cada ficha traz de fato** (`conteudoProjeto`): a página 3 do livro e a seção "Por dentro de um projeto" falam em móvel pronto, vistas, peças, montagem, material e instalação. Confirmar que as fichas finais trazem exatamente isso — **nenhuma medida, carga ou lista de cortes pode vir de imagem de IA**; só de desenho dimensionado e conferido.
- [ ] `formatoArquivos` — PDF? área de membros?
- [ ] `usoImagensComClientes` — o marceneiro pode mostrar as imagens aos clientes? (a FAQ correspondente fica escondida até definir)
- [ ] Lista de cortes: os projetos terão? (a FAQ "Os projetos incluem lista de cortes?" fica escondida até definir)
- [ ] Revisão técnica (parede, fixação, carga) antes de qualquer número estrutural aparecer.

## 4. Imagens a produzir (hoje há ilustrações vetoriais conceituais no lugar)
- [ ] **Mockup do pacote** (3:2, fundo transparente): hero, vitrine, card VIP e modal. Hoje é um SVG conceitual (`#mock-pacote`).
- [ ] **8 imagens das categorias** (4:5, fundo branco): hoje são SVGs conceituais (`#ill-*`). A skill prevê 6 cards; como a oferta tem **8 categorias**, usei 8 (grade 4×2). Se preferir 6, agrupo.
- [ ] **Fichas reais**: 30 no carrossel (`public/assets/fichas/web/REF-NNN.webp`, 16:9, códigos em `FICHAS` no script) + a do exemplo (`REF-021-g.webp`, 1400×788). Enquanto não existirem, o rascunho mostra o nome do projeto e "ficha em produção"; ao publicar, esses cartões somem.
- [ ] **Página 3 do livro ("Como ler uma ficha")** é um **esquema** do formato. Trocar por uma ficha real quando existir (refazer `_fonte/paginas.tpl.html` → `python _fonte/renderizar_paginas.py`).
- [ ] **Capas dos 4 bônus**: hoje SVG conceitual (função `capaBonus` no fim do `index.html`).
- [ ] Rostos/depoimentos: **não há** cliente real — hero usa `hero-apoio`, sem S6b.

## 5. Seção "Por dentro de um projeto" (S5)
- [x] Preenchida em 14/10/2026 com o projeto real **REF-031 — Nicho hexagonal com cúpula** (`OFERTA.projetoExemplo = 'REF-031'`, ficha em `public/assets/fichas/web/REF-031.webp`). Escolhido porque é o único dos testados cujas 3 medidas (largura 520 × profundidade 470 × altura 450 mm) vêm declaradas por uma fonte real (RK032); a cúpula (Ø 350 mm) e as peças internas são sugestões — a nota da seção diz isso.
- A ilustração de "Dimensões" é um SVG 3D (hexágono extrudado, cúpula, furos laterais) com as cotas de largura, altura, profundidade e Ø da cúpula, desenhado a partir dessas medidas.
- [ ] Os números de nível/tempo/pessoas ("Avançado · 5 a 7 h · 1 pessoa") vêm da ficha gerada — confirmar quando a ficha final for revisada. "Gatos por vez" saiu (a ficha não traz).

## 6. Como regenerar / rodar
- `npm install` · `npm run dev` (ou `npm run build` e `npm run preview`).
- `index.html` é gerado por `python _fonte/gerar_index.py` a partir da estrutura da página 60 Equipamentos; **depois de gerado, pode editar o `index.html` direto**. Rodar o gerador de novo sobrescreve edições manuais.
- Páginas do livro: `python _fonte/renderizar_paginas.py` (usa o Chrome headless).
