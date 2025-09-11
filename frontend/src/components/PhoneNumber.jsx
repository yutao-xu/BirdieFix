import { useNavigate } from "react-router-dom";

function PhoneNumber() {
    const navigate = useNavigate();

    const updateValue = value => {
        window.phoneNumber = value;
    }

    return (
        <>
            <h1>Enter Your Phone Number</h1>
            <input type="text" onChange={choice => updateValue(choice.target.value)} />
            <br />
            <br />
            <button onClick={() => navigate("/tension")}>Back</button>
            <button onClick={() => navigate("/confirmation")}>Next</button>
        </>
    )
}

export default PhoneNumber;