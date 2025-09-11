import { useNavigate } from "react-router-dom";

function PhoneNumber() {
    const navigate = useNavigate();
    return (
        <>
            <h1>Enter Your Phone Number</h1>
            <button onClick={() => navigate("/tension")}>Back</button>
            <button onClick={() => navigate("/confirmation")}>Next</button>
        </>
    )
}

export default PhoneNumber;