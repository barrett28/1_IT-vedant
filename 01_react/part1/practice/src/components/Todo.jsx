import React, { useState } from "react";

const Todo = () => {
  const [tasks, setTasks] = useState([
    { id: 1, text: "Buy milk" },
    { id: 2, text: "Read book" },
    { id: 3, text: "Practice React" },
  ]);

  const handleDelete = (id) => {
    setTasks(tasks.filter((task) => task.id !== id));
  };

  return (
    <div>
      <p style={{ marginBottom: "20px" }}>My Task</p>
      <ul>
        {tasks.map((item) => (
          <li key={item.id}>
            {item.text}{" "}
            <button onClick={() => handleDelete(item.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Todo;
