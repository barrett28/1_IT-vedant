import React, { Component } from "react";

export function Avenger(props) {
  return <h1>My name is {props.first_name} -function</h1>;
}
// export function Header() {
//   return <h1>Header </h1>;
// }

export class AvengerClass extends Component {
  render() {
    return <h1>My name is {this.props.heroic_name} -class </h1>;
  }
}
