import React from "react";

const Render = () => {
  const fruits = [
    { name: "apple", color: "red" },
    { name: "banana", color: "yellow" },
    { name: "orange", color: "orange" },
  ];
  return (
    <div>
      {fruits.map((item, index) => (
        <ul>
          <li>
            {item.name} and the color is {<item className="color"></item>}
          </li>
        </ul>
      ))}
    </div>
  );
};

export default Render;
