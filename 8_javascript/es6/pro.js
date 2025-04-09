// console.log("promise");

// var ans = new Promise((res, rej) => {
//   if (true) {
//     return res();
//   } else {
//     return rej();
//   }
// });

// ans
//   .then(function () {
//     console.log("resolved");
//   })
//   .catch(function () {
//     console.log("not resolved");
//   });

// ======================

const pOne = new Promise(function (resolve, reject) {
  setTimeout(() => {
    console.log("Task Completed which acted as an async");
    resolve();
  }, 1000);
});

pOne.then(function () {
  console.log("promise task completed");
});
