gsap.to("#box", {
  x: 1200,
  duration: 2.5,
  delay: 1,
  rotate: 360,
  borderRadius: "50%",
  scale: 0.5,
  yoyo: true,
  //   repeat: -1,
  backgroundColor: "yellow",
});

gsap.from("#box1", {
  y: 200,
  duration: 2,
});
