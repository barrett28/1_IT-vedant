import { React, useState, useEffect, useContext } from "react";
import { CoinContext } from "../context/coinContext";
import { Link } from "react-router-dom";

const Home = () => {
  const { allCoin, currency } = useContext(CoinContext);
  const [displayCoin, setDisplayCoin] = useState([]);
  const [input, setInput] = useState("");

  const inputHandler = (event) => {
    setInput(event.target.value);
    if (event.target.value === "") {
      setDisplayCoin(allCoin);
    }
  };

  const submitHandler = async (event) => {
    event.preventDefault();
    const coins = await allCoin.filter((items) => {
      return items.name.toLowerCase().includes(input.toLowerCase());
    });
    setDisplayCoin(coins);
  };

  useEffect(() => {
    setDisplayCoin(allCoin);
  }, [allCoin]);

  return (
    <div className="px-[10px] pb-[50px]">
      <div className="max-w-[700px] text-center mt-[80px] mb-[80px] mx-auto flex flex-col justify-center items-center gap-10">
        <h1 className="text-[max(4vw,36px)] font-bold">
          Stay Ahead in the Crypto Game
        </h1>
        <p className="w-[75%] text-shadow-white font-semibold leading-5 pb-5">
          Discover live prices insights for <br /> Bitcoin, Ethereum, and many
          more coins.
        </p>
        <form
          className="p-[8px] w-[80%] bg-zinc-600 text-white rounded-[5px] flex justify-between items-center gap-5"
          onSubmit={submitHandler}
        >
          <input
            className="flex-1 outline-none p-2 border-none text-[16px] font-semibold"
            type="text"
            name=""
            id=""
            placeholder="Search Crypto..."
            onChange={inputHandler}
            required
            list="coinsList"
          />

          <datalist id="coinsList">
            {allCoin.map((item, index) => (
              <option key={index} value={item.name} />
            ))}
          </datalist>

          <button className="px-3 py-2 bg-amber-700 rounded" type="submit">
            Search
          </button>
        </form>
      </div>

      <div className="w-[800px] mx-auto bg-gradient-to-r from-[#252047] via-[#290a71] to-[#010535]">
        <div className="tableLayout grid grid-cols-[0.5fr_2fr_1fr_1fr_1.5fr] px-[20px] py-[15px] items-center border-b-[1px] border-[#c3c3c3c]">
          <p>#</p>
          <p>Coin</p>
          <p>Price</p>
          <p className="text-end">24H Change</p>
          <p className="text-end">Market Cap</p>
        </div>
        {displayCoin.slice(0, 10).map((item, index) => (
          <Link
            to={`/coin/${item.id}`}
            className="grid grid-cols-[0.5fr_2fr_1fr_1fr_1.5fr] px-[20px] py-[15px] items-center border-b border-[#c3c3c3]"
            key={index}
          >
            <p>{item.market_cap_rank}</p>
            <div className="flex justify-start gap-5 items-center">
              <img className="w-[15%]" src={item.image} alt="" />
              <p>{item.name + " - " + item.symbol}</p>
            </div>
            <p>
              {currency.currency} {item.current_price.toLocaleString()}
            </p>
            <p
              className={`text-center ${
                item.price_change_percentage_24h > 0
                  ? "text-green-500"
                  : "text-red-500"
              }`}
            >
              {Math.floor(item.price_change_percentage_24h * 100) / 100}
            </p>
            <p className="text-end">
              {currency.currency}
              {item.market_cap.toLocaleString()}
            </p>
          </Link>
        ))}
      </div>
    </div>
  );
};

export default Home;
