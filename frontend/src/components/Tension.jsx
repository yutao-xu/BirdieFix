import { useNavigate } from "react-router-dom";

function Tension() {
    const navigate = useNavigate();
    return (
        <>
            <h1>Select A Tension</h1>
            <button onClick={() => navigate("/racketstring")}>Back</button>
            <button onClick={() => navigate("/phonenumber")}>Next</button>
        </>
    )
}

export default Tension;