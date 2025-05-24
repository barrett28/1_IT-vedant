import React from "react";
import Card from "./Card";

function Cards() {
  return (
    <div className="w-[90%] h-[40vh] bg-zinc-200 p-5 overflow-y-auto flex gap-5 flex-wrap">
      <Card />
    </div>
  );
}

export default Cards;
