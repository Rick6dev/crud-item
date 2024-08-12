import React from 'react';
import Create from './components/Create';
import Read from './components/Read';

const App = () => {
    return (
        <div>
            <h1>CRUD con Flask y MariaDB</h1>
            <Create />
            <Read />
        </div>
    );
};

export default App;
