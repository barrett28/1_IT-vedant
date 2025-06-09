import { useState, useEffect } from "react";
import Chart from "react-google-charts";

const LineChart = ({ chartData }) => {
  const [data, setData] = useState([["Date", "Prices"]]);

  useEffect(() => {
    let dataCopy = [["Date", "Prices"]];
    if (chartData?.prices) {
      chartData.prices.forEach((item) => {
        dataCopy.push([new Date(item[0]).toLocaleDateString(), item[1]]);
      });
      setData(dataCopy);
    }
  }, [chartData]);

  return (
    <div>
      <Chart
        chartType="LineChart"
        height="100%"
        width="100%"
        data={data}
        legendToggle
      />
    </div>
  );
};

export default LineChart;
