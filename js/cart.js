/**
 * Carrito propio de PrepForCaos.
 * Guarda selección en localStorage (por visitante) y, al finalizar,
 * construye una URL de Amazon que añade todos los productos al carrito
 * REAL del usuario en Amazon.es, manteniendo el tag de afiliado:
 *   https://www.amazon.es/gp/aws/cart/add.html?AssociateTag=...&ASIN.1=...&Quantity.1=...
 * Depende de PRODUCTS y AFFILIATE_TAG (definidos en products.js), que debe
 * cargarse ANTES que este script en cada página.
 */
(function () {
  const CART_KEY = "prepforcaos_carrito";
  const MAX_ITEMS_CARRITO = 24; // límite prudente para no pasarnos de la longitud de URL que acepta Amazon

  function leerCarrito() {
    try {
      const raw = localStorage.getItem(CART_KEY);
      return raw ? JSON.parse(raw) : {};
    } catch (e) {
      return {};
    }
  }

  function guardarCarrito() {
    try {
      localStorage.setItem(CART_KEY, JSON.stringify(carrito));
    } catch (e) {
      /* si el navegador bloquea el almacenamiento, el carrito solo dura la visita actual */
    }
  }

  let carrito = leerCarrito(); // { asin: cantidad }

  function totalUnidades() {
    return Object.values(carrito).reduce((s, q) => s + q, 0);
  }

  function producto(asin) {
    return typeof PRODUCTS !== "undefined" ? PRODUCTS.find((p) => p.asin === asin) : null;
  }

  function amazonCartUrl() {
    const entradas = Object.entries(carrito).slice(0, MAX_ITEMS_CARRITO);
    const params = new URLSearchParams();
    params.set("AssociateTag", typeof AFFILIATE_TAG !== "undefined" ? AFFILIATE_TAG : "");
    entradas.forEach(([asin, cantidad], i) => {
      params.set(`ASIN.${i + 1}`, asin);
      params.set(`Quantity.${i + 1}`, String(cantidad));
    });
    return `https://www.amazon.es/gp/aws/cart/add.html?${params.toString()}`;
  }

  function icono(categoria) {
    const c = typeof CATEGORIES !== "undefined" ? CATEGORIES.find((x) => x.id === categoria) : null;
    return c ? c.icono : "📦";
  }

  function actualizarBadge() {
    document.querySelectorAll(".carrito-badge").forEach((el) => {
      const n = totalUnidades();
      el.textContent = String(n);
      el.hidden = n === 0;
    });
  }

  function renderPanel() {
    const listaEl = document.getElementById("carrito-lista");
    const totalEl = document.getElementById("carrito-total");
    const checkoutBtn = document.getElementById("carrito-checkout");
    const vacioEl = document.getElementById("carrito-vacio");
    if (!listaEl) return;

    const asins = Object.keys(carrito);

    if (asins.length === 0) {
      listaEl.innerHTML = "";
      if (vacioEl) vacioEl.hidden = false;
      if (checkoutBtn) checkoutBtn.setAttribute("aria-disabled", "true");
      if (totalEl) totalEl.textContent = "";
      return;
    }
    if (vacioEl) vacioEl.hidden = true;

    listaEl.innerHTML = asins
      .map((asin) => {
        const p = producto(asin);
        const cantidad = carrito[asin];
        if (!p) return "";
        return `
        <div class="carrito-item" data-asin="${asin}">
          <div class="carrito-item-ilustracion cat-${p.categoria}" aria-hidden="true">${icono(p.categoria)}</div>
          <div class="carrito-item-info">
            <p class="carrito-item-titulo">${p.titulo}</p>
            <div class="carrito-item-qty">
              <button type="button" class="qty-btn" data-accion="restar" data-asin="${asin}" aria-label="Quitar una unidad">−</button>
              <span>${cantidad}</span>
              <button type="button" class="qty-btn" data-accion="sumar" data-asin="${asin}" aria-label="Añadir una unidad">+</button>
              <button type="button" class="carrito-quitar" data-asin="${asin}">Quitar</button>
            </div>
          </div>
        </div>`;
      })
      .join("");

    const totalArticulos = totalUnidades();
    if (totalEl) {
      totalEl.textContent = `${totalArticulos} artículo${totalArticulos === 1 ? "" : "s"} en el carrito`;
    }
    if (checkoutBtn) {
      checkoutBtn.href = amazonCartUrl();
      checkoutBtn.removeAttribute("aria-disabled");
    }
  }

  function añadir(asin, cantidad) {
    carrito[asin] = (carrito[asin] || 0) + cantidad;
    guardarCarrito();
    actualizarBadge();
    renderPanel();
  }

  function cambiarCantidad(asin, delta) {
    if (!carrito[asin]) return;
    carrito[asin] += delta;
    if (carrito[asin] <= 0) delete carrito[asin];
    guardarCarrito();
    actualizarBadge();
    renderPanel();
  }

  function quitar(asin) {
    delete carrito[asin];
    guardarCarrito();
    actualizarBadge();
    renderPanel();
  }

  function vaciar() {
    carrito = {};
    guardarCarrito();
    actualizarBadge();
    renderPanel();
  }

  function abrirPanel() {
    const panel = document.getElementById("carrito-panel");
    const overlay = document.getElementById("carrito-overlay");
    if (panel) panel.classList.add("abierto");
    if (overlay) overlay.classList.add("visible");
    renderPanel();
  }

  function cerrarPanel() {
    const panel = document.getElementById("carrito-panel");
    const overlay = document.getElementById("carrito-overlay");
    if (panel) panel.classList.remove("abierto");
    if (overlay) overlay.classList.remove("visible");
  }

  document.addEventListener("click", (e) => {
    const addBtn = e.target.closest(".add-carrito-btn");
    if (addBtn) {
      e.preventDefault();
      añadir(addBtn.dataset.asin, 1);
      const textoOriginal = addBtn.textContent;
      addBtn.classList.add("añadido");
      addBtn.textContent = "✔ Añadido";
      setTimeout(() => {
        addBtn.textContent = textoOriginal;
        addBtn.classList.remove("añadido");
      }, 1100);
      return;
    }

    if (e.target.closest(".carrito-abrir")) {
      e.preventDefault();
      abrirPanel();
      return;
    }

    if (e.target.closest(".carrito-cerrar") || e.target.id === "carrito-overlay") {
      e.preventDefault();
      cerrarPanel();
      return;
    }

    const qtyBtn = e.target.closest(".qty-btn");
    if (qtyBtn) {
      e.preventDefault();
      cambiarCantidad(qtyBtn.dataset.asin, qtyBtn.dataset.accion === "sumar" ? 1 : -1);
      return;
    }

    const quitarBtn = e.target.closest(".carrito-quitar");
    if (quitarBtn) {
      e.preventDefault();
      quitar(quitarBtn.dataset.asin);
      return;
    }

    if (e.target.closest("#carrito-vaciar")) {
      e.preventDefault();
      vaciar();
      return;
    }
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") cerrarPanel();
  });

  actualizarBadge();
})();
