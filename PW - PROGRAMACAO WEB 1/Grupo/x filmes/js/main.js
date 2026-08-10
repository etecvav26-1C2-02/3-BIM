(function () {
  'use strict';

  const grid = document.getElementById('catalogGrid');
  const sectionTitle = document.getElementById('sectionTitle');
  const resultsCount = document.getElementById('resultsCount');
  const emptyState = document.getElementById('emptyState');
  const emptyTerm = document.getElementById('emptyTerm');
  const searchInput = document.getElementById('searchInput');
  const navLinks = document.querySelectorAll('.nav-link');
  const menuToggle = document.getElementById('menuToggle');
  const nav = document.getElementById('nav');

  let currentFilter = 'todos';
  let searchTerm = '';

  const TITLES = {
    todos: 'Todos os títulos',
    filme: 'Filmes',
    serie: 'Séries'
  };

  function normalize(value) {
    return value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  }

  function cardHTML(item, index) {
    const inner = `
        <div class="card-poster">
          <img src="${item.image}" alt="${item.title}" loading="lazy">
          <span class="badge badge-${item.type}">${item.type === 'filme' ? 'Filme' : 'Série'}</span>
          <span class="badge-year">${item.year}</span>
        </div>
        <div class="card-info">
          <h3 class="card-title">${item.title}</h3>
          <div class="card-meta">${item.year} &middot; ${item.type === 'filme' ? 'Filme' : 'Série'}</div>
        </div>
    `;
    if (item.url) {
      return `<a href="${item.url}" class="card" target="_blank" rel="noopener" style="animation-delay:${(index % 12) * 45}ms">${inner}</a>`;
    }
    return `<div class="card" style="animation-delay:${(index % 12) * 45}ms">${inner}</div>`;
  }

  function filteredItems() {
    const term = normalize(searchTerm.trim());
    return CATALOG.filter(function (item) {
      const matchesType = currentFilter === 'todos' || item.type === currentFilter;
      const matchesSearch = !term || normalize(item.title).includes(term);
      return matchesType && matchesSearch;
    });
  }

  function render() {
    const items = filteredItems();

    grid.innerHTML = items.map(cardHTML).join('');
    sectionTitle.textContent = TITLES[currentFilter];
    resultsCount.textContent = items.length === 1
      ? '1 título'
      : items.length + ' títulos';

    emptyState.hidden = items.length > 0;
    if (items.length === 0) {
      emptyTerm.textContent = searchTerm.trim();
    }
  }

  function setFilter(filter, activeLink) {
    currentFilter = filter;
    navLinks.forEach(function (link) {
      link.classList.toggle('active', link === activeLink);
    });
    render();
  }

  navLinks.forEach(function (link) {
    link.addEventListener('click', function (event) {
      event.preventDefault();
      setFilter(link.dataset.filter, link);
      nav.classList.remove('open');
      menuToggle.classList.remove('open');
    });
  });

  let searchTimer;
  searchInput.addEventListener('input', function () {
    clearTimeout(searchTimer);
    searchTimer = setTimeout(function () {
      searchTerm = searchInput.value;
      render();
    }, 150);
  });

  menuToggle.addEventListener('click', function () {
    const open = nav.classList.toggle('open');
    menuToggle.classList.toggle('open', open);
  });

  render();
})();
