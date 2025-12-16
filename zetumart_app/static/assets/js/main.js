/**
* Template Name: UpConstruction
* Template URL: https://bootstrapmade.com/upconstruction-bootstrap-construction-website-template/
* Updated: Aug 07 2024 with Bootstrap v5.3.3
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/

(function() {
  "use strict";

  /**
   * Apply .scrolled class to the body as the page is scrolled down
   */
  function toggleScrolled() {
    const selectBody = document.querySelector('body');
    const selectHeader = document.querySelector('#header');
    if (!selectHeader.classList.contains('scroll-up-sticky') && !selectHeader.classList.contains('sticky-top') && !selectHeader.classList.contains('fixed-top')) return;
    window.scrollY > 100 ? selectBody.classList.add('scrolled') : selectBody.classList.remove('scrolled');
  }

  document.addEventListener('scroll', toggleScrolled);
  window.addEventListener('load', toggleScrolled);

  /**
   * Mobile nav toggle
   */
  const mobileNavToggleBtn = document.querySelector('.mobile-nav-toggle');

  function mobileNavToogle() {
    document.querySelector('body').classList.toggle('mobile-nav-active');
    mobileNavToggleBtn.classList.toggle('bi-list');
    mobileNavToggleBtn.classList.toggle('bi-x');
  }
  mobileNavToggleBtn.addEventListener('click', mobileNavToogle);

  /**
   * Hide mobile nav on same-page/hash links
   */
  document.querySelectorAll('#navmenu a').forEach(navmenu => {
    navmenu.addEventListener('click', () => {
      if (document.querySelector('.mobile-nav-active')) {
        mobileNavToogle();
      }
    });

  });

  /**
   * Toggle mobile nav dropdowns
   */
  document.querySelectorAll('.navmenu .toggle-dropdown').forEach(navmenu => {
    navmenu.addEventListener('click', function(e) {
      e.preventDefault();
      this.parentNode.classList.toggle('active');
      this.parentNode.nextElementSibling.classList.toggle('dropdown-active');
      e.stopImmediatePropagation();
    });
  });

  /**
   * Preloader
   */
  const preloader = document.querySelector('#preloader');
  if (preloader) {
    window.addEventListener('load', () => {
      preloader.remove();
    });
  }

  /**
   * Scroll top button
   */
  let scrollTop = document.querySelector('.scroll-top');

  function toggleScrollTop() {
    if (scrollTop) {
      window.scrollY > 100 ? scrollTop.classList.add('active') : scrollTop.classList.remove('active');
    }
  }
  scrollTop.addEventListener('click', (e) => {
    e.preventDefault();
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });

  window.addEventListener('load', toggleScrollTop);
  document.addEventListener('scroll', toggleScrollTop);

  /**
   * Animation on scroll function and init
   */
  function aosInit() {
    AOS.init({
      duration: 600,
      easing: 'ease-in-out',
      once: true,
      mirror: false
    });
  }
  window.addEventListener('load', aosInit);

  /**
   * Initiate glightbox
   */
  let glightbox = null;
  try {
    glightbox = GLightbox({ selector: '.glightbox' });
  } catch (e) {
    // GLightbox not available yet; continue without breaking the page
  }

  /**
   * Init isotope layout and filters
   */
  try {
    document.querySelectorAll('.isotope-layout').forEach(function(isotopeItem) {
      let layout = isotopeItem.getAttribute('data-layout') ?? 'masonry';
      let filter = isotopeItem.getAttribute('data-default-filter') ?? '*';
      let sort = isotopeItem.getAttribute('data-sort') ?? 'original-order';

      let initIsotope;
      const cont = isotopeItem.querySelector('.isotope-container');
      if (typeof imagesLoaded === 'function' && cont) {
        imagesLoaded(cont, function() {
          if (typeof Isotope === 'function') {
            initIsotope = new Isotope(cont, {
              itemSelector: '.isotope-item',
              layoutMode: layout,
              filter: filter,
              sortBy: sort
            });
          }
        });
      }

      isotopeItem.querySelectorAll('.isotope-filters li').forEach(function(filters) {
        filters.addEventListener('click', function() {
          const active = isotopeItem.querySelector('.isotope-filters .filter-active');
          if (active) active.classList.remove('filter-active');
          this.classList.add('filter-active');
          if (initIsotope && typeof initIsotope.arrange === 'function') {
            initIsotope.arrange({ filter: this.getAttribute('data-filter') });
          }
          if (typeof aosInit === 'function') { aosInit(); }
        }, false);
      });

    });
  } catch (e) {
    // Do not break rendering if Isotope or imagesLoaded are not available
  }

  /**
   * Init swiper sliders
   */
  function initSwiper() {
    document.querySelectorAll(".init-swiper").forEach(function(swiperElement) {
      let config = JSON.parse(
        swiperElement.querySelector(".swiper-config").innerHTML.trim()
      );

      if (swiperElement.classList.contains("swiper-tab")) {
        initSwiperWithCustomPagination(swiperElement, config);
      } else {
        new Swiper(swiperElement, config);
      }
    });
  }

  window.addEventListener("load", initSwiper);

  /**
   * Initiate Pure Counter
   */
  new PureCounter();

})();

