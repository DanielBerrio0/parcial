import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import authService from '../../services/auth.service';
import Alert from '../Common/Alert';

const Register = () => {
    const [formData, setFormData] = useState({
        username: '',
        email: '',
        password: ''
    });
    const [error, setError] = useState('');
    const [success, setSuccess] = useState('');
    const history = useHistory();

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');
        setSuccess('');

        try {
            await authService.register(formData);
            setSuccess('Registro exitoso. Redirigiendo a inicio de sesión...');
            setTimeout(() => {
                history.push('/login');
            }, 2000);
        } catch (err) {
            setError(err.response.data.message || 'Error en el registro. Inténtalo de nuevo.');
        }
    };

    return (
        <div>
            <h2>Registro</h2>
            {error && <Alert message={error} type="error" />}
            {success && <Alert message={success} type="success" />}
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Nombre de usuario:</label>
                    <input
                        type="text"
                        name="username"
                        value={formData.username}
                        onChange={handleChange}
                        required
                    />
                </div>
                <div>
                    <label>Correo electrónico:</label>
                    <input
                        type="email"
                        name="email"
                        value={formData.email}
                        onChange={handleChange}
                        required
                    />
                </div>
                <div>
                    <label>Contraseña:</label>
                    <input
                        type="password"
                        name="password"
                        value={formData.password}
                        onChange={handleChange}
                        required
                    />
                </div>
                <button type="submit">Registrarse</button>
            </form>
        </div>
    );
};

export default Register;