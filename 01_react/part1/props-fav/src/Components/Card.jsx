import React from "react";

function Card({ values, handleClick, index }) {
  const { image, name, artist, added } = values;
  return (
    <div className="w-60 bg-zinc-200 p-4 rounded-md flex justify-around items-center gap-5 relative pb-8">
      <div className="w-20 h-20 bg-orange-200">
        <img src={image} alt="" />
      </div>
      <div>
        <h3 className="text-xl font-semibold">{name}</h3>
        <p className="text-gray-600">{artist}</p>
      </div>
      <button
        onClick={() => handleClick(index)}
        className={`px-2 py-1 ${
          added ? "bg-emerald-600" : "bg-orange-500"
        } cursor-pointer whitespace-nowrap rounded-2xl text-white absolute bottom-0 left-1/2 -translate-x-[50%] translate-y-[50%]`}
      >
        {added === false ? "Add to Favorites" : "Added"}
      </button>
    </div>
  );
}

export default Card;
