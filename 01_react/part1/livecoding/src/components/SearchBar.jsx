import React, { useState } from "react";

const SearchBar = ({ items }) => {
  const [search, setSearch] = useState("");

  const refinedSearch = items.filter((item) =>
    item.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div>
      <p>Search Bar</p>
      <div>
        <input
          className="w-50 p-1"
          type="text"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          placeholder="search any fruit...."
        />

        <ul className="text-dark fw-bold">
          {refinedSearch.map((item, index) => (
            <li key={index}>{item}</li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default SearchBar;
