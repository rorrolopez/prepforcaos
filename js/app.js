(function () {
  const filtrosEl = document.getElementById("filtros");
  const gridEl = document.getElementById("grid-productos");
  const trucoEl = document.getElementById("truco-prepper");
  const buscadorEl = document.getElementById("buscador-input");
  const footerCatEl = document.getElementById("footer-categorias");
  const anioEl = document.getElementById("anio");
  if (anioEl) anioEl.textContent = new Date().getFullYear();

  let categoriaActiva = "todas";
  let textoBusqueda = "";

  function renderFiltros() {
    // Enlaces reales (href a la página de categoría) que además filtran al vuelo con JS,
    // así son crawleables por buscadores y cómodos para quien navega con JS activado.
    const botones = [{ id: "todas", nombre: "Todas", icono: "🗂️" }, ...CATEGORIES];
    filtrosEl.innerHTML = botones
      .map((c) => {
        const href = c.id === "todas" ? "#catalogo" : `paginas/${c.id}.html`;
        return `<a class="filtro-btn${c.id === categoriaActiva ? " activo" : ""}" href="${href}" data-cat="${c.id}">${c.icono} ${c.nombre}</a>`;
      })
      .join("");

    filtrosEl.querySelectorAll(".filtro-btn").forEach((btn) => {
      btn.addEventListener("click", (e) => {
        e.preventDefault();
        categoriaActiva = btn.dataset.cat;
        renderFiltros();
        renderTruco();
        renderGrid();
      });
    });
  }

  function renderFooterCategorias() {
    // Enlaces reales a las páginas de categoría (mejor para SEO que un filtro solo-JS).
    footerCatEl.innerHTML = CATEGORIES.map(
      (c) => `<li><a href="paginas/${c.id}.html">${c.nombre}</a></li>`
    ).join("");
  }

  function renderTruco() {
    if (!trucoEl) return;
    const consejos = TIPS[categoriaActiva];
    const cat = CATEGORIES.find((c) => c.id === categoriaActiva);
    if (!consejos || !cat) {
      trucoEl.innerHTML = "";
      return;
    }
    trucoEl.innerHTML = `
      <div class="truco-caja">
        <h3>${cat.icono} El truco del prepper: ${cat.nombre}</h3>
        <ul>${consejos.map((c) => `<li>${c}</li>`).join("")}</ul>
      </div>`;
  }

  function renderGrid() {
    const texto = textoBusqueda.trim().toLowerCase();
    const filtrados = PRODUCTS.filter((p) => {
      const pasaCategoria = categoriaActiva === "todas" || p.categoria === categoriaActiva;
      const pasaTexto = !texto || p.titulo.toLowerCase().includes(texto);
      return pasaCategoria && pasaTexto;
    });

    if (filtrados.length === 0) {
      gridEl.innerHTML = `<p class="sin-resultados">No hay productos que coincidan con tu búsqueda. Prueba con otro término o categoría.</p>`;
      return;
    }

    gridEl.innerHTML = filtrados
      .map((p) => {
        const cat = CATEGORIES.find((c) => c.id === p.categoria);
        return `
        <article class="tarjeta-producto">
          <a class="tarjeta-enlace-ficha" href="ficha.html?asin=${p.asin}" aria-label="Ver ficha de ${p.titulo}">
            <div class="tarjeta-img tarjeta-foto"><img src="${fotoUrl(p, 400)}" alt="Imagen ilustrativa: ${p.titulo}" loading="lazy"><span class="foto-ilustrativa">Imagen ilustrativa</span></div>
            <div class="tarjeta-cuerpo-superior">
              <span class="tarjeta-cat">${cat ? cat.icono + " " + cat.nombre : ""}</span>
              <h3 class="tarjeta-titulo">${p.titulo}</h3>
            </div>
          </a>
          <div class="tarjeta-cuerpo-inferior">
            <div class="tarjeta-acciones">
              <button type="button" class="add-carrito-btn" data-asin="${p.asin}">+ Carrito</button>
              <a class="tarjeta-btn" href="${amazonLink(p.asin)}" target="_blank" rel="nofollow sponsored noopener">Ver precio en Amazon →</a>
            </div>
          </div>
        </article>`;
      })
      .join("");
  }

  buscadorEl.addEventListener("input", (e) => {
    textoBusqueda = e.target.value;
    renderGrid();
  });

  renderFiltros();
  renderFooterCategorias();
  renderTruco();
  renderGrid();
})();
