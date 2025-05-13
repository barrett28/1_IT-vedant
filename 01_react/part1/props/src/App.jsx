import { React, useState } from "react";
import Card from "./Components/Card";

function App() {
  const raw = [
    {
      name: "vedant",
      profession: "Artist",
      image:
        "https://images.unsplash.com/photo-1592046285097-6cdf4daf0d69?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
      isFriend: false,
    },
    {
      name: "Jasmin",
      profession: "Doctor",
      image:
        "https://images.unsplash.com/photo-1439402702863-6434b61e6392?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
      isFriend: false,
    },
    {
      name: "Bharat",
      profession: "Engineer",
      image:
        "https://images.unsplash.com/photo-1568602471122-7832951cc4c5?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
      isFriend: false,
    },
    {
      name: "Priya",
      profession: "Teacher",
      image:
        "https://images.unsplash.com/photo-1484627147104-f5197bcd6651?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
      isFriend: false,
    },
  ];

  const [data, setData] = useState(raw);

  const handleClick = (changingIndex) => {
    setData((previous) => {
      return previous.map((item, index) => {
        if (index === changingIndex)
          return { ...item, isFriend: !item.isFriend };
        return item;
      });
    });
  };

  // return (
  //   <div className="w-full h-screen bg-black flex justify-center items-center gap-5">
  //     {data.map((item, index) => (
  //       <Card key={index} values={item} />
  //     ))}
  //   </div>
  // );

  return (
    <div className="w-full h-screen bg-black flex justify-center flex-wrap items-center gap-5">
      {data.map((item, index) => (
        <Card
          key={index}
          values={item}
          handleClick={handleClick}
          index={index}
        />
      ))}
    </div>
  );
}

export default App;
