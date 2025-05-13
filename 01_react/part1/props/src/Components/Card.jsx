import { React, useState } from "react";

function Card({ values, handleClick, index }) {
  const { name, profession, image, isFriend } = values;
  const [fol, setFol] = useState(false);

  return (
    <div className="w-40 bg-white rounded-md overflow-hidden">
      <div className="w-40 h-32 bg-zinc-200">
        <img src={image} className="w-full h-full object-cover" />
      </div>
      <div className="text-left p-2">
        <h3 className="text-2xl mb-1 font-semibold">{name}</h3>
        <p className="font-semibold mb-1">{profession}</p>
        <button
          onClick={() => handleClick(index)}
          className={`px-2 py-1 ${
            isFriend ? "bg-red-500 text-white" : "bg-blue-500"
          } text-white rounded-md`}
        >
          {isFriend ? "Unfollow" : "Follow"}
        </button>
      </div>
    </div>
  );
  // return (
  //   <div className="w-40 bg-white rounded-md overflow-hidden">
  //     <div className="w-40 h-32 bg-zinc-200">
  //       <img src={image} className="w-full h-full object-cover" />
  //     </div>
  //     <div className="text-left p-2">
  //       <h3 className="text-2xl mb-1 font-semibold">{name}</h3>
  //       <p className="font-semibold mb-1">{profession}</p>
  //       <button
  //         onClick={() => {
  //           setFol((prev) => !prev);
  //           alert(`You have ${fol ? "Unfollowed" : "Followed"} ${name}`);
  //         }}
  //         className={`px-2 py-1 ${
  //           fol ? "bg-red-500 text-white" : "bg-blue-500"
  //         } text-white rounded-md`}
  //       >
  //         {fol ? "Unfollow" : "Follow"}
  //       </button>
  //     </div>
  //   </div>
  // );
}

export default Card;
