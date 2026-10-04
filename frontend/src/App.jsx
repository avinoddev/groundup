import { useState } from 'react'

function App() {
  const [result, setResult] = useState(null)
  const [vectors, setVectors] = useState(["1, 2", "2, 4"])

  function updateVector(index, newValue) {
    const newVectors = [...vectors]
    newVectors[index] = newValue
    setVectors(newVectors)
  }

  function parseVector(text) {
    return text.split(',').map(Number)
  }

  function addVector() {
    setVectors([...vectors, "0, 0"])
  }

  async function checkBackend() {
    const parsedVectors = vectors.map(parseVector)

    const response = await fetch("http://localhost:8000/test-dependence", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ vectors: parsedVectors }),
    })

    const data = await response.json()
    setResult(data.dependence)
  }

  return (
    <div>
      {vectors.map((vector, index) => (
        <div key={index}>
          [ <input 
            value={vector} 
            onChange={(e) => updateVector(index, e.target.value)} 
          /> 
          ]
        </div>
      ))}

      <button onClick={addVector}>Add Vector</button>

      <p>Result: {result}</p>
      <button onClick={checkBackend}>Check Backend</button>
    </div>
  )
}

export default App