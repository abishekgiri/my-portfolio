// Mobile nav toggle + scroll reveal
(function () {
  if (typeof window === 'undefined' || typeof document === 'undefined') return;

  // ---------- Mobile nav ----------
  const header = document.querySelector('.site-header');
  const toggle = document.querySelector('.nav-toggle');
  const nav = document.querySelector('.site-nav');

  if (header && toggle && nav) {
    const closeNav = () => {
      header.classList.remove('is-nav-open');
      toggle.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
    };

    const openNav = () => {
      header.classList.add('is-nav-open');
      toggle.setAttribute('aria-expanded', 'true');
      document.body.style.overflow = 'hidden';
    };

    toggle.addEventListener('click', () => {
      if (header.classList.contains('is-nav-open')) closeNav();
      else openNav();
    });

    // Close when a link is tapped
    nav.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', closeNav);
    });

    // Close on Escape
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') closeNav();
    });

    // Reset state when resizing back to desktop
    const resetOnResize = window.matchMedia('(min-width: 721px)');
    resetOnResize.addEventListener('change', (e) => {
      if (e.matches) closeNav();
    });
  }

  // ---------- Scroll reveal ----------
  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const targets = document.querySelectorAll('.section, .project-card, .timeline-item, .surface-card');
  if (!targets.length) return;

  if (prefersReduced || !('IntersectionObserver' in window)) {
    targets.forEach((el) => el.classList.add('is-visible'));
    return;
  }

  targets.forEach((el) => el.classList.add('reveal'));

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    },
    { rootMargin: '0px 0px -10% 0px', threshold: 0.08 }
  );

  targets.forEach((el) => observer.observe(el));
})();
