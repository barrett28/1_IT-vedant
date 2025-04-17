// primitive -> which cannot be changed/ immuted

// 7types -> string , number, boolean, null, undefined, symbol, bigint

let v = 22.3; // it will also be treated as integer
// in js there is nothing like decimal it will be considered as integer

console.log(typeof v);

let bigInt = 5545415451452155142421512n;
// the "n" in last represent the bigint
console.log(typeof bigInt);

//  non-primitive -> which can be muted (non primitive ka type return karenge tho object hi ayega)

// types-> array, objects , fucntions

let arrayVar = ["vedant", "aura", "jcb"];

const objVar = {
  name: "vdeant",
  age: 25,
  location: "kalyan",
};

function avenger() {
  console.log("steve rogers");
}

// function ka type return karenge tho object fucntion ayega

avenger();

// =========================stack asd heap ===============

/*  stack-->(primitive) and Heap-->(non-primitive)

In Stack a copy will be created and changes are done to that copy 
In Heap a reference is given that means changes will happen to the original value 
*/

let a = "vedant";
let b = a;
b = "it";

console.log("a", a);
console.log("b", b);

// this is stack copy values changed for primitive

let userOne = {
  name: "vedant",
  mail: "vedant@gmail.com",
};

let userTwo = userOne;

userTwo.name = "it";

console.log("userone", userOne);
console.log("usertwo", userTwo);

// in the heap original value changes due to of heap memory and its reference to data (no copy created)
