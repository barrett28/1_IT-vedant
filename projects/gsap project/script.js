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
    stagger: 0.15,
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
    y: 20,
    duration: 1,
    repeat: -1,
    yoyo: true,
    delay: 0.5,
    ease: "easeInOut",
  },
  "anime"
);
