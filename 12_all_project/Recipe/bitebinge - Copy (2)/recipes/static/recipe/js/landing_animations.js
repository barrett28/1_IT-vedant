document.addEventListener("DOMContentLoaded", function () {
  // Only run on landing page
  if (!document.querySelector(".section1")) return;

  // Register ScrollTrigger plugin
  gsap.registerPlugin(ScrollTrigger);

  // Navbar animation timeline
  var tl = gsap.timeline();
  tl.from(
    "nav h1, nav .search-container, nav a",
    {
      y: -30,
      opacity: 0,
      duration: 0.7,
      delay: 0.5,
      stagger: 0.15,
    },
    "anime"
  );

  // Hero section animations
  tl.from(
    ".center-part1 h1",
    {
      y: -300,
      opacity: 0,
      duration: 0.8,
      stagger: 0.15,
      delay: 0.5,
    },
    "anime"
  );

  tl.from(
    ".center-part1 p",
    {
      y: 50,
      opacity: 0,
      duration: 0.8,
      delay: 0.5,
      stagger: 0.2,
    },
    "anime"
  );

  tl.from(
    ".center-part1 button",
    {
      opacity: 0,
      duration: 0.8,
      delay: 0.5,
    },
    "anime"
  );

  tl.from(
    ".center-part2 img",
    {
      y: 10,
      duration: 1,
      repeat: -1,
      yoyo: true,
      delay: 0.5,
      ease: "easeInOut",
    },
    "anime"
  );

  // Section 2 animations
  var tl2 = gsap.timeline({
    scrollTrigger: {
      trigger: ".section2",
      scroller: "body",
      markers: false, // Set to true for debugging
      start: "top 45%",
      end: "top 90%",
      scrub: 2,
    },
  });

  tl2.from(".services", {
    x: -200,
    opacity: 0,
    duration: 0.5,
  });

  tl2.from(
    ".elem.left1",
    {
      y: 100,
      opacity: 0,
      rotate: 30,
      duration: 3,
    },
    "anime1"
  );

  tl2.from(
    ".elem.right1",
    {
      y: 100,
      opacity: 0,
      rotate: -30,
      duration: 3,
    },
    "anime1"
  );
});
