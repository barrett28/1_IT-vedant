import React, { useState } from "react";

const Home = ({ props }) => {
  const [click, setClick] = useState(true);

  const handleClick = () => {
    setClick((prev) => !prev);
  };

  return (
    <div>
      <button onClick={handleClick}>Click me</button>
      <p>{click ? "you liked it" : "you disliked it"}</p>
      <p>
        {props.name} having a role of {props.role}
      </p>
    </div>
  );
};

export default Home;
