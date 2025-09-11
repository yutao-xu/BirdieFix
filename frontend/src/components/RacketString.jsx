import { useNavigate } from "react-router-dom";

function RacketString() {
    const navigate = useNavigate();
    return (
        <>
            <h1>Select A String</h1>
            <button onClick={() => navigate("/")}>Back</button>
            <button onClick={() => navigate("/tension")}>Next</button>
        </>
    )
}

export default RacketString;