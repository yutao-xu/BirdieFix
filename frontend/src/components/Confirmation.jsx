import { useNavigate } from "react-router-dom";

function Confirmation() {
    const navigate = useNavigate();
    return (
        <>
            <h1>Confirmation</h1>
            <h2>String: {window.racketString}</h2>
            <h2>Tension: {window.tension}</h2>
            <h2>Phone Number: {window.phoneNumber}</h2>
            <button onClick={() => navigate("/phonenumber")}>Back</button>
            <button onClick={() => navigate("/")}>Checkout</button>
        </>
    )
}

export default Confirmation;