gsap.registerPlugin(ScrollTrigger);

// Sare panels except first ko animate karenge
const panels = document.querySelectorAll(".panel");

panels.forEach((panel, index) => {
  if (index === 0) return;

  gsap.fromTo(
    panel,
    { yPercent: 100 },
    {
      yPercent: 0,
      ease: "none",
      scrollTrigger: {
        trigger: panel,
        start: "top bottom",
        end: "top top",
        scrub: true,
        pin: true,
        pinSpacing: false,
      },
    }
  );
});
