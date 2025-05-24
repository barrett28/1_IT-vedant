import React from "react";
import { useForm } from "react-hook-form";

function ReactHookForm() {
  const { register, handleSubmit } = useForm();

  return (
    <>
      <hr />
      <h4 className="m-[50px]">forms using react form hook</h4>
      <form
        className="m-[50px]"
        action=""
        onSubmit={handleSubmit((data) => {
          console.log(data);
        })}
      >
        <input {...register("name")} type="text" placeholder="name" />
        <input {...register("email")} type="email" placeholder="email" />
        <input type="submit" />
      </form>
    </>
  );
}

export default ReactHookForm;
