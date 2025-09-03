# Calculadora de Conversión Numérica

Una aplicación web Flask que convierte números decimales a binario, hexadecimal y octal.

## Características

- Conversión de decimal a binario
- Conversión de decimal a hexadecimal
- Conversión de decimal a octal
- Interfaz web intuitiva

## Instalación Local

1. Clona el repositorio
2. Crea un entorno virtual: `python -m venv .venv`
3. Activa el entorno virtual: `.venv\Scripts\activate` (Windows)
4. Instala las dependencias: `pip install -r requirements.txt`
5. Ejecuta la aplicación: `python main.py`

## Despliegue

### Heroku

1. Instala Heroku CLI
2. Inicia sesión: `heroku login`
3. Crea una nueva app: `heroku create nombre-de-tu-app`
4. Sube el código: `git push heroku main`

### Render

1. Conecta tu repositorio de GitHub
2. Selecciona "Web Service"
3. Configura:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python main.py`

### Railway

1. Conecta tu repositorio de GitHub
2. Railway detectará automáticamente que es una aplicación Python
3. El despliegue será automático

## Estructura del Proyecto

```
Calculadora/
├── main.py              # Aplicación principal Flask
├── requirements.txt     # Dependencias Python
├── Procfile            # Configuración para Heroku
├── .gitignore          # Archivos a ignorar en Git
└── templates/          # Plantillas HTML
    ├── index.html
    ├── binario.html
    ├── hexadecimal.html
    └── octal.html
```