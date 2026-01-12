import { useNavigate } from "react-router-dom";
import axios from "axios";

function Confirmation() {
    const navigate = useNavigate();
    const checkout = () => {
        const racket = {
            "tension": window.tension,
            "racketString": window.racketString,
            "phoneNumber": window.phoneNumber
        };

        axios.post("https://api.birdiefix.com/rackets/dropoff", racket)
        .then(response => {
            const data = response.data;
            console.log(data)
        })
        navigate("/")
    }
    
    return (
        <>
            <h1>Confirmation</h1>
            <h2>String: {window.racketString}</h2>
            <h2>Tension: {window.tension}</h2>
            <h2>Phone Number: {window.phoneNumber}</h2>
            <button onClick={() => navigate("/phonenumber")}>Back</button>
            <button onClick={() => checkout()}>Checkout</button>
        </>
    )
}

export default Confirmation;