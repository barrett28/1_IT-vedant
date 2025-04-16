import { useState } from "react";

function App() {
  let [counter, setCounter] = useState(15);

  // let counter = 15;

  let addValue = () => {
    // console.log("button clicked", Math.random());
    counter = counter + 1;
    setCounter(counter);
    console.log("counter:", counter);
  };

  let removeValue = () => {
    counter = counter - 1;
    setCounter(counter);
  };

  return (
    <>
      {/* <h2>hello vite</h2> */}
      <h2>Counter value is: {counter}</h2>
      <button onClick={addValue}>Increase {counter}</button> <br />
      <button onClick={removeValue}>decrease{counter}</button>
    </>
  );
}

export default App;
