import { React, useState } from "react";
import { Link } from "react-router-dom";

function TopNav() {
  const [query, setQuery] = useState("");
  console.log(query);

  return (
    <div className="w-full h-[10vh] flex justify-start ml-[20%] items-center gap-2 relative">
      <i class="text-3xl text-white ri-search-line"></i>
      <input
        onChange={(e) => setQuery(e.target.value)}
        value={query}
        className="w-[50%] p-2 ml-2 text-white outline-none border-none"
        placeholder="Search here..."
        type="text"
        name=""
        id=""
      />
      {query.length > 0 && (
        <i
          onClick={() => setQuery("")}
          class=" text-white text-2xl ri-close-line"
        ></i>
      )}

      <div className="absolute w-[50%] max-h-[60vh] top-[90%] overflow-auto">
        {/* <Link className="bg-zinc-700 text-white w-[100%] p-10 hover:bg-zinc-500 font-semibold flex justify-start items-center">
          <img src="" alt="" />
          <span>Hello</span>
        </Link> */}
      </div>
    </div>
  );
}

export default TopNav;
