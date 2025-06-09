import React from "react";
import SideNav from "./partials/SideNav";
import TopNav from "./partials/TopNav";

function Home() {
  document.title = "ShowTimez | HomePage";
  return (
    <div className="flex w-screen h-screen">
      <SideNav />
      <div className="w-[80vw] h-[100vh] ">
        <TopNav />
      </div>
    </div>
  );
}

export default Home;
