import { React, useState } from "react";

function App() {
  const [score, setScore] = useState(100);
  const [banned, setBanned] = useState(false);
  const [val, setVal] = useState(20);
  const [con, setCon] = useState({
    name: "vedant",
    age: 22,
    city: "bangalore",
    isBanned: false,
  });
  const [arr, setArr] = useState([1, 2, 3, 4, 5]);

  const changeSetScore = () => {
    setScore(score + 100);
  };

  const changeSetScoreNeg = () => {
    setScore(score - 100);
  };

  return (
    <div className="p-5">
      <h1>Current Score is: {score}</h1>
      <button
        onClick={changeSetScore}
        className="px-2 py-1 bg-blue-500 text-white rounded-full mt-2"
      >
        Change the state +
      </button>
      <button
        onClick={changeSetScoreNeg}
        className="px-2 py-1 bg-blue-500 text-white rounded-full mt-2"
      >
        Change the state -
      </button>
      <br />
      <br />
      <h1>{banned.toString()}</h1>
      <button
        onClick={() => setBanned((prev) => !prev)}
        className="px-2 py-1 bg-blue-500 text-white rounded-2xl"
      >
        Ban karo
      </button>
      <br />
      <br />
      <h1>{val}</h1>
      <button
        onClick={() => setVal((prev) => prev + 1)}
        className="px-2 py-1 bg-blue-500 text-white rounded-2xl"
      >
        Ban karo
      </button>
      <br />
      <br />
      <br />
      <h1>Name: {con.name}</h1>
      <h1>Age: {con.age}</h1>
      <h1>City: {con.city}</h1>
      <h1>isBanned: {con.isBanned.toString()}</h1>
      <br />
      <button
        onClick={() => setCon({ ...con, isBanned: !con.isBanned })}
        className={`px-2 py-1 ${
          con.isBanned ? "bg-blue-500" : "bg-red-500"
        } text-white rounded-2xl`}
      >
        Change
      </button>
      <br />
      <br />

      {arr.map((item) => (
        <h1>{item}</h1>
      ))}

      <button
        onClick={() =>
          setArr(() => arr.filter((item, index) => index != val.length - 1))
        }
        className="px-2 py-1 bg-blue-500 text-white rounded-2xl"
      >
        click
      </button>
    </div>
  );
}

export default App;
