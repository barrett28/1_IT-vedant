import { React, useState } from "react";
import { TodoProvider } from "./context";

const App = () => {
  const [todos, setTodos] = useState([]);

  const addTodo = () => {};
  const deleteTodo = () => {};
  const updateTodo = () => {};
  const toggleComplete = () => {};

  return (
    <TodoProvider
      value={{ todos, addTodo, deleteTodo, updateTodo, toggleComplete }}
    >
      <div className="w-full h-screen bg-zinc-900 text-white p-[8%]">
        <div className="w-[800px] bg-zinc-700 mx-auto rounded-lg">
          <h1 className="text-start mt-5 p-3 text-2xl">Manage your todos...</h1>
        </div>
      </div>
    </TodoProvider>
  );
};

export default App;