// ZetuMart: Simple front-end cart (UI only)
(function() {
  "use strict";

  const CART_KEY = 'zetumart_cart_v1';

  function getUserCartKey() {
    const user = getUser();
    if (user && user.email) {
      return `zetumart_cart_${user.email.replace(/[^a-zA-Z0-9]/g, '_')}`;
    }
    return CART_KEY;
  }

  function readCart() {
    try { return JSON.parse(localStorage.getItem(getUserCartKey()) || '[]'); } catch { return []; }
  }
  function writeCart(items) { localStorage.setItem(getUserCartKey(), JSON.stringify(items)); }

  function parsePriceKSh(text) {
    // Expect formats like "KSh 1,999"
    const digits = (text || '').replace(/[^0-9.]/g, '');
    return Number(digits || 0);
  }

  function updateCartBadge() {
    const badge = document.getElementById('cartBadge');
    if (!badge) return;
    const cart = readCart();
    const qty = cart.reduce((sum, it) => sum + (it.qty || 1), 0);
    badge.textContent = String(qty);
  }

  function renderCart() {
    const list = document.getElementById('cart-items');
    const totalEl = document.getElementById('cart-total');
    if (!list || !totalEl) return;
    const cart = readCart();
    list.innerHTML = '';
    let total = 0;
    cart.forEach((item, idx) => {
      const li = document.createElement('li');
      li.className = 'list-group-item d-flex align-items-center justify-content-between';
      const left = document.createElement('div');
      left.className = 'd-flex align-items-center';
      const img = document.createElement('img');
      img.src = item.img || '';
      img.alt = item.name || '';
      img.style.width = '48px';
      img.style.height = '48px';
      img.className = 'rounded me-2';
      const txt = document.createElement('div');
      txt.innerHTML = `<div class="fw-semibold">${item.name}</div><div class="text-muted small">KSh ${item.price.toLocaleString()} × ${item.qty}</div>`;
      left.appendChild(img);
      left.appendChild(txt);
      const right = document.createElement('div');
      right.className = 'd-flex align-items-center gap-2';
      const minus = document.createElement('button'); minus.className = 'btn btn-outline-secondary btn-sm'; minus.textContent = '-';
      const plus = document.createElement('button'); plus.className = 'btn btn-outline-secondary btn-sm'; plus.textContent = '+';
      const remove = document.createElement('button'); remove.className = 'btn btn-outline-danger btn-sm'; remove.innerHTML = '<i class="bi bi-trash"></i>';
      minus.addEventListener('click', () => { changeQty(idx, -1); });
      plus.addEventListener('click', () => { changeQty(idx, +1); });
      remove.addEventListener('click', () => { removeItem(idx); });
      right.append(minus, plus, remove);
      li.append(left, right);
      list.appendChild(li);
      total += (item.price || 0) * (item.qty || 1);
    });
    totalEl.textContent = 'KSh ' + total.toLocaleString();
    updateCartBadge();
  }

  function changeQty(index, delta) {
    const cart = readCart();
    const item = cart[index];
    if (!item) return;
    item.qty = Math.max(1, (item.qty || 1) + delta);
    writeCart(cart);
    renderCart();
  }

  function removeItem(index) {
    const cart = readCart();
    cart.splice(index, 1);
    writeCart(cart);
    renderCart();
  }

  function addToCartFromCard(cardEl) {
    if (!cardEl) return;
    const name = (cardEl.querySelector('.title')?.textContent || '').trim();
    const priceText = (cardEl.querySelector('.current-price')?.textContent || '').trim();
    const price = parsePriceKSh(priceText);
    const img = cardEl.querySelector('img')?.src || '';
    if (!name || !price) return;
    const cart = readCart();
    const existing = cart.find(it => it.name === name && it.price === price);
    if (existing) existing.qty = (existing.qty || 1) + 1; else cart.push({ name, price, img, qty: 1 });
    writeCart(cart);
    renderCart();
    updateCartBadge(); // Explicitly update cart badge
    // open offcanvas if available
    const offcanvasEl = document.getElementById('cartOffcanvas');
    if (offcanvasEl && window.bootstrap && bootstrap.Offcanvas) {
      const offc = bootstrap.Offcanvas.getOrCreateInstance(offcanvasEl);
      offc.show();
    }
  }

  function initAddToCartButtons() {
    // Re-bind add to cart buttons for dynamically loaded products
    const buttons = document.querySelectorAll('.add-to-cart-btn[data-act="add"]');
    buttons.forEach(btn => {
      // Remove existing listeners to prevent duplicates
      btn.replaceWith(btn.cloneNode(true));
    });
    
    // Re-add event listeners
    document.querySelectorAll('.add-to-cart-btn[data-act="add"]').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        const card = btn.closest('.portfolio-content') || btn.closest('.product-card');
        if (card) {
          addToCartFromCard(card);
        }
      });
    });
  }

  function insertSmallDetails() {
    document.querySelectorAll('.portfolio-info').forEach(info => {
      const priceEl = info.querySelector('p strong');
      if (!priceEl) return;
      if (!info.querySelector('.zm-small-details')) {
        const small = document.createElement('div');
        small.className = 'text-muted small zm-small-details';
        small.textContent = 'In stock • Fast delivery';
        priceEl.parentElement.insertAdjacentElement('afterend', small);
      }
    });
  }

  document.addEventListener('DOMContentLoaded', () => {
    updateCartBadge();
    renderCart();

    // --- Products data layer (localStorage) and dynamic shop rendering ---
    const PROD_KEY = 'zm_products_v1';
    function readProducts(){ try { return JSON.parse(localStorage.getItem(PROD_KEY)||'[]'); } catch { return []; } }
    function writeProducts(list){ localStorage.setItem(PROD_KEY, JSON.stringify(list||[])); }
    const catToFilter = { phones: 'filter-phones', electronics: 'filter-electronics', fashion: 'filter-fashion', supermarket: 'filter-supermarket', home: 'filter-home', beauty: 'filter-beauty' };
    function detectCategoryByClasses(cls){
      const map = { 'filter-phones':'phones','filter-electronics':'electronics','filter-fashion':'fashion','filter-supermarket':'supermarket','filter-home':'home','filter-beauty':'beauty' };
      for (const key in map){ if (cls.contains(key)) return map[key]; }
      return 'electronics';
    }
    function parseKshStrong(el){ const t = (el?.textContent||'').replace(/[^0-9.]/g,''); return Number(t||0); }
    function seedProductsFromDOMIfEmpty(){
      const existing = readProducts();
      if (existing && existing.length) return;
      const cont = document.querySelector('.isotope-container'); if (!cont) return;
      const items = Array.from(cont.querySelectorAll('.portfolio-item'));
      const scraped = items.map(it=>{
        const info = it.querySelector('.portfolio-info');
        const name = (info?.querySelector('h4')?.textContent||'').trim();
        const price = parseKshStrong(info?.querySelector('p strong'));
        const img = it.querySelector('img')?.getAttribute('src')||'';
        const cat = detectCategoryByClasses(it.classList);
        return name && price ? { id: 'P-'+Math.random().toString(36).slice(2,8), name, price, img, category: cat, stock: 10, details: '', specs: {} } : null;
      }).filter(Boolean);
      if (scraped.length) writeProducts(scraped);
    }
    function normalizeImgPath(path){
      if (!path) return '';
      // Fix legacy paths saved in localStorage
      let p = path.replace('assets/img/projects/','assets/img/');
      p = p.replace('assets/img/hero-carousel/hero-carousel-','assets/img/');
      p = p.replace('assets/img/hero-carousel/New folder/','assets/img/');
      return p;
    }
    let shopSearchTerm = '';
    function renderShopFromProducts(){
      const cont = document.querySelector('.isotope-container'); if (!cont) return;
      let list = readProducts();
      const q = (shopSearchTerm||'').trim().toLowerCase();
      if (q) {
        list = list.filter(p => (p.name||'').toLowerCase().includes(q) || (p.category||'').toLowerCase().includes(q));
      }
      const frag = document.createDocumentFragment();
      let changed = false;
      try {
        list.forEach(p=>{
          const fixed = normalizeImgPath(p.img||'');
          if (fixed !== (p.img||'')) { p.img = fixed; changed = true; }
          const col = document.createElement('div');
          const filterCls = catToFilter[p.category] || 'filter-electronics';
          // denser grid: 2 on xs, 3 on md, 4 on lg, 6 on xl (Bootstrap only)
          col.className = `col-6 col-md-4 col-lg-3 col-xl-2 portfolio-item isotope-item ${filterCls}`;
          const priceNow = Number(p.price||0);
          const priceOldVal = p.oldPrice && Number(p.oldPrice)>priceNow ? Number(p.oldPrice) : Math.round(priceNow * 1.1);
          const showOld = priceOldVal > priceNow;
          const discount = showOld ? Math.max(1, Math.round((1 - priceNow/priceOldVal) * 100)) : 0;
          const galleryId = `gal-${p.id || Math.random().toString(36).slice(2,8)}`;
          col.innerHTML = `<div class="portfolio-content h-100">
              <a href="${p.img||'#'}" class="glightbox" data-gallery="${galleryId}" data-title="${(p.name||'')}">
                <img src="${p.img||'assets/img/1.jpg'}" class="img-fluid" alt="">
              </a>
              <div class="portfolio-info">
                <h4>${p.name}</h4>
                <div class="text-muted small">★★★★☆ (12 reviews)</div>
                <div class="price-box d-flex align-items-center justify-content-between">
                  <div class="prices">
                    <span class="price-now">KSh ${priceNow.toLocaleString()}</span>
                    ${showOld ? `<span class="price-old">KSh ${priceOldVal.toLocaleString()}</span>` : ''}
                    ${showOld ? `<span class="badge-discount">-${discount}%</span>` : ''}
                  </div>
                  <a href="#" class="btn btn-primary btn-sm" data-act="add">Add to Cart</a>
                </div>
              </div>
            </div>`;
          // append hidden anchors for more images into the same column to form a gallery group
          const extras = Array.isArray(p.images) ? p.images : [];
          extras.forEach((src)=>{
            const a = document.createElement('a');
            a.href = src; a.className = 'glightbox d-none'; a.setAttribute('data-gallery', galleryId); a.setAttribute('data-title', p.name||'');
            col.appendChild(a);
          });
          frag.appendChild(col);
        });
        if (changed) writeProducts(list);
        // Always replace content to reflect filtering
        cont.innerHTML = '';
        if (list.length) cont.appendChild(frag);
        // Re-init layout safely
        try {
          const layoutRoot = cont.closest('.isotope-layout');
          const layout = layoutRoot?.getAttribute('data-layout') ?? 'masonry';
          const filter = layoutRoot?.getAttribute('data-default-filter') ?? '*';
          const sort = layoutRoot?.getAttribute('data-sort') ?? 'original-order';
          if (typeof imagesLoaded === 'function') {
            imagesLoaded(cont, function(){
              if (typeof Isotope === 'function') {
                new Isotope(cont, { itemSelector: '.isotope-item', layoutMode: layout, filter: filter, sortBy: sort });
              }
              if (typeof aosInit === 'function') aosInit();
            });
          }
        } catch {}
        // Re-bind lightbox to new elements
        try { GLightbox({ selector: '.glightbox' }); } catch {}
      } catch (e) {
        // On any error, do not touch existing template items
      }
      // Update results summary
      const res = document.getElementById('searchResults');
      if (res) {
        if (q) {
          res.classList.remove('d-none');
          res.textContent = `Showing ${list.length} result${list.length===1?'':'s'} for "${shopSearchTerm}"`;
        } else {
          res.classList.add('d-none');
          res.textContent = '';
        }
      }
    }

    // seed from template if needed, then render and bind cart buttons
    seedProductsFromDOMIfEmpty();
    renderShopFromProducts();
    initAddToCartButtons();
    insertSmallDetails();

    // Shop search: filter products like Jumia
    const shopSearch = document.getElementById('shopSearch');
    if (shopSearch) {
      shopSearch.addEventListener('input', () => {
        shopSearchTerm = shopSearch.value || '';
        renderShopFromProducts();
        initAddToCartButtons();
        insertSmallDetails();
        const proj = document.getElementById('projects');
        if (proj) proj.scrollIntoView({ behavior: 'smooth', block: 'start' });
      });
    }

    // Open cart from nav link (cart is opened via toggleCart function)
    // Cart functionality is handled by the toggleCart function in the HTML

    // Function to update cart item quantity
    function updateCartItemQuantity(index, change) {
      const cart = readCart();
      if (cart[index]) {
        cart[index].qty = Math.max(1, (cart[index].qty || 1) + change);
        writeCart(cart);
        updateCartBadge();
        renderCart();
        // Refresh cart section if open
        if (document.body.classList.contains('cart-mode')) {
          // Cart section is handled by toggleCart function
        }
      }
    }

    // Function to remove cart item
    function removeCartItem(index) {
      const cart = readCart();
      if (cart[index]) {
        const itemName = cart[index].name;
        cart.splice(index, 1);
        writeCart(cart);
        updateCartBadge();
        renderCart();
        // Refresh cart section if open
        if (document.body.classList.contains('cart-mode')) {
          // Cart section is handled by toggleCart function
        }
        // Show notification
        showNotification(`${itemName} removed from cart`);
      }
    }

    // Auth helpers
    function getUser(){ try { return JSON.parse(localStorage.getItem('zetumart_user')||'null'); } catch { return null; } }
    function logout(){ 
    // Get current user before clearing
    const currentUser = getUser(); 
    localStorage.removeItem('zetumart_user'); 
    localStorage.removeItem('zetumart_is_admin'); 
    // Clear current user's cart when logging out
    if (currentUser && currentUser.email) {
      const userCartKey = `zetumart_cart_${currentUser.email.replace(/[^a-zA-Z0-9]/g, '_')}`;
      localStorage.setItem(userCartKey, '[]');
    }
    location.reload(); 
  }

    function updateNavAuth(){
      const user = getUser();
      const nav = document.querySelector('#navmenu ul');
      if (!nav) return;
      const loginLi = Array.from(nav.children).find(li=>li.querySelector('a[href="/login/"]'));
      const regLi = Array.from(nav.children).find(li=>li.querySelector('a[href="/register/"]'));
      const existingProfile = document.getElementById('profileMenu');
      if (user) {
        if (loginLi) loginLi.remove();
        if (regLi) regLi.remove();
        if (!existingProfile) {
          const li = document.createElement('li');
          li.className = 'dropdown';
          li.id = 'profileMenu';
          li.innerHTML = `<a href="#"><span>Profile</span> <i class="bi bi-chevron-down toggle-dropdown"></i></a>
            <ul>
              <li><a href="#">${user.name || user.email || 'Account'}</a></li>
              <li><a href="#" id="logoutLink">Logout</a></li>
            </ul>`;
          nav.appendChild(li);
        }
      } else {
        if (existingProfile) existingProfile.remove();
      }
      const logoutLink = document.getElementById('logoutLink');
      if (logoutLink) logoutLink.addEventListener('click', (e)=>{ e.preventDefault(); logout(); });
      
      // Refresh cart display when user state changes
      updateCartBadge();
      renderCart();
    }

    updateNavAuth();

    // Gate checkout behind login
    const openCheckout = document.getElementById('openCheckout');
    if (openCheckout) {
      openCheckout.addEventListener('click', (e) => {
        const user = getUser();
        if (!user) {
          e.preventDefault();
          // Don't redirect to login, just proceed with checkout
        }
      });
    }

    // Open chat from nav
    function openChat(tab){
      const el = document.getElementById('chatOffcanvas');
      if (el && window.bootstrap && bootstrap.Offcanvas) {
        const offc = bootstrap.Offcanvas.getOrCreateInstance(el);
        offc.show();
        // switch tab
        const targetId = tab === 'live' ? '#pane-live' : '#pane-ai';
        const btnId = tab === 'live' ? '#tab-live' : '#tab-ai';
        const btn = document.querySelector(btnId);
        if (btn && window.bootstrap && bootstrap.Tab) {
          bootstrap.Tab.getOrCreateInstance(btn).show();
        } else {
          document.querySelectorAll('#chatOffcanvas .tab-pane').forEach(p=>p.classList.remove('show','active'));
          const pane = document.querySelector(targetId);
          if (pane) pane.classList.add('show','active');
        }
      }
    }
    const openChatAI = document.getElementById('openChatAI');
    if (openChatAI) openChatAI.addEventListener('click', (e)=>{ e.preventDefault(); openChat('ai'); });
    const openChatLive = document.getElementById('openChatLive');
    if (openChatLive) openChatLive.addEventListener('click', (e)=>{ e.preventDefault(); openChat('live'); });

    // Capture contact form messages into localStorage for Admin > Messages
    const contactForm = document.querySelector('body.contact-page form.php-email-form');
    if (contactForm) {
      contactForm.addEventListener('submit', (e)=>{
        e.preventDefault();
        const name = contactForm.querySelector('input[name="name"]')?.value||'';
        const email = contactForm.querySelector('input[name="email"]')?.value||'';
        const subject = contactForm.querySelector('input[name="subject"]')?.value||'';
        const message = contactForm.querySelector('textarea[name="message"]')?.value||'';
        let msgs=[]; try { msgs = JSON.parse(localStorage.getItem('zm_messages_v1')||'[]'); } catch { msgs=[]; }
        msgs.push({ id: 'MSG-'+Math.random().toString(36).slice(2,8).toUpperCase(), date: new Date().toISOString(), name, email, subject, message });
        localStorage.setItem('zm_messages_v1', JSON.stringify(msgs));
        alert('Your message has been sent. Thank you!');
        contactForm.reset();
      });
    }
  });
})();

