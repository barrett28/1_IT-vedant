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
    <div className="px-4 pb-[50px]">
      <div className="max-w-[700px] text-center mt-[60px] mb-[60px] mx-auto flex flex-col justify-center items-center gap-6 px-2">
        <h1 className="text-[max(6vw,28px)] font-bold leading-tight">
          Stay Ahead in the Crypto Game
        </h1>
        <p className="w-[90%] text-shadow-white font-semibold leading-5 pb-3 text-[14px] sm:text-[16px]">
          Discover live prices insights for Bitcoin, Ethereum, and many more
          coins.
        </p>

        {/* Search Bar */}
        <form
          className="w-full sm:w-[80%] flex flex-col sm:flex-row justify-between items-center gap-3 sm:gap-5 bg-zinc-600 text-white p-3 rounded-md"
          onSubmit={submitHandler}
        >
          <input
            className="w-full flex-1 outline-none p-2 border-none text-[16px] font-semibold rounded-sm"
            type="text"
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
          <button
            className="px-4 py-2 bg-amber-700 rounded w-full sm:w-auto"
            type="submit"
          >
            Search
          </button>
        </form>
      </div>

      {/* Table Headers */}
      <div className="w-full overflow-x-auto">
        <div className="min-w-[700px] max-w-[1000px] mx-auto bg-gradient-to-r from-[#252047] via-[#290a71] to-[#010535] rounded-md shadow-md">
          <div className="grid grid-cols-[0.5fr_2fr_1fr_1fr_1.5fr] px-5 py-4 text-white font-semibold text-[14px] sm:text-[16px] border-b border-[#c3c3c3]">
            <p>#</p>
            <p>Coin</p>
            <p>Price</p>
            <p className="text-end">24H Change</p>
            <p className="text-end">Market Cap</p>
          </div>

          {/* Coin List */}
          {displayCoin.slice(0, 10).map((item, index) => (
            <Link
              to={`/coin/${item.id}`}
              className="grid grid-cols-[0.5fr_2fr_1fr_1fr_1.5fr] px-5 py-4 items-center text-white text-[14px] sm:text-[16px] border-b border-[#c3c3c3] hover:bg-[#1c1c3a] transition"
              key={index}
            >
              <p>{item.market_cap_rank}</p>
              <div className="flex items-center gap-3">
                <img
                  className="w-[25px] sm:w-[35px]"
                  src={item.image}
                  alt={item.name}
                />
                <p>{item.name + " - " + item.symbol}</p>
              </div>
              <p>
                {currency.currency} {item.current_price.toLocaleString()}
              </p>
              <p
                className={`text-end ${
                  item.price_change_percentage_24h > 0
                    ? "text-green-500"
                    : "text-red-500"
                }`}
              >
                {Math.floor(item.price_change_percentage_24h * 100) / 100}%
              </p>
              <p className="text-end">
                {currency.currency} {item.market_cap.toLocaleString()}
              </p>
            </Link>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Home;
