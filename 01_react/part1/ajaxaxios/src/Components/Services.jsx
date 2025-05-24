import { React, useEffect, useState } from "react";
import axios from "../utils/axios";

function Services() {
  const [first, setFirst] = useState("this is first data");
  const [second, setSecond] = useState("this is Second data");

  const [user, setUser] = useState([]);

  const fetchUser = () => {
    axios
      .get("/users")
      .then((user) => {
        console.log(user.data);
        setUser(user.data);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  useEffect(() => {
    fetchUser();
  }, []);

  //   useEffect(() => {
  //     fetchUser();
  //   }, []);

  //   useEffect(() => {
  //     console.log("Services component mounted");

  //     return () => {
  //       console.log("Services component unmounted");
  //     };
  //   }, [second]);

  return (
    <>
      <div className="mt-10 ml-12 bg-red-300 w-1/4 p-5">
        <h1>Welcome to service Page</h1>
        <p>This is the service page.</p>
      </div>
      <div className="mt-10 ml-12 bg-red-300 w-1/4 p-5">
        <h1>{first}</h1>
        <button
          onClick={() => {
            setFirst("second data changed");
          }}
          className="px-2 py-1 bg-blue-400 rounded"
        >
          button one
        </button>
        <br />
        <br />
        <h1>{second}</h1>
        <button
          onClick={() => {
            setSecond("first data changed");
          }}
          className="px-2 py-1 bg-blue-400 rounded"
        >
          button two
        </button>
        <br />
        <hr />
      </div>

      <ul>
        {user.length > 0
          ? user.map((items, index) => (
              <li key={index} className="w-fit px-3 py-2 bg-red-300 m-2">
                {items.name.firstname}
              </li>
            ))
          : "Loading..."}
      </ul>
    </>
  );
}

export default Services;
