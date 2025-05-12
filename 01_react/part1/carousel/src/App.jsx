import { React, useState } from "react";
import { FaArrowRight, FaArrowLeft } from "react-icons/fa";

function App() {
  const [val, setVal] = useState(false);

  return (
    <div className="p-5 w-full h-screen bg-black flex justify-center items-center">
      <div className="w-full h-[600px] bg-blue-200 flex overflow-hidden">
        <img
          className={`shrink-0 transition-transform duration-500 ease-in-out ${
            val === false ? "-translate-x-[0%]" : "-translate-x-[100%]"
          } w-full h-full object-cover relative`}
          src="https://images.unsplash.com/photo-1506905925346-21bda4d32df4?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
          alt=""
        />
        <img
          className={`shrink-0 transition-transform duration-500 ease-in-out ${
            val === false ? "-translate-x-[0%]" : "-translate-x-[100%]"
          } w-full h-full object-cover relative`}
          src="https://images.unsplash.com/photo-1519681393784-d120267933ba?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
          alt=""
        />
        <span
          onClick={() => setVal(!val)}
          className="w-10 h-10 bg-[#dadada7b] cursor-pointer rounded-[50%] flex justify-center items-center absolute bottom-[12%] left-1/2 -translate-x-[50%] -translate-y-[50%]"
        >
          {val ? (
            <FaArrowLeft size={"1.2em"} />
          ) : (
            <FaArrowRight size={"1.2em"} />
          )}
        </span>
      </div>
    </div>
  );
}

export default App;

// ============================================

// import { React, useState } from "react";
// import { FaArrowRight, FaArrowLeft } from "react-icons/fa";

// function App() {
//   const [val, setVal] = useState(false);

//   return (
//     <div className="p-5 w-full h-[400px] bg-black flex justify-center items-center">
//       <div className="w-[90%] h-full bg-blue-200 rounded-md overflow-hidden relative">
//         {/* Sliding wrapper */}
//         <div
//           className={`flex w-[200%] h-full transition-transform duration-500 ease-in-out ${
//             val ? "-translate-x-1/2" : "translate-x-0"
//           }`}
//         >
//           <img
//             className="w-1/2 h-full object-cover"
//             src="https://images.unsplash.com/photo-1506905925346-21bda4d32df4?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
//             alt=""
//           />
//           <img
//             className="w-1/2 h-full object-cover"
//             src="https://images.unsplash.com/photo-1519681393784-d120267933ba?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
//             alt=""
//           />
//         </div>

//         {/* Button */}
//         <span
//           onClick={() => setVal(!val)}
//           className="w-10 h-10 bg-[#dadada7b] cursor-pointer rounded-full flex justify-center items-center absolute bottom-[12%] left-1/2 -translate-x-1/2 -translate-y-1/2"
//         >
//           {val ? <FaArrowLeft size="1.2em" /> : <FaArrowRight size="1.2em" />}
//         </span>
//       </div>
//     </div>
//   );
// }

// export default App;
