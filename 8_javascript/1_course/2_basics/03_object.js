// object literals

const mySym = Symbol("key1");

const jsuser = {
  name: "vedant",
  [mySym]: Symbol("mykey"),
  age: 22,
  location: "kalyan",
  email: "abc@gmail.com",
  isLoggedIn: false,
};

console.log(jsuser.email);
console.log(jsuser["email"]);
console.log(jsuser[mySym]);
console.log(typeof jsuser[mySym]);

// we can free the object so no more changes can be done
Object.freeze(jsuser);

jsuser["name"] = "karan"; // it wont change because of the freeze
// console.log(jsuser["name"]);

//function

jsuser.greeting = function () {
  console.log(`hello users ${this.name}`);
};
console.log(jsuser.greeting);
