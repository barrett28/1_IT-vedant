import React from "react";
import Navbar from "./components/Navbar";
import Work from "./components/Work";
import Stripe from "./components/Stripe";

function App() {
  return (
    <div className="w-full h-screen bg-zinc-900 text-white">
      <Navbar />
      <Work />
      <Stripe />
    </div>
  );
}

export default App;
