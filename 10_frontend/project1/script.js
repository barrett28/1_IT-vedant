// locomotive code

const scroll = new LocomotiveScroll({
  el: document.querySelector("main"),
  smooth: true,
});

// curosr code

var a = document.querySelector("main");
var b = document.querySelector("#cursor");

a.addEventListener("mousemove", function (e) {
  // console.log(e.clientX, e.clientY)
  b.style.transform = `translate(${e.clientX}px, ${e.clientY}px)`;
});

// 2nd page hover code
