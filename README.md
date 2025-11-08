# Backend API - Sistema de Autenticación y Gestión

Este proyecto implementa una API REST desarrollada en Flask para gestionar selecciones nacionales de fútbol, mundiales, y un sistema completo de autenticación de usuarios.

## 🚀 Despliegue

El backend está desplegado en Railway y accesible en:
```
https://[tu-proyecto]-production.up.railway.app
```

## 📋 Endpoints Disponibles

### Autenticación

#### Login
```http
POST /login
Content-Type: application/json

{
  "username": "usuario@example.com",
  "password": "contraseña"
}
```

**Respuesta exitosa:**
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

#### Registro
```http
POST /registry
Content-Type: application/json

{
  "username": "usuario@example.com",
  "password": "contraseña"
}
```

**Respuesta exitosa:**
```json
{
  "id": 1,
  "username": "usuario@example.com"
}
```

### Usuarios

#### Listar todos los usuarios (requiere autenticación)
```http
GET /users
Authorization: Bearer {token}
```

#### Obtener usuario por ID
```http
GET /users/{id}
```

#### Actualizar usuario
```http
PUT /users/{id}
Content-Type: application/json

{
  "username": "nuevo_usuario@example.com",
  "password": "nueva_contraseña"
}
```

#### Eliminar usuario
```http
DELETE /users/{id}
```

### Fútbol
```http
GET /futbol
```
Endpoints para gestión de selecciones nacionales y mundiales.

## 🛠️ Tecnologías

- Flask 2.3+
- Flask-SQLAlchemy
- Flask-JWT-Extended
- Flask-CORS
- Gunicorn (para producción)
- SQLite (desarrollo) / MySQL (producción opcional)

## 🔧 Instalación Local

1. Clonar el repositorio:
```bash
git clone https://github.com/DanielBerrio0/parcial.git
cd parcial
```

2. Crear entorno virtual e instalar dependencias:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Ejecutar la aplicación:
```bash
python app.py
```

El servidor estará disponible en `http://localhost:5000`

## 🌐 CORS

El backend tiene CORS habilitado para permitir peticiones desde cualquier origen. Ideal para consumir la API desde un frontend en otro repositorio.

## 📝 Variables de Entorno

- `JWT_SECRET_KEY`: Clave secreta para JWT (opcional, usa un valor por defecto)
- `MYSQL_URI`: URI de conexión a MySQL (opcional, usa SQLite por defecto)
- `PORT`: Puerto del servidor (por defecto 5000)

## 📦 Estructura del Proyecto

```
├── app.py                 # Aplicación principal
├── config/               # Configuraciones
│   ├── config.py
│   ├── database.py
│   └── jwt.py
├── controllers/          # Controladores/Rutas
│   ├── futbol_controller.py
│   └── users_controllers.py
├── models/              # Modelos de datos
│   ├── futbol_model.py
│   └── users_model.py
├── repository/          # Capa de acceso a datos
│   ├── futbol_repository.py
│   └── users_repository.py
├── services/            # Lógica de negocio
│   └── users_services.py
├── extensions.py        # Extensiones de Flask
├── requirements.txt     # Dependencias
├── Procfile            # Configuración para Railway
└── runtime.txt         # Versión de Python
```

## 🔐 Seguridad

- Las contraseñas se hashean usando Werkzeug
- Autenticación JWT para endpoints protegidos
- CORS configurado para permitir peticiones desde frontend externo

## 🎨 Frontend

El frontend se encuentra en un repositorio separado y consume esta API a través de la URL de Railway.

## 👨‍💻 Desarrollo

Para contribuir o desarrollar nuevas características:

1. Crea una nueva rama desde `Development`
2. Realiza tus cambios
3. Haz commit y push
4. Crea un Pull Request a `Development`
5. Una vez aprobado, fusiona a `main` para desplegar

## ⚠️ Correcciones Realizadas

- Unificación de bases de datos (se eliminó duplicidad de archivos .db)
- Implementación correcta de commit() en repositorios
- Separación clara entre backend y frontend
- Configuración para despliegue en Railway con Gunicorn

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.
