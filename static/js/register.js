document.getElementById('registerForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const username = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirm-password').value;
    const errorMessage = document.getElementById('error-message');

    if (password !== confirmPassword) {
        errorMessage.textContent = 'Las contraseñas no coinciden';
        errorMessage.classList.remove('hidden');
        return;
    }

    try {
        const response = await fetch('/registry', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });

        const data = await response.json();

        if (response.ok) {
            window.location.href = '/';  // Redirige al login
        } else {
            errorMessage.textContent = data.message || 'Error en el registro';
            errorMessage.classList.remove('hidden');
        }
    } catch (error) {
        errorMessage.textContent = 'Error de conexión';
        errorMessage.classList.remove('hidden');
    }
});