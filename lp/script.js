document.addEventListener('DOMContentLoaded', function() {
    // Basic script for the static landing page.
    // The carousel uses Bootstrap's JS, so we only need custom logic if desired.
    console.log("Landing page loaded successfully.");
    initFeaturedCarousel();
});

function initFeaturedCarousel() {
  const tracks = document.querySelectorAll('.featured-carousel-track');
  
  tracks.forEach(track => {
    let scrollSpeed = 1;
    let isPaused = false;
    let animationFrameId;
    
    function autoScroll() {
      if (!isPaused) {
        track.scrollLeft += scrollSpeed;
        if (track.scrollLeft >= (track.scrollWidth - track.clientWidth - 1)) {
           track.scrollLeft = 0;
        }
      }
      animationFrameId = requestAnimationFrame(autoScroll);
    }
    
    animationFrameId = requestAnimationFrame(autoScroll);
    
    const pauseScroll = () => { isPaused = true; };
    const resumeScroll = () => { isPaused = false; };
    
    track.addEventListener('mouseenter', pauseScroll);
    track.addEventListener('mouseleave', resumeScroll);
    track.addEventListener('touchstart', pauseScroll, {passive: true});
    track.addEventListener('touchend', resumeScroll);
    
    const wrapper = track.closest('.featured-carousel-wrapper');
    if (wrapper) {
      const prevBtn = wrapper.querySelector('.carousel-nav-btn.prev');
      const nextBtn = wrapper.querySelector('.carousel-nav-btn.next');
      
      if (prevBtn) {
        prevBtn.addEventListener('click', () => { track.scrollBy({ left: -320, behavior: 'smooth' }); });
        prevBtn.addEventListener('mouseenter', pauseScroll);
        prevBtn.addEventListener('mouseleave', resumeScroll);
      }
      
      if (nextBtn) {
        nextBtn.addEventListener('click', () => { track.scrollBy({ left: 320, behavior: 'smooth' }); });
        nextBtn.addEventListener('mouseenter', pauseScroll);
        nextBtn.addEventListener('mouseleave', resumeScroll);
      }
    }
  });
}
