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
    y: 10,
    duration: 1,
    repeat: -1,
    yoyo: true,
    delay: 0.5,
    ease: "easeInOut",
  },
  "anime"
);

// ----section2--
// gsap.from(".services h3", {
//   x: -100,
//   duration: 0.8,
//   opacity: 0,
//   scrollTrigger: {
//     trigger: ".services h3",
//     scroller: "body",
//     markers: true,
//     start: "top 50%",
//   },
// });
// gsap.from(".services p", {
//   y: -50,
//   duration: 0.8,
//   opacity: 0,
//   scrollTrigger: {
//     trigger: ".services h3",
//     scroller: "body",
//     markers: true,
//     start: "top 50%",
//   },
// });

var tl2 = gsap.timeline({
  scrollTrigger: {
    trigger: ".section2",
    scroller: "body",
    markers: true,
    start: "top 45%",
    end: "top 90%",
    scrub: 2,
  },
});

tl2.from(".services", {
  x: -200,
  opacity: 0,
  duration: 0.8,
});

tl2.from(
  ".elem.left1",
  {
    y: 100,
    // x: -200,
    opacity: 0,
    rotate: 30,
    duration: 4,
  },
  "anime1"
);
tl2.from(
  ".elem.right1",
  {
    y: 100,
    // x: 200,
    opacity: 0,
    rotate: -30,
    duration: 4,
  },
  "anime1"
);

// ----login /signup-----

document.addEventListener("DOMContentLoaded", () => {
  const formTitle = document.getElementById("form-title");
  const toggleText = document.getElementById("toggle-text");
  const toggleLink = document.getElementById("toggle-link");
  const authForm = document.getElementById("auth-form");

  let isLogin = true;

  toggleLink.addEventListener("click", () => {
    isLogin = !isLogin;
    formTitle.textContent = isLogin ? "Login" : "Sign Up";
    toggleText.innerHTML = isLogin
      ? "Don't have an account? <span id='toggle-link'>Sign Up</span>"
      : "Already have an account? <span id='toggle-link'>Login</span>";
    document
      .getElementById("toggle-link")
      .addEventListener("click", toggleLink.click);
  });

  authForm.addEventListener("submit", (e) => {
    e.preventDefault();
    alert(isLogin ? "Logging in..." : "Signing up...");
  });
});
