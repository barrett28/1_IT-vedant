let age = "33abc";

console.log(typeof age);

let changeToString = Number(age);
// console.log("changed to number->", typeof changeToString);
// console.log(changeToString);

/*
agar ham koi string jisme number and string dono ho tho jese ki "33qbs" types 
tho isko Number me convert krte samay ye number me convert kr dega 
pr uska tho value vo Nan  me convert ho jayega 


same undefined k sath be hoga 
jb hm ek varibale me undefined istemal krte hai 
and usko Number me convert krte vakt uski value "Nan" ho jayegi 

same cheez "string" k sath bhi hogi
jb hm string jisme koi number na ho "hello" ✅  ,  "hello12" ❌
tn Number me convert krte vakt iski value bhi "Nan" ho jayegi
*/

let score = null;

console.log(typeof score);

let changeNullToNumber = Number(score);
// console.log(typeof changeNullToNumber);
// console.log(changeNullToNumber);

/*
Aur agar hm "Null" dene k baad usko Number me change krte hai tho uski value "0" ho jayega 
*/

let bol = 0;
let convertToBool = Boolean(bol);
// console.log(typeof convertToBool);
// console.log(convertToBool);

/* jb boolean me convert krte hai tb
    0 -> flase 
    1-> true
    empty string "" -> false
    "hello" -> true
*/
// Number, String, Boolean  ---> first letter capital hoga for conversion

console.log(3 + ((4 * 5) % 3));
