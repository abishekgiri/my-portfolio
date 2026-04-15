document.addEventListener('DOMContentLoaded', () => {
    const reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduceMotion || window.innerWidth <= 900) {
        return;
    }

    const interactiveCards = document.querySelectorAll('.project-card, .info-card, .timeline-card, .skill-card');

    interactiveCards.forEach((card) => {
        card.addEventListener('mousemove', (event) => {
            const rect = card.getBoundingClientRect();
            const x = event.clientX - rect.left;
            const y = event.clientY - rect.top;
            const offsetX = (x / rect.width) - 0.5;
            const offsetY = (y / rect.height) - 0.5;

            card.style.transform = `translateY(-4px) rotateX(${offsetY * -2.2}deg) rotateY(${offsetX * 2.4}deg)`;
        });

        card.addEventListener('mouseleave', () => {
            card.style.transform = '';
        });
    });
});