// ZetuMart: Checkout flow (payment options, counties, delivery fees)
(function() {
  "use strict";

  const counties = [
    'Nairobi','Mombasa','Kisumu','Nakuru','Kiambu','Machakos','Kajiado','Uasin Gishu','Nyeri','Murang\'a','Embu','Tharaka-Nithi','Meru','Laikipia','Kirinyaga','Kericho','Bomet','Kakamega','Vihiga','Bungoma','Busia','Siaya','Homa Bay','Migori','Kisii','Nyamira','Narok','Trans Nzoia','West Pokot','Elgeyo-Marakwet','Nandi','Baringo','Turkana','Samburu','Marsabit','Isiolo','Garissa','Wajir','Mandera','Tana River','Lamu','Kilifi','Taita-Taveta','Kwale','Kitui','Makueni'
  ];

  const countyFees = {
    'Nairobi': 200,
    'Mombasa': 250,
    'Kisumu': 250,
    'Nakuru': 220,
    'Kiambu': 220,
    'Machakos': 220,
    'Kajiado': 220
    // others fallback below
  };

  // Allow overriding fees from Admin Settings
  try {
    const settings = JSON.parse(localStorage.getItem('zm_settings_v1')||'null');
    if (settings && settings.fees && typeof settings.fees === 'object') {
      Object.assign(countyFees, settings.fees);
    }
  } catch {}

  function ksh(n){ return 'KSh ' + Number(n||0).toLocaleString(); }

  function readCart() {
    try { return JSON.parse(localStorage.getItem(getUserCartKey()) || '[]'); } catch { return []; }
  }
  function clearCart() { localStorage.setItem(getUserCartKey(), '[]'); }

  function subtotal() {
    return readCart().reduce((s, it) => s + (it.price||0) * (it.qty||1), 0);
  }

  function selectedDeliveryFee() {
    const sel = document.getElementById('countySelect');
    if (!sel) return 0;
    const name = sel.value;
    const base = countyFees[name];
    return base != null ? base : 300; // default fee
  }

  function updateCheckoutTotals() {
    const sub = subtotal();
    const del = selectedDeliveryFee();
    const total = sub + del;
    const sEl = document.getElementById('co-subtotal');
    const dEl = document.getElementById('co-delivery');
    const tEl = document.getElementById('co-total');
    if (sEl) sEl.textContent = ksh(sub);
    if (dEl) dEl.textContent = ksh(del);
    if (tEl) tEl.textContent = ksh(total);
  }

  function populateCounties() {
    const sel = document.getElementById('countySelect');
    if (!sel || sel.options.length) return;
    const frag = document.createDocumentFragment();
    counties.forEach(c => {
      const opt = document.createElement('option');
      opt.value = c; opt.textContent = c;
      frag.appendChild(opt);
    });
    sel.appendChild(frag);
    sel.value = 'Nairobi';
  }

  function toggleMpesaFields() {
    const mpesa = document.getElementById('payMpesa');
    const box = document.getElementById('mpesaFields');
    if (!mpesa || !box) return;
    box.classList.toggle('d-none', !mpesa.checked);
  }

  function validatePhone(phone) {
    // Basic KE mobile: 07XXXXXXXX (10 digits)
    return /^07\d{8}$/.test(phone.trim());
  }

  function appendOrderRecord(paymentMeta) {
    // Persist order with items, totals, statuses
    const items = readCart();
    const total = items.reduce((s,it)=> s + (it.price||0)*(it.qty||1), 0) + selectedDeliveryFee();
    let orders = [];
    try { orders = JSON.parse(localStorage.getItem('zm_orders_v1')||'[]'); } catch { orders = []; }
    let user = null; try { user = JSON.parse(localStorage.getItem('zetumart_user')||'null'); } catch {}
    const id = 'ORD-' + Math.random().toString(36).slice(2,8).toUpperCase();
    orders.push({ id, date: new Date().toISOString(), items, total, customer: user, paymentMethod: paymentMeta.method, paymentStatus: paymentMeta.status, shippingStatus: 'Pending' });
    localStorage.setItem('zm_orders_v1', JSON.stringify(orders));
  }

  function finishOrder() {
    // Close modal and offcanvas, clear cart and refresh UI
    clearCart();
    const offEl = document.getElementById('cartOffcanvas');
    if (offEl && window.bootstrap && bootstrap.Offcanvas) {
      bootstrap.Offcanvas.getOrCreateInstance(offEl).hide();
    }
    const modEl = document.getElementById('checkoutModal');
    if (modEl && window.bootstrap && bootstrap.Modal) {
      bootstrap.Modal.getOrCreateInstance(modEl).hide();
    }
    // Re-render cart counts if previous IIFE exists
    if (typeof window !== 'undefined') {
      try {
        const ev = new Event('DOMContentLoaded');
        document.dispatchEvent(ev);
      } catch {}
    }
    alert('Order placed successfully. Thank you for shopping with ZetuMart!');
  }

  document.addEventListener('DOMContentLoaded', () => {
    const checkoutModalEl = document.getElementById('checkoutModal');
    if (!checkoutModalEl) return;

    checkoutModalEl.addEventListener('shown.bs.modal', () => {
      populateCounties();
      updateCheckoutTotals();
      toggleMpesaFields();
    });

    const countySel = document.getElementById('countySelect');
    if (countySel) {
      countySel.addEventListener('change', updateCheckoutTotals);
    }

    const payDelivery = document.getElementById('payDelivery');
    const payMpesa = document.getElementById('payMpesa');
    const payTill = document.getElementById('payTill');
    const payCard = document.getElementById('payCard');
    const payPaypal = document.getElementById('payPaypal');
    const payPolepole = document.getElementById('payPolepole');

    function togglePaymentSections() {
      const mpesaBox = document.getElementById('mpesaFields');
      const cardBox = document.getElementById('cardFields');
      const paypalBox = document.getElementById('paypalFields');
      const tillBox = document.getElementById('tillFields');
      const polepoleBox = document.getElementById('polepoleFields');
      const isMpesa = payMpesa && payMpesa.checked;
      const isTill = payTill && payTill.checked;
      const isCard = payCard && payCard.checked;
      const isPaypal = payPaypal && payPaypal.checked;
      const isPole = payPolepole && payPolepole.checked;
      if (mpesaBox) mpesaBox.classList.toggle('d-none', !isMpesa);
      if (cardBox) cardBox.classList.toggle('d-none', !isCard);
      if (paypalBox) paypalBox.classList.toggle('d-none', !isPaypal);
      if (tillBox) tillBox.classList.toggle('d-none', !isTill);
      if (polepoleBox) polepoleBox.classList.toggle('d-none', !isPole);
    }

    [payDelivery, payMpesa, payTill, payCard, payPaypal, payPolepole].forEach(el => {
      if (el) el.addEventListener('change', () => { toggleMpesaFields(); togglePaymentSections(); });
    });

    const confirmBtn = document.getElementById('confirmCheckout');
    if (confirmBtn) {
      confirmBtn.addEventListener('click', async () => {
        const isMpesa = document.getElementById('payMpesa')?.checked;
        const isCard = document.getElementById('payCard')?.checked;
        const isTill = document.getElementById('payTill')?.checked;
        const isPaypal = document.getElementById('payPaypal')?.checked;
        const isPole = document.getElementById('payPolepole')?.checked;
        if (isMpesa) {
          const phone = document.getElementById('mpesaPhone')?.value || '';
          if (!validatePhone(phone)) {
            alert('Please enter a valid MPESA number (e.g., 07XXXXXXXX).');
            return;
          }
          const approved = document.getElementById('mpesaApproved')?.checked;
          if (!approved) { alert('Please approve the MPESA prompt first, then tick the checkbox.'); return; }
          // Simulate MPESA STK Push (placeholder). Replace with your backend endpoint.
          confirmBtn.disabled = true; confirmBtn.textContent = 'Processing...';
          setTimeout(() => {
            confirmBtn.disabled = false; confirmBtn.textContent = 'Confirm & Pay';
            appendOrderRecord({ method: 'mpesa', status: 'Paid' });
            alert('MPESA payment confirmed.');
            finishOrder();
          }, 1000);
        } else if (isTill) {
          const txt = document.getElementById('tillMessage')?.value.trim();
          if (!txt) { alert('Please paste your MPESA Till payment message.'); return; }
          confirmBtn.disabled = true; confirmBtn.textContent = 'Verifying...';
          setTimeout(() => { confirmBtn.disabled = false; confirmBtn.textContent = 'Confirm & Pay'; appendOrderRecord({ method: 'till', status: 'Paid' }); alert('Till payment verified.'); finishOrder(); }, 1200);
        } else if (isCard) {
          // Simulate card processing
          confirmBtn.disabled = true; confirmBtn.textContent = 'Processing...';
          setTimeout(() => { confirmBtn.disabled = false; confirmBtn.textContent = 'Confirm & Pay'; appendOrderRecord({ method: 'card', status: 'Paid' }); finishOrder(); }, 1200);
        } else if (isPaypal) {
          // Simulate PayPal redirect
          confirmBtn.disabled = true; confirmBtn.textContent = 'Redirecting...';
          setTimeout(() => { confirmBtn.disabled = false; confirmBtn.textContent = 'Confirm & Pay'; appendOrderRecord({ method: 'paypal', status: 'Paid' }); finishOrder(); }, 1200);
        } else if (isPole) {
          // Simulate pay polepole approval
          confirmBtn.disabled = true; confirmBtn.textContent = 'Setting up plan...';
          setTimeout(() => { confirmBtn.disabled = false; confirmBtn.textContent = 'Confirm & Pay'; appendOrderRecord({ method: 'polepole', status: 'Partial' }); finishOrder(); }, 1200);
        } else {
          // Cash on Delivery
          appendOrderRecord({ method: 'cod', status: 'Unpaid' });
          finishOrder();
        }
      });
    }

    // Explicit STK push button
    const stkBtn = document.getElementById('sendStkBtn');
    if (stkBtn) {
      stkBtn.addEventListener('click', () => {
        const phone = document.getElementById('mpesaPhone')?.value || '';
        const status = document.getElementById('stkStatus');
        if (!validatePhone(phone)) { alert('Enter a valid MPESA number (07XXXXXXXX).'); return; }
        if (status) status.textContent = 'Sending STK push...';
        stkBtn.disabled = true;
        setTimeout(() => { if (status) status.textContent = 'STK push sent. Check your phone and approve.'; stkBtn.disabled = false; }, 1200);
      });
    }

    // Till submit
    const tillBtn = document.getElementById('submitTillBtn');
    if (tillBtn) {
      tillBtn.addEventListener('click', () => {
        const txt = document.getElementById('tillMessage')?.value.trim();
        const status = document.getElementById('tillStatus');
        if (!txt) { alert('Paste your MPESA message first.'); return; }
        if (status) status.textContent = 'Submitting message...';
        tillBtn.disabled = true;
        setTimeout(() => { if (status) status.textContent = 'Message received. We will verify shortly.'; tillBtn.disabled = false; }, 1000);
      });
    }
  });
})();

