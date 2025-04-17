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

array2.unshift(11); // unshift adds a element at start of list
console.log(array2);
