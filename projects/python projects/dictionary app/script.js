const form = document.querySelector("form");
const resultDiv = document.querySelector(".result");

form?.addEventListener("submit", (e) => {
  e.preventDefault();
  getWordInfo(form.elements[0].value);
});

const getWordInfo = (word) => {
  alert("Word:" + word);
};
