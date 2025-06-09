import { useState, useEffect, useContext } from "react";
import { useParams } from "react-router-dom";
import { CoinContext } from "../context/coinContext";
import LineChart from "../components/LineChart";

const Coin = () => {
  const { coinId } = useParams();
  const { currency } = useContext(CoinContext);
  const [coinData, setCoinData] = useState(null);
  const [chartData, setChartData] = useState(null);

  const fetchCoinData = async () => {
    const options = {
      headers: {
        accept: "application/json",
        "x-cg-demo-api-key": "CG-TZdmpxZpYSQyMs74RhYeAdUy",
      },
    };

    try {
      const res = await fetch(
        `https://api.coingecko.com/api/v3/coins/${coinId}`,
        options
      );
      const data = await res.json();
      setCoinData(data);
    } catch (err) {
      console.error(err);
    }
  };

  const fetchChartData = async () => {
    const options = {
      headers: {
        accept: "application/json",
        "x-cg-demo-api-key": "CG-TZdmpxZpYSQyMs74RhYeAdUy",
      },
    };

    try {
      const res = await fetch(
        `https://api.coingecko.com/api/v3/coins/${coinId}/market_chart?vs_currency=${currency.name}&days=10&interval=daily`,
        options
      );
      const data = await res.json();
      setChartData(data);
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    fetchCoinData();
    fetchChartData();
  }, [currency]);

  if (!coinData || !chartData) {
    return <p>Loading...</p>;
  }

  return (
    <div className="w-[900px] mx-auto mt-[100px] pb-10">
      <div className="coin-name flex flex-col justify-center items-center">
        <img
          className="w-[30%]"
          src={coinData.image.large}
          alt={coinData.name}
        />
        <p className="mb-10">
          <b>
            {coinData.name} - {coinData.symbol.toUpperCase()}
          </b>
        </p>
      </div>
      <div className="chart">
        <LineChart chartData={chartData} />
      </div>
      <div className="coinInfo w-[600px] mx-auto mt-[80px]">
        <ul className="flex justify-between items-center p-3 hover:bg-zinc-500 font-semibold border-b-[1px] border-zinc-400">
          <li>Market Rank:</li>
          <li>{coinData.market_cap_rank}</li>
        </ul>
        <ul className="flex justify-between items-center p-3 hover:bg-zinc-500 font-semibold border-b-[1px] border-zinc-400">
          <li>Current price: </li>
          <li>
            {currency.currency}{" "}
            {coinData.market_data.current_price[currency.name].toLocaleString()}
          </li>
        </ul>
        <ul className="flex justify-between items-center p-3 hover:bg-zinc-500 font-semibold border-b-[1px] border-zinc-400">
          <li>Market Cap: </li>
          <li>
            {currency.currency}{" "}
            {coinData.market_data.market_cap[currency.name].toLocaleString()}
          </li>
        </ul>
      </div>
    </div>
  );
};

export default Coin;
