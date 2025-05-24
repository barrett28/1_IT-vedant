import React from "react";
import SideNav from "./partials/SideNav";

function Home() {
  document.title = "Movie App | HomePage";
  return (
    <div>
      <SideNav />
      <div className="w-[80vw] h-[100vh] bg-red-300">jfn</div>
    </div>
  );
}

export default Home;
