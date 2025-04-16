const accountId = 123456;
let accountEmail = "bharat@gmail.com";
var acocuntPass = "124578";
accountloacte = "Mumbai"; // ye hm use kr sakte hai js me pr recommended nhi hai esa use krna
let accountState; //ye undefined rahega

// accountId = 875421;   //this is not allowed, we cannot assign different value to the const variable

accountEmail = "india@gmail.com";
acocuntPass = "9865230";
accountloacte = "Delhi";

console.log(accountId);

/*
Prefer not to use var 
because of issue in block scope and functional scope 
*/

console.table([
  accountId,
  accountEmail,
  acocuntPass,
  accountloacte,
  accountState,
]);
