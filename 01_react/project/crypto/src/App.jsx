import React from "react";
import Navbar from "./components/Navbar";
import Home from "./components/Home";
import About from "./components/About";
import Contact from "./components/Contact";
import Coin from "./components/Coin";
import Footer from "./components/Footer";
import { Routes, Route, NavLink } from "react-router-dom";

const App = () => {
  return (
    <div className="min-h-[100vh] bg-gradient-to-b from-[#0b004e] via-[#1d152f] to-[#002834] w-full text-white">
      <Navbar />

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
        <Route path="/coin/:coinId" element={<Coin />} />
      </Routes>

      <Footer />
    </div>
  );
};

export default App;
