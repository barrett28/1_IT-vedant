import { React, useState } from "react";

function Controlled() {
  // using hooks -> useState to manage real time value

  const [val, setVal] = useState({ name: "", email: "" });

  const handleConSubmit = (event) => {
    event.preventDefault();
    console.log(val);
  };

  return (
    <>
      <hr />
      <h4 className="m-[50px]">Using useState -- controlled components</h4>
      <form className="m-[50px]" action="" onSubmit={handleConSubmit}>
        <input
          className="border-2 border-gray-400 p-1"
          onChange={(event) => {
            console.log(event.target.value),
              setVal({ ...val, name: event.target.value });
          }}
          type="text"
          name=""
          id=""
          placeholder="name"
        />
        <input
          className="border-2 border-gray-400 p-1"
          onChange={(event) => {
            console.log(event.target.value),
              setVal({ ...val, email: event.target.value });
          }}
          type="email"
          name=""
          id=""
          placeholder="email"
        />
        <input type="submit" />
      </form>
    </>
  );
}

export default Controlled;
