import React, { Fragment } from "react";
import ReactDOM from "react-dom/client";
import { Avenger, AvengerClass } from "./App.js";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <Fragment>
    <Avenger />
    <AvengerClass />
  </Fragment>
);
