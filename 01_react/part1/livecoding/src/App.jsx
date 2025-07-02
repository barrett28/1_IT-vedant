import React from "react";
import SearchBar from "./components/SearchBar";

const App = () => {
  const items = [
    "car",
    "bike",
    "cycle",
    "Apple",
    "Juice",
    "mango",
    "pineApple",
    "watermelon",
    "toy",
    "game",
  ];

  return (
    <div>
      <SearchBar items={items} />
    </div>
  );
};

export default App;
