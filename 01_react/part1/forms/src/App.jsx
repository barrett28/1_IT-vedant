import { React, useRef } from "react";

function App() {
  // using useRef

  const name = useRef(null);
  const age = useRef(null);
  const email = useRef(null);

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(name.current.value, age.current.value, email.current.value);
  };

  return (
    <>
      <h1 className="m-[50px]">Form using useRef</h1>
      <form className="m-[50px]" action="" onSubmit={handleSubmit}>
        <input
          className="border-2"
          type="text"
          name=""
          id=""
          ref={name}
          placeholder="enter name"
        />{" "}
        <br /> <br />
        <input
          className="border-2"
          type="number"
          name=""
          id=""
          ref={age}
          placeholder="enter age"
        />{" "}
        <br /> <br />
        <input
          className="border-2"
          type="email"
          name=""
          id=""
          ref={email}
          placeholder="enter email"
        />{" "}
        <br /> <br />
        <input type="submit" />
      </form>
    </>
  );
}

export default App;
