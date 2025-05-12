import React from "react";

function Music() {
  const data = [
    {
      name: "Lo-Fi Chill",
      description:
        "Relaxing lo-fi beats perfect for studying, reading, or winding down.",
    },
    {
      name: "Hip-Hop Vibes",
      description:
        "A curated collection of smooth beats and lyrical hip-hop tracks.",
    },
    {
      name: "Acoustic Mornings",
      description:
        "Gentle acoustic tunes to start your morning with calm and focus.",
    },
  ];

  const handleDownload = (elem) => {
    alert("Download started. Please wait a moment. :)");
  };

  return (
    <div className="w-full h-screen bg-violet-300 flex flex-col items-center justify-center gap-5">
      {data.map((elem, index) => (
        <div key={index} className="w-100 bg-zinc-200 px-3 py-2 rounded-sm">
          <h1 className="text-2xl font-bold mb-2">{elem.name}</h1>
          <p className="mb-3">{elem.description}</p>
          <button
            onClick={handleDownload}
            className="bg-blue-500 text-white font-bold hover:bg-blue-700 px-3 py-2 rounded "
          >
            Download
          </button>
        </div>
      ))}
    </div>
  );
}

export default Music;
