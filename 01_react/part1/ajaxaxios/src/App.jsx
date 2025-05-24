import { React, useState } from "react";
import axios from "axios";
import Home from "./Components/Home";
import Show from "./Components/Show";
import Services from "./Components/Services";
import { Link, Routes, Route } from "react-router-dom";

function App() {
  return (
    <>
      <div className="w-1/4 bg-zinc-300 p-4 flex justify-start ml-13 items-center gap-5">
        <Link to="/">Home</Link>
        <Link to="/show">Show</Link>
        <Link to="/services">Services</Link>
      </div>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/show" element={<Show />} />
        <Route path="/services" element={<Services />} />
      </Routes>
    </>
  );
}

export default App;
