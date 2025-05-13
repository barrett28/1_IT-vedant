import React from "react";

function Navbar({ navsend }) {
  return (
    <div className="w-full px-15 py-3 flex justify-between items-center gap-10 bg-teal-200">
      <h3 className="font-bold text-black text-2xl">Add To Fav Exercise</h3>
      <div className="flex justify-center items-center bg-orange-700 text-white px-2 py-1 rounded-md gap-2">
        <h3>Favourites</h3>
        <h4>{navsend.filter((item) => item.added).length}</h4>
      </div>
    </div>
  );
}

export default Navbar;
