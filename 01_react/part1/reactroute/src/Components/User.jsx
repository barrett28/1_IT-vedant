import React from "react";
import { Link, Outlet } from "react-router-dom";

function User() {
  return (
    <>
      <div className="w-1/2 bg-zinc-300 m-5 p-5">
        <h1 className="text-2xl">Welcome to Home Page</h1>
        <div className="mt-5">
          <Link
            to="/user/john"
            className=" bg-orange-500 text-black w-fit px-2 py-1 rounded-sm"
          >
            John
          </Link>
          <br />
          <br />
          <Link
            to="/user/vedant"
            className=" bg-orange-500 text-black w-fit px-2 py-1 rounded-sm"
          >
            Vedant
          </Link>
          <br />
          <br />
          <Link
            to="/user/kumar"
            className=" bg-orange-500 text-black w-fit px-2 py-1 rounded-sm"
          >
            Kumar
          </Link>
        </div>
      </div>
      <hr />
      <Outlet />
    </>
  );
}

export default User;
