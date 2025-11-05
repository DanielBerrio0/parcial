document.getElementById('loginForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const username = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const errorMessage = document.getElementById('error-message');

    try {
        const response = await fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });

        const data = await response.json();

        if (response.ok) {
            localStorage.setItem('token', data.token);
            window.location.href = '/dashboard';
        } else {
            errorMessage.textContent = data.message || 'Usuario no encontrado. Por favor regístrese.';
            errorMessage.classList.remove('hidden');
        }
    } catch (error) {
        errorMessage.textContent = 'Error de conexión';
        errorMessage.classList.remove('hidden');
    }
});