// console.log(null);

f = "3ab";
t = Number(f);
// console.log(typeof t);
// console.log("value", t);

/*
if we compare the null with 0 then js will automatically convert that null in 0
so if we check (null > 0) answer will be false 
or (null = 0) answer will be true  
*/

console.log(null > 0);
// in this while comparing js will change null to 0 then 0>0 is flase

console.log(null == 0);
// in this "==" loose equality, js will take "null == undefined"✅, but not "null == 0"❌ or "undefined == 0"❌

console.log(null >= 0);
// here again it will covert the null to zero and then 0>=0 will be true

console.log(undefined == null);
// this will be true , because in loose equality undefined will be equal to null

// ---------------------------------

// "==="

console.log("2" === 2);
/*
== it will convert the string to number and check but 
=== it wont convert and check both i.e datatype and the value if both are true then true
*/

console.log("2" > 1);
console.log("1" > 1);
