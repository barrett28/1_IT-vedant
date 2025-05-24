import React from "react";

function Work() {
  const images = [
    {
      url: "https://thumbs.dreamstime.com/b/projects-concept-black-chalkboard-d-rendering-handwritten-top-view-office-desk-lot-business-office-supplies-79906734.jpg",
      top: "50%",
      left: "50%",
      isActive: true,
    },
    {
      url: "https://thumbs.dreamstime.com/b/projects-concept-black-chalkboard-d-rendering-handwritten-top-view-office-desk-lot-business-office-supplies-79906734.jpg",
      top: "56%",
      left: "56%",
      isActive: false,
    },
    {
      url: "https://thumbs.dreamstime.com/b/projects-concept-black-chalkboard-d-rendering-handwritten-top-view-office-desk-lot-business-office-supplies-79906734.jpg",
      top: "47%",
      left: "43%",
      isActive: true,
    },
    {
      url: "https://thumbs.dreamstime.com/b/projects-concept-black-chalkboard-d-rendering-handwritten-top-view-office-desk-lot-business-office-supplies-79906734.jpg",
      top: "55%",
      left: "49%",
      isActive: false,
    },
    {
      url: "https://thumbs.dreamstime.com/b/projects-concept-black-chalkboard-d-rendering-handwritten-top-view-office-desk-lot-business-office-supplies-79906734.jpg",
      top: "50%",
      left: "52%",
      isActive: false,
    },
    {
      url: "https://thumbs.dreamstime.com/b/projects-concept-black-chalkboard-d-rendering-handwritten-top-view-office-desk-lot-business-office-supplies-79906734.jpg",
      top: "55%",
      left: "53",
      isActive: false,
    },
  ];

  return (
    <div className="w-full">
      <div className="max-w-screen-xl mx-auto text-center">
        <h1 className=" relative text-[30vw] leading-none tracking-tight font-medium ">
          Work
        </h1>
        <div>
          {images.map(
            (elem, index) =>
              elem.isActive && (
                <img
                  className="absolute w-52 rounded-lg -translate-x-[50%] -translate-y-[50%]"
                  src={elem.url}
                  style={{ top: elem.top, left: elem.left }}
                  alt=""
                />
              )
          )}
        </div>
      </div>
    </div>
  );
}

export default Work;
