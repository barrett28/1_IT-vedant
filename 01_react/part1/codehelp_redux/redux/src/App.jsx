import { React, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import {
  increment,
  decrement,
  incrementByAmount,
  reset,
  decrementByAmount,
} from "./features/counter/counterSlice";

const App = () => {
  const [amount, setAmount] = useState("");
  const [decAmount, setDecAmount] = useState("");
  const count = useSelector((state) => state.counter.value);
  const dispatch = useDispatch();

  const handleIncrement = () => {
    dispatch(increment());
  };
  const handleDecrement = () => {
    dispatch(decrement());
  };
  const handleReset = () => {
    dispatch(reset());
  };
  const handleIncByAmount = () => {
    dispatch(incrementByAmount(amount));
  };

  const handleDecByAmount = () => {
    dispatch(decrementByAmount(decAmount));
  };

  return (
    <div className="w-full h-screen bg-zinc-800 text-white flex justify-center items-center">
      <div className="main text-center ">
        <button
          className="px-3 py-1 mb-5 rounded-sm border-2 text-3xl cursor-pointer hover:bg-zinc-100 hover:text-black"
          onClick={handleIncrement}
        >
          +
        </button>
        <h1 className="text-4xl font-semibold">Count: {count} </h1>
        <button
          className="px-4 py-1 mt-5 rounded-sm border-2 text-3xl cursor-pointer hover:bg-zinc-100 hover:text-black"
          onClick={handleDecrement}
        >
          -
        </button>
        <br />
        <button
          className="px-4 py-1 mt-5 rounded-sm border-2 text-3xl cursor-pointer hover:bg-zinc-100 hover:text-black"
          onClick={handleReset}
        >
          Reset
        </button>
        <br />
        <br />

        <div className="flex gap-10 justify-center items-center ">
          <h1>increment by</h1>
          <input
            className="border-[1px] border-zinc-600 p-2 text-[1.3vw]"
            type="number"
            placeholder="enter number"
            value={amount}
            onChange={(e) => setAmount(e.target.value)}
          />
          <button
            onClick={handleIncByAmount}
            className="px-3 py-1 rounded-sm border-2 text-3xl cursor-pointer hover:bg-zinc-100 hover:text-black"
          >
            enter
          </button>
        </div>
        <div className="flex gap-10 justify-center items-center ">
          <h1>decrement by</h1>
          <input
            className="border-[1px] border-zinc-600 p-2 text-[1.3vw]"
            type="number"
            placeholder="enter number"
            value={decAmount}
            onChange={(e) => setDecAmount(e.target.value)}
          />
          <button
            onClick={handleDecByAmount}
            className="px-3 py-1 rounded-sm border-2 text-3xl cursor-pointer hover:bg-zinc-100 hover:text-black"
          >
            enter
          </button>
        </div>
      </div>
    </div>
  );
};

export default App;
