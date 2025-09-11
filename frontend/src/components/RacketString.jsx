import { useNavigate } from "react-router-dom";


function RacketString() {
    const navigate = useNavigate();

    const updateValue = value => {
        window.racketString = value;
    }

    return (
        <>
            <h1>Select A String</h1>
            <select onChange={choice => updateValue(choice.target.value)}>
                <option value="bg65">BG 65</option>
                <option value="bg66">BG 66</option>
                <option value="bg80">BG 80</option>
                <option value="nanogy">Nanogy</option>
                <option value="aerobite">Aerobite</option>
            </select>
            <br />
            <br />
            <button onClick={() => navigate("/")}>Back</button>
            <button onClick={() => navigate("/tension")}>Next</button>
        </>
    )
}

export default RacketString;