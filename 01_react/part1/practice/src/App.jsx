import React from "react";
import Home from "./components/Home";
import About from "./components/About";
import Contact from "./components/Contact";
import Form from "./components/Form";
import Render from "./components/Render";
import Todo from "./components/Todo";
import Pagi from "./components/Pagi";
import Timer from "./components/Timer";
import UserList from "./components/UserList";
import { Routes, Route, NavLink } from "react-router-dom";
import UserContext from "./context/UserContext";
import FormUncontrolled from "./components/FormUncontrolled";

const App = () => {
  const user = { name: "xyz", roll: 45, div: "classA" };

  return (
    <UserContext.Provider value={user}>
      <nav style={{ display: "flex", gap: "20px" }}>
        <NavLink to="/">Home</NavLink>
        <NavLink to="/about">About</NavLink>
        <NavLink to="/contact">contact</NavLink>
        <NavLink to="/timer">Timer</NavLink>
      </nav>

      <Routes>
        <Route
          path="/"
          element={<Home props={{ name: "xyz", role: "software dev" }} />}
        />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
        <Route path="/timer" element={<Timer />} />
      </Routes>
      <hr />
      <hr />

      {/* <Form /> */}
      {/* <FormUncontrolled /> */}

      {/* <Render /> */}
      {/* <Todo /> */}
      {/* <UserList /> */}
      <Pagi />
    </UserContext.Provider>
  );
};

export default App;
