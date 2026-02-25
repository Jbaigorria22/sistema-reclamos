Sistema de Gestión de Reclamos - Cooperativa Malvinas
Este es un sistema de gestión administrativa desarrollado para centralizar, seguir y resolver reclamos de servicios (Agua, Luz, Cloacas, etc.) en una cooperativa o institución vecinal.

🚀 Funcionalidades Principales
Dashboard de Control: Panel inicial con tarjetas estadísticas (Total, Pendientes, Resueltos) que ofrecen una visión rápida del estado operativo.

Gestión de Socios: Registro de reclamos vinculados obligatoriamente a un DNI y un Número de Socio para una trazabilidad completa.

Buscador Inteligente: Motor de búsqueda unificado que permite filtrar reclamos por cualquier criterio: DNI, Socio, Nombre o Dirección.

Módulo de Edición: Funcionalidad para corregir errores de carga o revertir estados de gestión en cualquier momento.

Seguridad: Acceso restringido mediante sistema de autenticación para personal administrativo.

🛠️ Tecnologías Utilizadas
Backend: Python con Flask.

Base de Datos: SQLite (Relacional).

Frontend: HTML5, CSS3 y Bootstrap 5 para un diseño responsivo y profesional.

Lógica de Persistencia: SQL dinámico para filtros y reportes.

📂 Estructura del Proyecto
app.py: Servidor Flask y manejo de rutas de negocio.

database.py: Configuración de la base de datos y esquemas de tablas.

templates/: Plantillas dinámicas de Jinja2 para la interfaz de usuario.

static/: Recursos estáticos (CSS personalizado).

⚙️ Instalación y Uso
Clonar el repositorio.

Crear un entorno virtual: python -m venv venv.

Instalar dependencias: pip install flask.

Ejecutar la aplicación: python app.py.

Acceder a localhost:5000 e ingresar con las credenciales por defecto (admin / 1234).