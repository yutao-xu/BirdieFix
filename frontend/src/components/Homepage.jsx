import { useNavigate } from "react-router-dom";


const Homepage = () => {
    const navigate = useNavigate();

    return (
        <>
            <h1>Birdie Fix</h1>
            <button className="homepage" onClick={() => navigate("/pickup")}>Pickup</button>{' '}
            <button className="homepage" onClick={() => navigate("/racketstring")}>Dropoff</button>
        </>
    )
}

export default Homepage;