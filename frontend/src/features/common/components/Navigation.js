import React from "react";
import { Link } from 'react-router-dom'

export default function Navigation() {
    return(<>
    <div>
        <ul>
            <li><Link to="/home">Home</Link></li>
            <li><Link to="/history">history</Link></li>
        </ul>
    </div>
    </>)
}