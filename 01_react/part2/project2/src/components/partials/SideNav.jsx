import React from "react";
import { Link } from "react-router-dom";

function SideNav() {
  return (
    <>
      <div className="w-[20vw] h-[100vh] border-r-2 border-zinc-500 p-1">
        <h1 className="text-2xl font-semibold text-white ml-2 mt-2">
          <i class="ri-tv-fill"></i>
          ShowTimez
        </h1>
        <nav className="p-5 mt-5 text-white flex flex-col gap-0.5 font-semibold">
          <h1 className="text-xl font-semibold">Timez Feed</h1>
          <Link className="hover:bg-[#6556CD] duration-300 rounded p-5">
            <i class="mr-1 ri-fire-fill"></i>
            Trending
          </Link>
          <Link className="hover:bg-[#6556CD] duration-300 rounded p-5">
            <i class="mr-2 ri-sparkling-2-fill"></i>
            Popular
          </Link>
          <Link className="hover:bg-[#6556CD] duration-300 rounded p-5">
            <i class="mr-2 ri-movie-2-line"></i>
            Movies
          </Link>
          <Link className="hover:bg-[#6556CD] duration-300 rounded p-5">
            <i class="mr-2 ri-tv-2-fill"></i>
            Tv Shows
          </Link>
          <Link className="hover:bg-[#6556CD] duration-300 rounded p-5">
            <i class="mr-2 ri-user-star-fill"></i>
            People
          </Link>
        </nav>

        <hr className="border-none h-[1px] bg-zinc-500" />

        <nav className="p-5 text-white flex flex-col gap-0.5 mb-5 font-semibold">
          <h1 className="text-xl font-semibold">Timez Info</h1>
          <Link className="hover:bg-[#6556CD] duration-300 rounded p-5 mb-0">
            <i class="mr-2 ri-information-line"></i>
            About Us
          </Link>
          <Link className="hover:bg-[#6556CD] duration-300 rounded p-5">
            <i class="mr-2 ri-phone-fill"></i>
            Contact
          </Link>
        </nav>
      </div>
    </>
  );
}

export default SideNav;
