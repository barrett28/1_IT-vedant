import { usePower } from "./Shield.jsx";

function ShieldPass() {
  const pow = usePower();
  return (
    <>
      <h1>power: {pow.power}</h1>
      <button onClick={pow.incPower}>increase power</button>
    </>
  );
}

export default ShieldPass;
