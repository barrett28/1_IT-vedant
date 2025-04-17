import { useState, useEffect } from "react";

function App() {
  const [name, setname] = useState("steve rogers");
  const [power, setPower] = useState(100);
  const [willPower, setWillPower] = useState(100);

  const incPower = () => {
    setPower(power + 1);
  };
  const decPower = () => {
    setWillPower(willPower - 1);
  };

  useEffect(() => {
    console.log("use effect Called");

    return () => {
      console.log("unmount is called ");
    };
  });

  return (
    <>
      {/* <h1>hero, {name}</h1> */}
      <h1>Heropower : {power}</h1>
      <button onClick={incPower}>change name</button>

      <h1>Willianpower : {willPower}</h1>
      <button onClick={decPower}>change name</button>
    </>
  );
}

export default App;
