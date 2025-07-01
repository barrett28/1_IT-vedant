import React, { useContext } from "react";
import { useNavigate } from "react-router-dom";
import UserContext from "../context/UserContext";

const Contact = () => {
  const { name, roll } = useContext(UserContext);

  const navigate = useNavigate();
  const back = () => {
    navigate("/");
  };

  return (
    <div>
      <p>Contact</p>
      <button onClick={back}>Back</button>
      <p>
        name is {name}, having a roll no of {roll}
      </p>
    </div>
  );
};

export default Contact;
