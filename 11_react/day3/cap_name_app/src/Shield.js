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
export class AvengerState extends Component {
  state = {
    name: "Justin Singh",
    heroic_name: this.props.heroic_name,
  };
  render() {
    return <h1>My heroic name is {this.state.heroic_name} </h1>;
  }
}
export class AvengerStateCon extends Component {
  constructor(props) {
    super(props);
    this.state = {
      arid: 1,
      name: "Steve Rog",
      heroic_name: this.props.heroic_name,
    };
  }

  changeHeroName = () => {
    this.setState({
      name: "Scott Lang",
    });
  };

  show_arid = (arid) => {
    console.log(arid);
  };

  send_arid = () => {
    this.show_arid(this.state.arid);
  };

  render() {
    return (
      <>
        <h1>
          My name is {this.state.name} and my heroic name is{" "}
          {this.state.heroic_name}
        </h1>
        <button onClick={this.changeHeroName}>Change</button>
        <button onClick={this.send_arid}>arid</button>
      </>
    );
  }
}
