import { useNavigate } from "react-router-dom";

function Confirmation() {
    const navigate = useNavigate();
    return (
        <>
            <h1>Confirmation</h1>
            <button onClick={() => navigate("/phonenumber")}>Back</button>
            <button onClick={() => navigate("/")}>Next</button>
        </>
    )
}

export default Confirmation;