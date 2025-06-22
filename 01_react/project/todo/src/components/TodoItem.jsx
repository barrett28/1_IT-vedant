import React from "react";
import { useDispatch } from "react-redux";
import { toggleTodo, deleteTodo } from "../features/todos/todoSlice";

const TodoItem = ({ todo }) => {
  const dispatch = useDispatch();

  return (
    <div className="flex items-center justify-between bg-zinc-600 p-3 rounded shadow mb-2">
      <span
        className={`cursor-pointer text-lg ${
          todo.completed ? "line-through text-gray-500" : ""
        }`}
        onClick={() => dispatch(toggleTodo(todo.id))}
      >
        {todo.text}
      </span>
      <button
        onClick={() => dispatch(deleteTodo(todo.id))}
        className="text-red-500 hover:text-red-700"
      >
        ❌
      </button>
    </div>
  );
};

export default TodoItem;
