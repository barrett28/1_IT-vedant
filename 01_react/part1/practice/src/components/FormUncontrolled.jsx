import React, { useRef } from "react";

const FormUncontrolled = () => {
  const inputRef = useRef();
  const emailRef = useRef();

  const handleSubmit = () => {
    const name = inputRef.current.value;
    const email = emailRef.current.value;
    console.log(`Hello ${name} your email is ${email}`);
  };

  return (
    <div>
      <input type="text" ref={inputRef} placeholder="name" />
      <input type="email" ref={emailRef} placeholder="email" />
      <button onClick={handleSubmit}>submit</button>
    </div>
  );
};

export default FormUncontrolled;
