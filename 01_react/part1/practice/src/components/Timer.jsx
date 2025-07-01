import React, { useState, useEffect } from "react";

const Timer = () => {
  const [time, setTime] = useState(0);

  const handleReset = () => {
    setTime(0);
  };

  useEffect(() => {
    const timer = setInterval(() => {
      setTime((prev) => prev + 1);
    }, 1000);
    return () => clearInterval(timer);
  }, []);

  return (
    <div>
      <p>timer: {time} </p>

      <button onClick={handleReset}>Reset</button>
    </div>
  );
};

export default Timer;
