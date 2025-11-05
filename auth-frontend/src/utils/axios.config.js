import axios from 'axios';

const axiosInstance = axios.create({
    baseURL: 'http://localhost:5000/api', // Cambia esto a la URL de tu API
    timeout: 10000, // Tiempo de espera de 10 segundos
});

// Interceptor para manejar errores
axiosInstance.interceptors.response.use(
    response => response,
    error => {
        // Manejo de errores global
        if (error.response) {
            // El servidor respondió con un código de estado fuera del rango de 2xx
            console.error('Error en la respuesta:', error.response.data);
        } else if (error.request) {
            // La solicitud fue realizada pero no se recibió respuesta
            console.error('Error en la solicitud:', error.request);
        } else {
            // Algo sucedió al configurar la solicitud
            console.error('Error:', error.message);
        }
        return Promise.reject(error);
    }
);

export default axiosInstance;