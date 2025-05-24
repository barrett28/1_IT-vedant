import React from "react";
import { Link, Routes, Route, NavLink } from "react-router-dom";
import Home from "./Components/Home";
import About from "./Components/About";
import Contact from "./Components/Contact";
import User from "./Components/User";
import UserDetails from "./Components/UserDetails";

function App() {
  return (
    <>
      <nav className="w-full h-min-[40px] bg-zinc-500 p-5 flex justify-start gap-5">
        <NavLink
          style={(e) => {
            return {
              color: e.isActive ? "pink" : "",
              fontWeight: e.isActive ? "bold" : "",
            };
          }}
          to="/"
          className="text-2xl font-semibold"
        >
          Home
        </NavLink>
        <NavLink
          style={(e) => {
            return {
              color: e.isActive ? "pink" : "",
              fontWeight: e.isActive ? "bold" : "",
            };
          }}
          to="/user"
          className="text-2xl font-semibold"
        >
          User
        </NavLink>
        <NavLink
          style={(e) => {
            return {
              color: e.isActive ? "pink" : "",
              fontWeight: e.isActive ? "bold" : "",
            };
          }}
          to="/about"
          className="text-2xl font-semibold"
        >
          About
        </NavLink>
        <NavLink
          style={(e) => {
            return {
              color: e.isActive ? "pink" : "",
              fontWeight: e.isActive ? "bold" : "",
            };
          }}
          to="/contact"
          className="text-2xl font-semibold"
        >
          Contact
        </NavLink>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/user" element={<User />}>
          <Route path="/user/:name" element={<UserDetails />} />
        </Route>
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
      </Routes>
    </>
  );
}

export default App;
