import { createSlice } from "@reduxjs/toolkit";

export const counterSlice = createSlice({
  name: "counter",
  initialState: {
    value: 0,
  },
  reducers: {
    increment: (state) => {
      state.value += 1;
      //   console.log(state.value);
    },

    reset: (state) => {
      state.value = 0;
    },

    decrement: (state) => {
      state.value -= 1;
      //   console.log(state.value);
    },

    incrementByAmount: (state, action) => {
      state.value += Number(action.payload);
    },

    decrementByAmount: (state, action) => {
      state.value -= Number(action.payload);
    },
  },
});

export const {
  increment,
  decrement,
  incrementByAmount,
  reset,
  decrementByAmount,
} = counterSlice.actions;

export default counterSlice.reducer;
