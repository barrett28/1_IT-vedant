const marvel_hero = ["ironman", "captain", "thor"];
const dc_hero = ["Batman", "Aquaman", "flash"];

// marvel_hero.push(dc_hero); // kuch return nhi krta hai and array me array ko hi push kr deta hai
// console.log(marvel_hero);

// so we will use "concat", ye ek naya array return krta hai and usme sahi hai add hote hai element

const all_hero = marvel_hero.concat(dc_hero);
// console.log(all_hero);

// ek aur method hai "split" method
const all_hero2 = [...marvel_hero, ...dc_hero];
// console.log(all_hero2);

console.log(Array.isArray("vedant"));
console.log(Array.from("vedant")); // ye array me convert kr dega

let score1 = 100;
let score2 = 200;
let score3 = 300;

console.log(Array.of(score1, score2, score3)); // "of" different element ko leke ek array return krta hai
