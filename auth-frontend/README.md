# Auth Frontend

Este proyecto es una aplicación de frontend que permite a los usuarios registrarse y autenticarse. 

## Estructura del Proyecto

- **src/components/Auth**: Contiene los componentes de autenticación.
  - `Login.jsx`: Componente para el inicio de sesión.
  - `Register.jsx`: Componente para el registro de nuevos usuarios.
  
- **src/components/Common**: Contiene componentes comunes.
  - `Navbar.jsx`: Barra de navegación de la aplicación.
  - `Alert.jsx`: Componente para mostrar mensajes de alerta.

- **src/services**: Contiene servicios para la autenticación.
  - `auth.service.js`: Funciones para interactuar con la API de autenticación.

- **src/context**: Contiene el contexto de autenticación.
  - `AuthContext.jsx`: Proporciona el estado de autenticación a los componentes.

- **src/utils**: Contiene utilidades.
  - `axios.config.js`: Configuración de Axios para solicitudes HTTP.

- **src/App.jsx**: Componente principal que configura las rutas y renderiza los componentes.

- **src/main.jsx**: Punto de entrada de la aplicación.

- **public/index.html**: Plantilla HTML principal.

## Instalación

1. Clona el repositorio.
2. Navega al directorio del proyecto.
3. Ejecuta `npm install` para instalar las dependencias.

## Uso

Para iniciar la aplicación, ejecuta `npm run dev` y abre tu navegador en `http://localhost:3000`.