// ZetuMart: Simple auth helpers for login/register pages
(function(){
  'use strict';
  document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.querySelector('body.login-page .php-email-form, body .php-email-form#loginForm');
    const registerForm = document.querySelector('body.register-page .php-email-form, body .php-email-form#registerForm');
    function afterAuth() {
      const params = new URLSearchParams(location.search);
      const ret = params.get('return') || '/';
      window.location.href = ret;
    }
    if (loginForm) {
      loginForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const emailOrUser = loginForm.querySelector('input[name="email"]')?.value || '';
        const pass = loginForm.querySelector('input[name="password"]')?.value || '';
        // Admin login: Username "admin" and Password "root" -> redirect to admin page
        if (emailOrUser.trim().toLowerCase() === 'admin' && pass === 'root') {
          localStorage.setItem('zetumart_user', JSON.stringify({ email: 'admin@zetumart', name: 'Admin' }));
          localStorage.setItem('zetumart_is_admin', 'true');
          window.location.href = 'admin.html';
          return;
        }
        localStorage.setItem('zetumart_user', JSON.stringify({ email: emailOrUser }));
        // ensure user exists in users store
        try {
          const key = 'zm_users_v1';
          const users = JSON.parse(localStorage.getItem(key)||'[]');
          const id = (emailOrUser||'').toLowerCase();
          if (id && !users.find(u=> (u.email||'').toLowerCase()===id)) {
            users.push({ id: 'U-'+Math.random().toString(36).slice(2,8), email: emailOrUser, name: emailOrUser.split('@')[0]||'User', blocked: false });
            localStorage.setItem(key, JSON.stringify(users));
          }
        } catch {}
        localStorage.removeItem('zetumart_is_admin');
        afterAuth();
      });
    }
    if (registerForm) {
      registerForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const email = registerForm.querySelector('input[name="email"]')?.value || '';
        const name = registerForm.querySelector('input[name="name"]')?.value || '';
        localStorage.setItem('zetumart_user', JSON.stringify({ email, name }));
        try {
          const key = 'zm_users_v1';
          const users = JSON.parse(localStorage.getItem(key)||'[]');
          if (email && !users.find(u=> (u.email||'').toLowerCase()===email.toLowerCase())) {
            users.push({ id: 'U-'+Math.random().toString(36).slice(2,8), email, name, blocked: false });
            localStorage.setItem(key, JSON.stringify(users));
          }
        } catch {}
        afterAuth();
      });
    }
  });
})();