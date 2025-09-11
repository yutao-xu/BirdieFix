import { useNavigate } from "react-router-dom";

function Tension() {
    const navigate = useNavigate();

    const updateValue = value => {
        window.tension = value;
    }

    return (
        <>
            <h1>Select A Tension</h1>
            <select onChange={choice => updateValue(choice.target.value)}>
                <option value="25">25</option>
                <option value="26">26</option>
                <option value="27">27</option>
                <option value="28">28</option>
                <option value="29">29</option>
            </select>
            <br />
            <br />
            <button onClick={() => navigate("/racketstring")}>Back</button>
            <button onClick={() => navigate("/phonenumber")}>Next</button>
        </>
    )
}

export default Tension;