// ye get k liye tha

// async function getData() {
//   let response = await fetch("https://jsonplaceholder.typicode.com/todos/2");
//   let data = await response.json();
//   console.log(data);
// }

// getData();

//post ------

const myHeader = new Headers();
myHeader.append("Content-Type", "application/json");

const url = "https://jsonplaceholder.typicode.com/posts";

const options = {
  method: "POST",
  body: JSON.stringify({ username: "xyz" }),
  headers: myHeader,
};

async function getData() {
  let response = await fetch(url, options);
  let data = await response.json();
  console.log(data);
}

getData();
