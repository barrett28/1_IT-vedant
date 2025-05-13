import { React, useState } from "react";
import Card from "./Components/Card";
import Navbar from "./Components/Navbar";

function App() {
  const data = [
    {
      image:
        "https://i1.sndcdn.com/artworks-Eke4dWZTIrXCkXPW-hX2ihg-t500x500.jpg",
      name: "Blinding Lights",
      artist: "Weeknd",
      added: false,
    },
    {
      image:
        "https://a10.gaanacdn.com/gn_img/albums/w4MKPObojg/4MKPGkYObo/size_m.jpg",
      name: "Levitating",
      artist: "Dua Lipa",
      added: false,
    },
    {
      image:
        "https://upload.wikimedia.org/wikipedia/en/b/b4/Shape_Of_You_%28Official_Single_Cover%29_by_Ed_Sheeran.png",
      name: "Shape of You",
      artist: "Ed Sheeran",
      added: true,
    },
    {
      image:
        "https://i1.sndcdn.com/artworks-boUvTeTEft8V0b2G-8spb0A-t500x500.jpg",
      name: "Peaches",
      artist: "Justin Bieber",
      added: false,
    },
  ];

  const [val, setVal] = useState(data);

  const handleClick = (checkIndex) => {
    setVal((prev) => {
      return prev.map((item, index) => {
        if (index === checkIndex) return { ...item, added: !item.added };
        return item;
      });
    });
  };

  return (
    <div>
      <Navbar navsend={val} />
      <div className="flex justify-center items-center gap-10 flex-wrap mt-[70px]">
        {val.map((item, index) => {
          return (
            <Card
              key={index}
              values={item}
              index={index}
              handleClick={handleClick}
            />
          );
        })}
      </div>
    </div>
  );
}

export default App;
