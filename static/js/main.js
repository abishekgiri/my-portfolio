document.addEventListener('DOMContentLoaded', () => {
    // Custom Cursor
    const cursorDot = document.querySelector('.cursor-dot');
    const cursorOutline = document.querySelector('.cursor-outline');

    // Check if device is touch or coarse pointer
    const isTouch = ('ontouchstart' in window) || (navigator.maxTouchPoints > 0);
    const isCoarse = window.matchMedia && window.matchMedia('(pointer: coarse)').matches;

    if (!isTouch && !isCoarse && cursorDot && cursorOutline) {
        document.body.classList.add('custom-cursor');
        window.addEventListener('mousemove', (e) => {
            const posX = e.clientX;
            const posY = e.clientY;

            // Dot follows instantly
            cursorDot.style.left = `${posX}px`;
            cursorDot.style.top = `${posY}px`;

            // Outline follows with lag
            cursorOutline.animate({
                left: `${posX}px`,
                top: `${posY}px`
            }, { duration: 500, fill: "forwards" });
        });

        // Hover Effect
        const hoverTargets = document.querySelectorAll('a, button, .bento-card');
        hoverTargets.forEach(el => {
            el.addEventListener('mouseenter', () => cursorOutline.classList.add('hovered'));
            el.addEventListener('mouseleave', () => cursorOutline.classList.remove('hovered'));
        });
    } else {
        if (cursorDot) cursorDot.style.display = 'none';
        if (cursorOutline) cursorOutline.style.display = 'none';
    }

    // 3D Tilt Effect for Bento Cards
    const reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduceMotion) return;

    const cards = document.querySelectorAll('.bento-card');

    cards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            if (window.innerWidth <= 768) return;

            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            const textContent = card.querySelector('.parallax-content');

            // Calculate rotation
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            const rotateX = ((y - centerY) / centerY) * -3; // Max 3 deg
            const rotateY = ((x - centerX) / centerX) * 3;

            card.style.transform = `perspective(1000px) translateY(-2px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.01, 1.01, 1.01)`;
        });

        card.addEventListener('mouseleave', () => {
            card.style.transform = '';
        });
    });
});
