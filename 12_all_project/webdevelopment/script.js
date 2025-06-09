Shery.mouseFollower();

Shery.makeMagnet(".menuIcon, .image");

Shery.hoverWithMediaCircle(".hover", {
  videos: ["./cover-2.mp4", "./cover-1.mp4", "./cover-3.mp4"],
});

gsap.to(".leftitem", {
  scrollTrigger: {
    trigger: "#fimage",
    pin: true,
    start: "top top",
    end: "bottom bottom",
    endTrigger: ".last",
    scrub: 1,
  },
  y: "-300%",
  ease: Power1,
});

let sections = document.querySelectorAll(".leftitem");
Shery.imageEffect("#fright .image", {
  style: 2,
  config: { onMouse: { value: 1 } },
  slideStyle: (setScroll) => {
    sections.forEach(function (section, index) {
      ScrollTrigger.create({
        trigger: section,
        start: "top top",
        scrub: 1,
        onUpdate: function (prog) {
          setScroll(prog.progress + index);
        },
      });
    });
  },
});
