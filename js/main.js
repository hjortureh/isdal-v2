// ÍSDAL — shared interactions

// mobile menu
const menuBtn = document.querySelector('.menu-btn');
const nav = document.querySelector('.site-nav');
if (menuBtn && nav) {
  menuBtn.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    menuBtn.textContent = open ? 'Loka' : 'Valmynd';
  });
}

// scroll reveal
const io = new IntersectionObserver(
  (entries) => {
    for (const e of entries) {
      if (e.isIntersecting) {
        e.target.classList.add('in');
        io.unobserve(e.target);
      }
    }
  },
  { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
);
document.querySelectorAll('.reveal').forEach((el) => io.observe(el));

// hero carousel (front page)
const carousel = document.querySelector('.hero-carousel');
if (carousel) {
  const slides = carousel.querySelectorAll('.slide');
  const dots = carousel.querySelectorAll('.dots button');
  let current = 0;
  let timer;
  const show = (n) => {
    current = (n + slides.length) % slides.length;
    slides.forEach((s, i) => s.classList.toggle('is-active', i === current));
    dots.forEach((d, i) => d.classList.toggle('active', i === current));
  };
  const start = () => {
    timer = setInterval(() => show(current + 1), 4500);
  };
  dots.forEach((d, i) =>
    d.addEventListener('click', () => {
      clearInterval(timer);
      show(i);
      start();
    })
  );
  start();
}

// project filter (verkefni page)
const filterbar = document.querySelector('.filterbar');
if (filterbar) {
  const cards = document.querySelectorAll('.pcard[data-cat]');
  filterbar.addEventListener('click', (ev) => {
    const btn = ev.target.closest('button[data-filter]');
    if (!btn) return;
    filterbar.querySelectorAll('button').forEach((b) => b.classList.remove('active'));
    btn.classList.add('active');
    const f = btn.dataset.filter;
    cards.forEach((c) => {
      c.classList.toggle('hidden', f !== 'allt' && !c.dataset.cat.includes(f));
    });
  });
}

// contact form → mailto (no backend in prototype)
const form = document.querySelector('form.contact-form');
if (form) {
  form.addEventListener('submit', (ev) => {
    ev.preventDefault();
    const d = new FormData(form);
    const subject = encodeURIComponent('Fyrirspurn frá vef — ' + (d.get('nafn') || ''));
    const body = encodeURIComponent(
      'Nafn: ' + d.get('nafn') + '\nNetfang: ' + d.get('netfang') + '\n\n' + d.get('skilabod')
    );
    window.location.href = 'mailto:info@isdal.is?subject=' + subject + '&body=' + body;
  });
}
