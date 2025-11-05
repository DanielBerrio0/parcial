import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Navbar from './components/Common/Navbar';
import Login from './components/Auth/Login';
import Register from './components/Auth/Register';
import Alert from './components/Common/Alert';
import { AuthProvider } from './context/AuthContext';

const App = () => {
  return (
    <AuthProvider>
      <Router>
        <Navbar />
        <Alert />
        <Switch>
          <Route path="/login" component={Login} />
          <Route path="/register" component={Register} />
          <Route path="/" exact>
            <h1>Bienvenido a la aplicación</h1>
            <p>Por favor, regístrate o inicia sesión.</p>
          </Route>
        </Switch>
      </Router>
    </AuthProvider>
  );
};

export default App;