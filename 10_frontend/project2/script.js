function init() {
  gsap.registerPlugin(ScrollTrigger);

  const locoScroll = new LocomotiveScroll({
    el: document.querySelector("main"),
    smooth: true,
  });
  locoScroll.on("scroll", ScrollTrigger.update);

  ScrollTrigger.scrollerProxy("main", {
    scrollTop(value) {
      return arguments.length
        ? locoScroll.scrollTo(value, 0, 0)
        : locoScroll.scroll.instance.scroll.y;
    },
    getBoundingClientRect() {
      return {
        top: 0,
        left: 0,
        width: window.innerWidth,
        height: window.innerHeight,
      };
    },
    pinType: document.querySelector("main").style.transform
      ? "transform"
      : "fixed",
  });

  ScrollTrigger.addEventListener("refresh", () => locoScroll.update());

  ScrollTrigger.refresh();
}
init();

var tl = gsap.timeline({
  scrollTrigger: {
    trigger: ".text-wrapper",
    scroller: "main",
    markers: true,
    start: "top 20%",
    end: "top 0",
    scrub: true,
  },
});
tl.to(
  "#page1 h1",
  {
    x: -100,
    duration: 1,
  },
  "anim"
);
tl.to(
  "#page1 h2",
  {
    x: 100,
    duration: 1,
  },
  "anim"
);

tl.to(
  "#page1 .vid-wrapper video",
  {
    width: "90%",
    duration: 2,
  },
  "anim"
);
