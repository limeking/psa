import React, { useEffect, useState } from 'react';


function App() {
  const [ping, setPing] = useState("");

  useEffect(() => {
    fetch("/api/ping")
      .then((response) => response.json())
      .then((data) => setPing(data.msg))
      .catch(() => setPing("error"));
    }, []);

    return (
      <div>
        <h1>Ping Test</h1>
        <p>Result: {ping}</p>
      </div>
    );
}

export default App;