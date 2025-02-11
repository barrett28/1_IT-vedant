// @ts-nocheck
const form = document.querySelector("form");
const resultDiv = document.querySelector(".result");

form?.addEventListener("submit", (e) => {
  e.preventDefault();
  getWordInfo(form.elements[0].value);
});

const getWordInfo = async (word) => {
  try {
    resultDiv.innerHTML = `<p>Fetching data...</p>`;
    const response = await fetch(
      `https://api.dictionaryapi.dev/api/v2/entries/en/${word}`
    );
    const data = await response.json();

    resultDiv.innerHTML = `
  <h2> <strong>Word:</strong> ${data[0].word}</h2>
  <p> <strong>Part Of Speech:</strong> ${data[0].meanings[0].partOfSpeech}</p>
  <p> <strong>Meaning:</strong> ${
    data[0].meanings[0].definitions[0].definition === undefined
      ? "Not Found"
      : data[0].meanings[0].definitions[0].definition
  }</p>
  <p> <strong>Example:</strong> ${
    data[0].meanings[0].definitions[0].example === undefined
      ? "Not Found"
      : data[0].meanings[0].definitions[0].example
  }</p>
  <p> <strong>Synonyms: </strong> ${
    data[0].meanings[0].synonyms === undefined
      ? "Not Found"
      : data[0].meanings[0].synonyms
  }
  </p>
  <p class="anto"> <strong>Antonyms: </strong> ${
    data[0].meanings[0].antonyms === undefined
      ? "Not Found"
      : data[0].meanings[0].antonyms
  }
  </p>
  `;

    // for (let i=0; i<data[0].meanings[0].definitions[0].)

    //adding source url
    resultDiv.innerHTML += `<a href="${data[0].sourceUrls}" target="_blank">Read More</a>`;
  } catch {
    resultDiv.innerHTML = `<p>Word could not be found</p>`;
  }
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
