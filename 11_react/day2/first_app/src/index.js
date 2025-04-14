import React, { Fragment } from "react";
import ReactDOM from "react-dom/client";
import { Avenger, aven, AvengerClass } from "./App";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <Fragment>
    {aven}
    <Avenger />
    <AvengerClass />
  </Fragment>
);
