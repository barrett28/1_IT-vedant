import React from "react";
import { useParams, useNavigate } from "react-router-dom";

function UserDetails() {
  const d = useParams();
  const { name } = d;
  const navigate = useNavigate();

  const goBackHandler = () => {
    navigate("/user");
  };

  return (
    <div className="w-1/2 bg-zinc-300 m-5 p-5">
      <p className="text-2xl font-semibold">this is user detail</p>
      <h1 className="mt-3 p-2 bg-red-400 w-fit">
        Current user name is <span className="font-bold">{name}</span>
      </h1>
      <button
        onClick={goBackHandler}
        className="px-2 py-1 bg-blue-500 rounded-sm mt-2"
      >
        back
      </button>
    </div>
  );
}

export default UserDetails;
