import React from "react";
import AddTodo from "./components/AddTodo";
import TodoList from "./components/TodoList";

const App = () => {
  return (
    <div className="min-h-screen bg-zinc-800 text-white flex flex-col items-center justify-start pt-20">
      <h1 className="text-4xl font-bold mb-10">📝 Todo Redux App</h1>
      <AddTodo />
      <TodoList />
    </div>
  );
};

export default App;
