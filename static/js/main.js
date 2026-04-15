document.addEventListener('DOMContentLoaded', () => {
    const clock = document.querySelector('.live-time');
    if (!clock) {
        return;
    }

    const zone = clock.dataset.zone || 'America/New_York';

    const renderTime = () => {
        clock.textContent = new Intl.DateTimeFormat('en-US', {
            timeZone: zone,
            hour: '2-digit',
            minute: '2-digit',
            hour12: false
        }).format(new Date());
    };

    renderTime();
    window.setInterval(renderTime, 30000);
});
