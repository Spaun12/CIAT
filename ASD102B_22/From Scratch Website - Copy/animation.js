// Michael D. Connell Jr. Beginner Website creation project 2023 CIAT WebDevelopment

// text animation
function animateText() {
    anime({
      targets: '#animated-text',
      translateY: [-100, 0],
      opacity: [0, 1],
      easing: 'easeOutElastic(1, .8)',
      duration: 2000,
    });
  }
  
  document.addEventListener('DOMContentLoaded', animateText);