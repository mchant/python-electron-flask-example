import logo from "./logo.svg";
import "./App.css";
import axios from "axios";
import React, { useState, useEffect } from "react";

function App() {
  const [retval, setRetVal] = useState(null);
  const [computerName, setComputerName] = useState(null);
  useEffect(() => {
    axios.get("http://localhost:5000/todos/sample").then((res) => {
      // debugger;
      setRetVal(res.data.buy);
    });
    axios
      .get("http://localhost:5000/todos/computer_name", {
        params: { item: "computer_name" },
      })
      .then((res) => {
        // debugger;
        setComputerName(res.data);
      });
  });

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React {retval}
        </a>
        <div>{computerName}</div>
      </header>
    </div>
  );
}

export default App;
