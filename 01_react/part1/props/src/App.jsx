import React from "react";
import Card from "./Components/Card";

function App() {
  const data = [
    {
      name: "vedant",
      profession: "Artist",
      image:
        "https://images.unsplash.com/photo-1592046285097-6cdf4daf0d69?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    },
    {
      name: "Jasmin",
      profession: "Doctor",
      image:
        "https://images.unsplash.com/photo-1439402702863-6434b61e6392?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    },
    {
      name: "Bharat",
      profession: "Engineer",
      image:
        "https://images.unsplash.com/photo-1568602471122-7832951cc4c5?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    },
    {
      name: "Priya",
      profession: "Teacher",
      image:
        "https://images.unsplash.com/photo-1484627147104-f5197bcd6651?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    },
  ];

  return (
    <div className="w-full h-screen bg-black flex justify-center items-center gap-5">
      {data.map((item, index) => (
        <Card key={index} values={item} />
      ))}
    </div>
  );
}

export default App;
