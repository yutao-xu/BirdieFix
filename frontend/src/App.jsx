import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Homepage from './components/Homepage'
import Tension from './components/tension'
import RacketString from './components/RacketString'
import PhoneNumber from './components/PhoneNumber'
import Confirmation from './components/Confirmation'

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Homepage />} />
        <Route path="/racketstring" element={<RacketString />} />
        <Route path="/tension" element={<Tension />} />
        <Route path="/phonenumber" element={<PhoneNumber />} />
        <Route path="/confirmation" element={<Confirmation />} />
      </Routes>
    </Router>
  );
}

export default App