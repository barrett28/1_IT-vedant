document.addEventListener("DOMContentLoaded", () => {
  const cards = document.querySelectorAll(".card");

  cards.forEach((card) => {
    card.addEventListener("click", () => {
      if (!card.classList.contains("active")) {
        const activeCard = document.querySelector(".card.active");

        // Animate the clicked card to the top
        card.style.transition = "all 0.5s ease";
        card.classList.add("active");

        // Push the previous active card back into the stack
        activeCard.classList.remove("active");
        activeCard.style.zIndex = cards.length - 1;

        // Reset z-index for all cards (except the new active one)
        cards.forEach((c, index) => {
          if (!c.classList.contains("active")) {
            c.style.zIndex = index;
          }
        });
      }
    });
  });
});
