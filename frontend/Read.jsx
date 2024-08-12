import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Read = () => {
    const [items, setItems] = useState([]);

    useEffect(() => {
        const fetchItems = async () => {
            const response = await axios.get('http://localhost:5000/items');
            setItems(response.data);
        };
        fetchItems();
    }, []);

    return (
        <ul>
            {items.map(item => (
                <li key={item.id}>{item.nombre}</li>
            ))}
        </ul>
    );
};

export default Read;
