import React from "react";
import Cards from "./Components/Cards";
import Forms from "./Components/Forms";

function App() {
  return (
    <>
      <div className="w-full h-screen bg-zinc-500 flex justify-center items-center">
        <div className="container mx-auto">
          <Cards />
          <Forms />
        </div>
      </div>
    </>
  );
}

export default App;
