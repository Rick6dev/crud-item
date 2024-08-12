import React, { useState } from 'react';
import axios from 'axios';

const Create = () => {
    const [nombre, setNombre] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        await axios.post('http://localhost:5000/items', { nombre });
        setNombre('');
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                value={nombre}
                onChange={(e) => setNombre(e.target.value)}
                placeholder="Nombre"
                required
            />
            <button type="submit">Crear</button>
        </form>
    );
};

export default Create;
