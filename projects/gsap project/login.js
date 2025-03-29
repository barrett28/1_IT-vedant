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
