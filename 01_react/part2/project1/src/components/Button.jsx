import React from "react";
import { BsArrowReturnRight } from "react-icons/bs";

function Button() {
  return (
    <div className="w-40 px-3 py-2 rounded-full text-black bg-zinc-300 flex items-center justify-center gap-5">
      Get Started
      <span className="mt-1">
        <BsArrowReturnRight />
      </span>
    </div>
  );
}

export default Button;
