import React from "react";
import Button from "./Button";

function Navbar() {
  return (
    <div className="max-w-screen-lg mx-auto py-4 flex items-center justify-between gap-10 border-b-[1px] border-zinc-700">
      <div className="flex items-center">
        <img
          className="image h-[50px] w-fit"
          src="https://cdn.prod.website-files.com/6552fa0e9db1071c9d279ba9/6654005f64b18d1eaa48cf60_Refokus.png"
          alt=""
        />
        <h3>Refokus</h3>

        <div className="links flex gap-14 ml-20">
          {["Home", "Work", "Culture"].map((elem, index) => (
            <a key={index} className="flex items-center gap-1" href="#">
              {index === 1 && (
                <span
                  style={{ boxShadow: " 0 0 0.25em #fff" }}
                  className="inline-block w-2 h-2 rounded-full bg-green-500"
                ></span>
              )}

              {elem}
            </a>
          ))}
        </div>
      </div>

      <Button />
    </div>
  );
}

export default Navbar;
