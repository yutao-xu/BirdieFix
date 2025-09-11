import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  return (
    <>
      <button onClick={() => console.log("hi")}>
        Pickup
      </button>
      <button onClick={() => console.log("hi")}>
        Dropoff
      </button>
    </>
  )
}

export default App
