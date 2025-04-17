import "./App.css";
import React, { useState, useCallback, useEffect, useRef } from "react";

function App() {
  let [length, setLength] = useState(8);
  let [numberAllowed, setNumberAllowed] = useState(false);
  let [charAllowed, setCharAllowed] = useState(false);
  let [password, setPassword] = useState("");

  //ref hook
  const passwordRef = useRef(null);

  const passwordGenerator = useCallback(() => {
    let pass = "";
    let str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    if (numberAllowed) {
      str = str + "0123456789";
    }
    if (charAllowed) {
      str = str + "!@#$%&*-{}[]_";
    }
    // let check = Math.floor(Math.random() * str.length);
    // console.log(check);

    for (let i = 1; i <= length; i++) {
      let char = Math.floor(Math.random() * str.length);
      pass = pass + str.charAt(char);
    }
    setPassword(pass);
  }, [length, numberAllowed, charAllowed, setPassword]);
  // callback k dependencies optimisation k liye kaam ata hai

  const copyToClipboard = useCallback(() => {
    passwordRef.current?.select(); // ye password ko select hote hue dikhayega
    // passwordRef.current?.setSelectionRange(0, 3); //ye particular range ko select krne k liye use hota hai
    window.navigator.clipboard.writeText(password);
  }, [password]);

  useEffect(() => {
    passwordGenerator();
  }, [length, numberAllowed, charAllowed, setPassword]);

  // useEffect ki dependencies kuch change hone pr vapas call krne k liye kaam ata hai

  return (
    <>
      <main className="h-screen w-screen flex items-start justify-center bg-black">
        <div className="flex flex-col items-center bg-gray-600 rounded-2xl mt-32 p-5 w-auto">
          <p className=" text-4xl rounded-xl min-w-auto m-1 ">
            Password Generator
          </p>

          <input
            type="text"
            value={password}
            className="mt-3 p-2 rounded-lg border border-gray-300 w-full"
            readOnly
            ref={passwordRef}
          />
          <button onClick={copyToClipboard}>Copy</button>
          <div className="flex text-sm gap-x-2">
            <div className="flex items-center gap-x-2 mt-9">
              <input
                type="range"
                min={6}
                max={15}
                value={length}
                className="cursor-pointer"
                onChange={(e) => {
                  setLength(e.target.value);
                }}
              />
              <label className="bg-black rounded p-2">Length: {length}</label>
            </div>

            <div className="flex items-center gap-x-2 mt-9">
              <input
                type="checkbox"
                defaultChecked={numberAllowed}
                id="numberInput"
                onChange={() => {
                  setNumberAllowed((prev) => !prev);
                }}
              />
              <label className="bg-black rounded p-2">Number</label>
            </div>

            <div className="flex items-center gap-x-2 mt-9">
              <input
                type="checkbox"
                defaultChecked={charAllowed}
                id="characterInput"
                onChange={() => {
                  setCharAllowed((prev) => !prev);
                }}
              />
              <label className="bg-black rounded p-2">Characters</label>
            </div>
          </div>
        </div>
      </main>
    </>
  );
}

export default App;
