// Función para verificar si el token es válido
async function verificarToken() {
    const token = localStorage.getItem('token');
    
    if (!token) {
        console.log('No hay token, redirigiendo a login');
        window.location.href = '/';
        return false;
    }

    try {
        const response = await fetch('/futbol/', {
            headers: {
                'Authorization': `Bearer ${token}`,
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        });

        if (response.status === 422 || response.status === 401) {
            console.log('Token inválido o expirado');
            localStorage.removeItem('token');
            window.location.href = '/';
            return false;
        }

        return true;
    } catch (error) {
        console.error('Error al verificar token:', error);
        mostrarAlerta('Error de conexión. Por favor, intente más tarde.', 'danger');
        return false;
    }
}

// Verificar el token y cargar datos al iniciar
document.addEventListener('DOMContentLoaded', async function() {
    // Mostrar indicador de carga
    mostrarSpinner(true);
    
    if (await verificarToken()) {
        await cargarPaises();
    }
    
    // Ocultar indicador de carga
    mostrarSpinner(false);
});

// Función para cargar la lista de países
async function cargarPaises() {
    try {
        if (!await verificarToken()) {
            return;
        }

        const token = localStorage.getItem('token');
        console.log('Token:', token); // Debug token

        const response = await fetch('/futbol/', {
            headers: {
                'Authorization': `Bearer ${token}`,
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        });
        
        console.log('Status:', response.status); // Debug status

        if (!response.ok) {
            if (response.status === 401 || response.status === 422) {
                console.log('Error de autenticación, redirigiendo...');
                localStorage.removeItem('token');
                window.location.href = '/';
                return;
            }
            const errorData = await response.json();
            console.error('Error response:', errorData); // Debug error
            throw new Error(errorData.error || 'Error en la respuesta del servidor');
        }

        const data = await response.json();
        console.log('Datos recibidos:', data); // Debug data
        const tablaPaises = document.getElementById('tablaPaises');
        tablaPaises.innerHTML = '';

        data.forEach(pais => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>${pais.id}</td>
                <td>${pais.nombre_pais}</td>
                <td>${pais.mundiales.map(m => m.title).join(', ')}</td>
                <td>
                    <button class="btn btn-sm btn-primary" onclick="editarPais(${pais.id})">Editar</button>
                    <button class="btn btn-sm btn-danger" onclick="eliminarPais(${pais.id})">Eliminar</button>
                    <button class="btn btn-sm btn-success" onclick="agregarMundial(${pais.id})">Añadir Mundial</button>
                </td>
            `;
            tablaPaises.appendChild(tr);
        });
    } catch (error) {
        console.error('Error:', error);
        mostrarAlerta('Error al cargar los países', 'danger');
    }
}

// Funciones de utilidad
function mostrarAlerta(mensaje, tipo) {
    // Eliminar alertas anteriores
    const alertasAnteriores = document.querySelectorAll('.alert');
    alertasAnteriores.forEach(alerta => alerta.remove());

    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${tipo} alert-dismissible fade show`;
    alertDiv.role = 'alert';
    alertDiv.innerHTML = `
        ${mensaje}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    `;

    // Insertar la alerta al principio del contenedor
    const container = document.querySelector('.container');
    container.insertBefore(alertDiv, container.firstChild);

    // Remover la alerta después de 3 segundos
    setTimeout(() => {
        if (alertDiv && alertDiv.parentNode) {
            alertDiv.remove();
        }
    }, 3000);
}

function mostrarSpinner(mostrar) {
    const spinner = document.querySelector('.spinner-container');
    if (!spinner && mostrar) {
        const spinnerHTML = `
            <div class="spinner-container position-fixed top-50 start-50 translate-middle">
                <div class="spinner-border text-primary" role="status">
                    <span class="visually-hidden">Cargando...</span>
                </div>
            </div>
        `;
        document.body.insertAdjacentHTML('beforeend', spinnerHTML);
    } else if (spinner && !mostrar) {
        spinner.remove();
    }
}

// Manejar el guardado del país
document.getElementById('formPais').addEventListener('submit', async function(e) {
    e.preventDefault(); // Prevenir el envío normal del formulario
    console.log('Iniciando guardado...');
    
    const form = e.target;
    if (!form.checkValidity()) {
        e.stopPropagation();
        form.classList.add('was-validated');
        return;
    }
    
    const token = localStorage.getItem('token');
    if (!token) {
        mostrarAlerta('No hay token de autenticación. Por favor, inicie sesión nuevamente.', 'danger');
        window.location.href = '/';
        return;
    }
    
    const paisId = document.getElementById('paisId').value;
    const nombrePais = document.getElementById('nombrePais').value;
    const mundialAnio = document.getElementById('mundialAnio').value;

    console.log('Datos del formulario:', { paisId, nombrePais, mundialAnio });

    if (!nombrePais || !mundialAnio) {
        mostrarAlerta('Por favor, complete todos los campos', 'danger');
        return;
    }

    try {
        const token = localStorage.getItem('token');
        if (!token) {
            throw new Error('No hay token de autenticación');
        }

        console.log('Guardando país...');
        // Primero creamos o actualizamos el país
        const urlPais = paisId ? `/futbol/${paisId}` : '/futbol/';
        const methodPais = paisId ? 'PUT' : 'POST';
        
        const responsePais = await fetch(urlPais, {
            method: methodPais,
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Authorization': 'Bearer ' + token
            },
            body: JSON.stringify({ nombre_pais: nombrePais })
        });

        if (!responsePais.ok) {
            const error = await responsePais.json();
            console.error('Error al guardar país:', error);
            throw new Error(error.error || 'Error al guardar el país');
        }

        const dataPais = await responsePais.json();
        console.log('País guardado:', dataPais);
        
        // Luego agregamos el mundial
        console.log('Guardando mundial...');
        const responseMundial = await fetch(`/futbol/${dataPais.id}/mundiales`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + localStorage.getItem('token')
            },
            body: JSON.stringify({ title: mundialAnio.toString() })
        });

        if (!responseMundial.ok) {
            const error = await responseMundial.json();
            console.error('Error al guardar mundial:', error);
            throw new Error(error.error || 'Error al guardar el mundial');
        }

        console.log('Mundial guardado exitosamente');
        
        // Todo salió bien
        mostrarAlerta('País y Mundial guardados exitosamente', 'success');
        
        // Cerrar el modal usando Bootstrap
        const modalElement = document.getElementById('modalPais');
        const modalInstance = bootstrap.Modal.getInstance(modalElement);
        modalInstance.hide();
        
        // Recargar la lista de países
        await cargarPaises();
        
    } catch (error) {
        console.error('Error en el proceso de guardado:', error);
        mostrarAlerta(error.message || 'Error al guardar la información', 'danger');
    }
});

// Función para editar país
async function editarPais(id) {
    try {
        if (!await verificarToken()) {
            return;
        }

        const response = await fetch(`/futbol/${id}`, {
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('token')}`,
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || 'Error al obtener los datos del país');
        }

        const pais = await response.json();
        
        document.getElementById('paisId').value = pais.id;
        document.getElementById('nombrePais').value = pais.nombre_pais;
        
        // Si el país tiene mundiales, mostramos el último
        if (pais.mundiales && pais.mundiales.length > 0) {
            document.getElementById('mundialAnio').value = pais.mundiales[pais.mundiales.length - 1].title;
        } else {
            document.getElementById('mundialAnio').value = '';
        }
        
        new bootstrap.Modal(document.getElementById('modalPais')).show();
    } catch (error) {
        console.error('Error:', error);
        mostrarAlerta('Error al cargar el país', 'danger');
    }
}

// Función para eliminar país
async function eliminarPais(id) {
    if (!confirm('¿Está seguro de eliminar este país?')) return;

    try {
        if (!await verificarToken()) {
            return;
        }

        const response = await fetch(`/futbol/${id}`, {
            method: 'DELETE',
            headers: {
                'Authorization': `Bearer ${localStorage.getItem('token')}`,
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        });

        if (response.ok) {
            mostrarAlerta('País eliminado exitosamente', 'success');
            cargarPaises();
        } else {
            const data = await response.json();
            mostrarAlerta(data.error || 'Error al eliminar el país', 'danger');
        }
    } catch (error) {
        console.error('Error:', error);
        mostrarAlerta('Error al eliminar el país', 'danger');
    }
}

// Función para añadir mundial a un país
async function agregarMundial(paisId) {
    const titulo = prompt('Ingrese el año del mundial:');
    if (!titulo) return;

    try {
        if (!await verificarToken()) {
            return;
        }

        const response = await fetch(`/futbol/${paisId}/mundiales`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            },
            body: JSON.stringify({ title: titulo })
        });

        if (response.ok) {
            mostrarAlerta('Mundial agregado exitosamente', 'success');
            cargarPaises();
        } else {
            const data = await response.json();
            mostrarAlerta(data.error || 'Error al agregar el mundial', 'danger');
        }
    } catch (error) {
        console.error('Error:', error);
        mostrarAlerta('Error al agregar el mundial', 'danger');
    }
}

// Manejar el cierre de sesión
document.getElementById('btnLogout').addEventListener('click', function() {
    localStorage.removeItem('token');
    window.location.href = '/';
});

// Limpiar el formulario al abrir el modal de nuevo país
document.querySelector('[data-bs-target="#modalPais"]').addEventListener('click', function() {
    document.getElementById('paisId').value = '';
    document.getElementById('nombrePais').value = '';
    document.getElementById('mundialAnio').value = '';
});;