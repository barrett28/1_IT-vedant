import React from "react";

function Cards() {
  const data = [
    {
      image:
        "https://images.unsplash.com/photo-1633174524827-db00a6b7bc74?q=80&w=2096&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
      name: "Amazon",
      description:
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed semperposuere mi, id elementum massa ullamcorper non.",
      instock: true,
    },
    {
      image:
        "https://images.unsplash.com/photo-1654573817889-296cad084c97?q=80&w=2062&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
      name: "flipkart",
      description:
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed semperposuere mi, id elementum massa ullamcorper non.",
      instock: true,
    },
    {
      image:
        "https://images.unsplash.com/photo-1611262588024-d12430b98920?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
      name: "instagram",
      description:
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed semperposuere mi, id elementum massa ullamcorper non.",
      instock: false,
    },
  ];

  return (
    <div className="w-full h-screen flex justify-center items-center gap-5 bg-neutral-400">
      {data.map((elem, index) => (
        <div
          key={index}
          className="w-[220px] min-h-[300px] bg-zinc-100 rounded flex flex-col justify-between items-center"
        >
          <div className="image h-[20%] ">
            <img src={elem.image} alt="amazon-image" />
          </div>
          <div>
            <h1 className="p-2 text-left text-xl font-bold mt-1">
              {elem.name}
            </h1>
            <p className=" leading-tight text-gray-900 p-2">
              {elem.description}
            </p>
            <div className="p-2">
              <button
                className={`px-2 py-1 rounded ${
                  elem.instock ? "bg-blue-500" : "bg-red-500 text-amber-50"
                } text-sm`}
              >
                {elem.instock ? "In stock" : "Out of stock"}
              </button>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
}

export default Cards;
