import React, { useState, useEffect } from "react";

const UserList = () => {
  const [users, setUsers] = useState([]);
  const [load, setLoad] = useState(true);

  useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/users")
      .then((res) => {
        return res.json();
      })
      .then((data) => {
        setUsers(data);
        setLoad(false);
      })
      .catch((err) => console.log(err));
  }, []);

  if (load) {
    <p>laoding...</p>;
  }

  return (
    <div>
      {users.map((user) => (
        <li key={user.id}>
          name is {user.name} and corresponding is {user.email}
        </li>
      ))}
    </div>
  );
};

export default UserList;
