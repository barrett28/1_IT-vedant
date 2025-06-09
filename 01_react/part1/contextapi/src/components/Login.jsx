import { React, useState, useContext } from "react";
import UserContext from "../context/UserContext";

const Login = () => {
  const [userName, setUserName] = useState("");
  const [pass, setPass] = useState("");

  const { setUser } = useContext(UserContext);

  const handleSubmit = (e) => {
    e.preventDefault();
    setUser({ userName, pass });
    console.log(userName, pass);
  };

  return (
    <div>
      <h1>Login here</h1>

      <input
        type="text"
        name=""
        id=""
        value={userName}
        onChange={(e) => setUserName(e.target.value)}
        placeholder="enter name"
      />
      <input
        type="text"
        name=""
        id=""
        value={pass}
        onChange={(e) => setPass(e.target.value)}
        placeholder="enter Pass"
      />

      <button onClick={handleSubmit}>Submit</button>
    </div>
  );
};

export default Login;
