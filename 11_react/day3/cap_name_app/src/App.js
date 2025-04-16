import { Avenger, AvengerClass, AvengerState, AvengerStateCon } from "./Shield";
import React, { Fragment } from "react";

function Shield() {
  return (
    <Fragment>
      <Avenger first_name="steve roge" />
      <AvengerClass heroic_name="Captain America" />
      <AvengerState heroic_name="Dupinder" />
      <AvengerStateCon heroic_name="captain" />
    </Fragment>
  );
}
export default Shield;
