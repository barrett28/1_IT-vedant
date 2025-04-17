// array

const array1 = new Array(1, 2, 3, 4, 5);
// console.log(array1);

//another method

const array2 = [2, 5, 4, 7, 8, 9];
// console.log(array2);

//shallow copy and Deep copy
/*
while making shallow copy the intial object will also be get updated (because it share the same point references) like heap
and while making Deep copy the initial object will not get updated
*/

//array methods

// array2.push(12);  //push
// array2.push(13);
// console.log(array2);

// array2.pop();  //pop
// console.log(array2);

// array2.unshift(11); // unshift adds a element at start of list
// console.log(array2);

// array2.shift(); // remove the first element

// console.log(array2);

// console.log(array2.includes(3)); // bool value return hoti hai, include hai ya nhi ye pata chalta hai

// console.log(array2.indexOf(3)); // kis position pr hai vo element vo position ko return karta hai, agar vo element nhi hai tho "-1" return karega

// const newArr = array2.join();  // join array ko string me return krta hai
// console.log(newArr);
// console.log(typeof newArr);

// slice and splice

// const slicearr = array2.slice(1, 3);
// console.log("slice", slicearr); // substring ya ek section return krta hai

const splicearr = array2.splice(1, 3); // 1. main array object ko change kr dega, 2. 1st and last element ko bhi include krta hai
console.log("splice", splicearr);
console.log("array2", array2);
