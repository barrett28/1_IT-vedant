import { useState, useEffect } from "react";

export function usePower() {
  const [power, setPower] = useState(100);

  const incPower = () => {
    setPower(power + 1);
  };

  return {
    power,
    incPower,
  };
}
