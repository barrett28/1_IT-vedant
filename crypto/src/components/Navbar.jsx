import { React, useContext } from "react";
import logo from "../assets/logo.png";
import { Link } from "react-router-dom";
import { CoinContext } from "../context/coinContext";

const Navbar = () => {
  const { setCurrency } = useContext(CoinContext);

  const currencyHandler = (event) => {
    switch (event.target.value) {
      case "usd": {
        setCurrency({ name: "usd", currency: "$" });
        break;
      }
      case "inr": {
        setCurrency({ name: "inr", currency: "₹" });
        break;
      }
      case "eur": {
        setCurrency({ name: "eur", currency: "€" });
        break;
      }
      default: {
        setCurrency({ name: "usd", currency: "$" });
        break;
      }
    }
  };

  return (
    <>
      <div className="w-full min-h-[10vh] flex justify-around items-center p-5 border-b-[1px] border-zinc-400">
        <img className="max-w-[8%] h-auto" src={logo} alt="" />

        <ul className="flex justify-between items-center gap-10 ">
          <Link to="/">Home</Link>
          <li>About</li>
          <li>Contact</li>
          {/* <li>Blog</li> */}
        </ul>

        <select
          onChange={currencyHandler}
          name=""
          id=""
          className="bg-transparent p-1.5 rounded"
        >
          <option className="bg-[#09005C]" value="usd">
            USD
          </option>
          <option className="bg-[#09005C]" value="inr">
            INR
          </option>
          <option className="bg-[#09005C]" value="eur">
            EUR
          </option>
        </select>

        {/* <button className="px-3 py-1.5 bg-amber-700 rounded cursor-pointer">
          SignUp <i class="ri-arrow-right-up-line"></i>
        </button> */}
      </div>
    </>
  );
};

export default Navbar;
