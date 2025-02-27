// script.js
let currentIndex = 0;

function showSlide(index) {
  const slides = document.querySelector(".carousel-container");
  const totalSlides = document.querySelectorAll(
    ".carousel-container img"
  ).length;

  if (index >= totalSlides) {
    currentIndex = 0; // Reset to first slide
  } else if (index < 0) {
    currentIndex = totalSlides - 1; // Go to last slide
  } else {
    currentIndex = index;
  }

  let translateX = -currentIndex * 500; // Adjust based on image width
  slides.style.transform = `translateX(${translateX}px)`;
}

function prevSlide() {
  showSlide(currentIndex - 1);
}

function nextSlide() {
  showSlide(currentIndex + 1);
}

// Auto slide every 3 seconds
setInterval(() => {
  nextSlide();
}, 3000);
