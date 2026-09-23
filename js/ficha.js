/**
 * Ficha extendida de producto (paginas/ficha.html?asin=XXXX).
 * Página única reutilizada para los 110 productos del catálogo: lee el
 * ASIN de la URL, busca el producto en PRODUCTS (products.js) y pinta
 * galería de imágenes, descripción extendida, atributos y acciones
 * (añadir al carrito / ver en Amazon / volver al catálogo).
 */
(function () {
  const contenidoEl = document.getElementById("ficha-contenido");
  const migasEl = document.getElementById("ficha-migas");
  const footerCatEl = document.getElementById("footer-categorias");
  const tituloTabEl = document.getElementById("ficha-titulo-tab");
  const metaDescEl = document.getElementById("ficha-meta-desc");

  if (footerCatEl && typeof CATEGORIES !== "undefined") {
    footerCatEl.innerHTML = CATEGORIES.map(
      (c) => `<li><a href="paginas/${c.id}.html">${c.nombre}</a></li>`
    ).join("");
  }

  function getAsin() {
    const params = new URLSearchParams(window.location.search);
    return params.get("asin") || params.get("id") || "";
  }

  function renderNoEncontrado() {
    contenidoEl.innerHTML = `
      <div style="text-align:center; padding:50px 0;">
        <h1 style="font-size:22px;">Producto no encontrado</h1>
        <p style="color:var(--texto-suave); max-width:480px; margin:12px auto 24px;">
          No hemos podido encontrar la ficha de este producto. Puede que el enlace sea incorrecto o que el producto ya no esté disponible.
        </p>
        <a href="index.html#catalogo" class="btn">← Volver al catálogo</a>
      </div>`;
  }

  function renderFicha(p) {
    const cat = CATEGORIES.find((c) => c.id === p.categoria);
    const catHref = `paginas/${p.categoria}.html`;
    const atributos = p.atributos && typeof p.atributos === "object" ? p.atributos : {};
    const atributoEntradas = Object.entries(atributos);

    document.title = `${p.titulo} — PrepForCaos`;
    if (tituloTabEl) tituloTabEl.textContent = `${p.titulo} — PrepForCaos`;
    if (metaDescEl) {
      metaDescEl.setAttribute(
        "content",
        (p.descripcion || p.titulo).slice(0, 155)
      );
    }

    if (migasEl) {
      migasEl.innerHTML = `
        <a href="index.html">Inicio</a> /
        <a href="${catHref}">${cat ? cat.icono + " " + cat.nombre : "Catálogo"}</a> /
        <span>${p.titulo}</span>`;
    }

    const atributosHtml = atributoEntradas.length
      ? `
      <div class="ficha-atributos">
        <h2>Características</h2>
        <dl>
          ${atributoEntradas
            .map(([clave, valor]) => `<dt>${clave}</dt><dd>${valor}</dd>`)
            .join("")}
        </dl>
      </div>`
      : "";

    contenidoEl.innerHTML = `
      <div class="ficha-grid">
        <div class="ficha-galeria">
          <div class="ficha-imagen-principal tarjeta-ilustracion cat-${p.categoria}" aria-hidden="true">
            <span>${cat ? cat.icono : "📦"}</span>
          </div>
        </div>
        <div class="ficha-info">
          <span class="tarjeta-cat">${cat ? cat.icono + " " + cat.nombre : ""}</span>
          <h1 class="ficha-titulo">${p.titulo}</h1>
          <p class="ficha-precio-nota">Consulta el precio y la disponibilidad actualizados en Amazon.es.</p>
          <p class="ficha-descripcion">${p.descripcion || ""}</p>
          ${atributosHtml}
          <div class="ficha-acciones">
            <button type="button" class="add-carrito-btn" data-asin="${p.asin}">+ Añadir al carrito</button>
            <a class="tarjeta-btn" href="${amazonLink(p.asin)}" target="_blank" rel="nofollow sponsored noopener">Ver precio en Amazon →</a>
            <a class="btn btn-outline-oscuro" href="index.html#catalogo">← Volver al catálogo</a>
          </div>
        </div>
      </div>`;

  }

  const asin = getAsin();
  const producto = typeof PRODUCTS !== "undefined" ? PRODUCTS.find((p) => p.asin === asin) : null;

  if (producto) {
    renderFicha(producto);
  } else {
    renderNoEncontrado();
  }
})();
