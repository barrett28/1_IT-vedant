import { React, useState, useEffect } from "react";
import axios from "../utils/axios";

function Show() {
  const [product, setProduct] = useState([]);

  const getProducts = () => {
    // const api = "https://fakestoreapi.com/products";

    axios
      .get("/products")
      .then((product) => {
        // console.log(product);
        setProduct(product.data);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  useEffect(() => {
    getProducts();
  }, []);

  return (
    <div className="m-[50px]">
      <ul className="mt-10">
        {product.length > 0
          ? product.map((items, index) => (
              <li key={index} className="w-fit px-3 py-2 bg-red-300 m-2">
                {items.title}
              </li>
            ))
          : "Loading..."}
      </ul>
    </div>
  );
}

export default Show;
