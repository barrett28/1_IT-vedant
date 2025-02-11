const form = document.querySelector("form");
const resultDiv = document.querySelector(".result");

form?.addEventListener("submit", (e) => {
  e.preventDefault();
  getWordInfo(form.elements[0].value);
});

const getWordInfo = async (word) => {
  const response = await fetch(
    `https://api.dictionaryapi.dev/api/v2/entries/en/${word}`
  );
  const data = await response.json();

  resultDiv.innerHTML = `
  <h2> <strong>Word:</strong> ${data[0].word}</h2>
  <p> <strong>Part Of Speech:</strong> ${data[0].meanings[0].partOfSpeech}</p>
  <p> <strong>Definition:</strong> ${data[0].meanings[0].definitions[0].definition}</p>
  <p> <strong>Example:</strong> ${data[0].meanings[0].definitions[0].example}</p>
  `;
  console.log(data);
};

// const form = document.querySelector("form");
// const resultDiv = document.querySelector(".result");

// form?.addEventListener("submit", (e) => {
//   e.preventDefault();
//   const word = form.elements[0].value.trim();
//   if (word) {
//     getWordInfo(word);
//   } else {
//     resultDiv.innerHTML = "<p>Please enter a word.</p>";
//   }
// });

// const getWordInfo = async (word) => {
//   try {
//     const response = await fetch(
//       `https://api.dictionaryapi.dev/api/v2/entries/en/${word}`
//     );

//     if (!response.ok) {
//       throw new Error("Word not found");
//     }

//     const data = await response.json();

//     // Check if data is an array and has valid structure
//     if (
//       Array.isArray(data) &&
//       data.length > 0 &&
//       data[0].meanings?.length > 0
//     ) {
//       const definition =
//         data[0].meanings[0].definitions[0]?.definition || "No definition found";
//       resultDiv.innerHTML = `<h2>${word}</h2><p>${definition}</p>`;
//     } else {
//       resultDiv.innerHTML = "<p>No definitions available.</p>";
//     }

//     console.log(data);
//   } catch (error) {
//     resultDiv.innerHTML = "<p>Word not found. Please try another word.</p>";
//     console.error(error);
//   }
// };
