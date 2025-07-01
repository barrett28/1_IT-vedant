import React, { useState } from "react";

const Form = () => {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");

  const onSubmit = () => {
    console.log(name, email);
  };

  return (
    <div>
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="enter name"
      />
      <input
        type="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        placeholder="enter email"
      />
      <button onClick={onSubmit}>Submit</button>
    </div>
  );
};

export default Form;
