import React from "react";

function Reuse() {
  const reuse = ["it", "vedant", "project", "components"];

  return (
    <div>
      {reuse.map((value, index) => (
        <div
          key={value}
          className="px-2 py-1 bg-blue-300 rounded-md w-fit m-5 text-2xl"
        >
          {value}
        </div>
      ))}
    </div>
  );
}

export default Reuse;
