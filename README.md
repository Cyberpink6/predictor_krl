<div align="center">
https://img.shields.io/badge/version-1.0-blue.svg
https://img.shields.io/badge/python-3.8+-green.svg
https://img.shields.io/badge/license-MIT-yellow.svg
https://img.shields.io/badge/platform-Windows%2520%257C%2520Linux%2520%257C%2520macOS-lightgrey.svg

Herramienta profesional para el cálculo del Coeficiente de Refracción Local (KRL)

</div>
📖 Tabla de Contenidos
¿Qué es el KRL?

Características

Requisitos del Sistema

Instalación

Guía Rápida

Interfaz de Usuario

Ejemplo Práctico

Interpretación de Resultados

Solución de Problemas

Preguntas Frecuentes

Glosario

🔬 ¿Qué es el KRL?
El Coeficiente de Refracción Local (KRL) es un parámetro fundamental que cuantifica cómo las condiciones atmosféricas afectan la trayectoria de las ondas electromagnéticas al atravesar diferentes capas de aire.

Aplicaciones principales:
🌍 Geodesia de alta precisión - Corrección de mediciones

📡 Telecomunicaciones - Estudios de propagación de señales

🌤️ Meteorología - Análisis de fenómenos atmosféricos

🔬 Investigación climática - Estudios atmosféricos avanzados

✨ Características
Característica	Descripción
🎨 Doble modo	Claro/Oscuro para adaptarse a cualquier entorno
🌐 Multilenguaje	Español e Inglés integrados
📊 Medidor visual	Barra con gradiente de colores para interpretación inmediata
💡 Tooltips interactivos	Información contextual en cada campo
🎯 Cálculo preciso	Resultados con 5 decimales
🖥️ Multiplataforma	Windows, Linux y macOS
💻 Requisitos del Sistema
Hardware
Componente	Mínimo	Recomendado
Procesador	1 GHz	2 GHz+
Memoria RAM	512 MB	2 GB
Espacio en disco	50 MB	100 MB
Resolución	1024 x 768	1920 x 1080
Software
Software	Versión
Windows	10 o superior
Linux	Ubuntu 18.04+
macOS	10.14+
Python	3.8 o superior
Dependencias
text
customtkinter 5.2.2
CTkToolTip   0.9
darkdetect   0.8.0
pillow       12.2.0
packaging    26.2
🚀 Instalación
Opción 1: Ejecutable (Recomendado)
Descarga KRLv_1.exe desde la sección Releases

Ejecuta el archivo - No requiere instalación adicional

Opción 2: Desde código fuente
bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/predictor_krl.git
cd predictor_krl

# Crear entorno virtual (opcional pero recomendado)
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Instalar dependencias
pip install customtkinter==5.2.2 CTkToolTip==0.9 darkdetect==0.8.0 pillow==12.2.0
📱 Guía Rápida





Paso a paso:

📏 Ingresa la altura (metros)

🌡️ Ingresa la temperatura (°C)

📊 Ingresa la presión (hPa)

📈 Ingresa el gradiente vertical (°C/m)

🔘 Haz clic en "Calcular KRL"

📋 Observa el resultado y el medidor visual

🖥️ Interfaz de Usuario
Elementos principales
text
┌─────────────────────────────────────────────────────────────┐
│                    PREDICTOR KRL                    [🌙] [🌐] │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  📏 Altura (m)                    [?]                       │
│  ┌─────────────────────────────────────┐                    │
│  │                                     │                    │
│  └─────────────────────────────────────┘                    │
│                                                             │
│  🌡️ Temperatura (°C)                 [?]                    │
│  ┌─────────────────────────────────────┐                    │
│  │                                     │                    │
│  └─────────────────────────────────────┘                    │
│                                                             │
│  📊 Presión (hPa)                     [?]                    │
│  ┌─────────────────────────────────────┐                    │
│  │                                     │                    │
│  └─────────────────────────────────────┘                    │
│                                                             │
│  📈 Gradiente (°C/m)                   [?]                    │
│  ┌─────────────────────────────────────┐                    │
│  │                                     │                    │
│  └─────────────────────────────────────┘                    │
│                                                             │
│  ┌──────────┐  ┌──────────┐                               │
│  │ CALCULAR │  │ LIMPIAR  │                               │
│  └──────────┘  └──────────┘                               │
│                                                             │
│  📊 Resultado: KRL = 0.15432                              │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │   │
│  └─────────────────────────────────────────────────────┘   │
│  ● Bajo                    ● Normal                    ● Alto │
│                                                             │
└─────────────────────────────────────────────────────────────┘
Campos de entrada
Campo	Descripción	Ejemplo
Altura (m)	Altura sobre el nivel del mar	100
Temperatura (°C)	Temperatura del aire	20
Presión (hPa)	Presión atmosférica	1013.25
Gradiente (°C/m)	Tasa de cambio de temperatura con altura	0.01
💡 Tip: Pasa el cursor sobre el icono (?) junto a cada campo para obtener información contextual

📝 Ejemplo Práctico
Escenario
Estación meteorológica ubicada a 100 metros sobre el nivel del mar

Datos de entrada
Parámetro	Valor
Altura	100 m
Temperatura	20 °C
Presión	1013.25 hPa
Gradiente	0.01 °C/m
Resultado esperado
KRL calculado: ~0.15432

Interpretación: Rango Normal

🎨 Interpretación del Medidor Visual
El medidor visual utiliza un gradiente de colores para facilitar la interpretación:

Rango	Valores de KRL	Color	Significado
Bajo	KRL ≤ 0.11	🟢 Verde	Condiciones estables, baja refracción
Normal	0.11 < KRL ≤ 0.20	🟡 Amarillo	Condiciones típicas, refracción moderada
Alto	KRL > 0.20	🔴 Rojo	Alta refracción, requiere correcciones
🛠️ Solución de Problemas
Error: "⚠️ Error: ingrese valores numéricos válidos"
Causas comunes:

Campos vacíos

Uso de coma (,) en lugar de punto (.) como decimal

Caracteres no numéricos

Soluciones:

diff
- Usar coma: 1013,25
+ Usar punto: 1013.25

- Dejar campos vacíos
+ Completar todos los campos

- Incluir letras: 20°C
+ Solo números: 20
La interfaz no se muestra correctamente
Solución:

Verifica resolución mínima: 1024 x 768

Ajusta el escalado del sistema

Reinicia la aplicación

❓ Preguntas Frecuentes
<details> <summary><b>¿Qué unidades debo usar?</b></summary>
Parámetro	Unidad
Altura	metros (m)
Temperatura	grados Celsius (°C)
Presión	hectopascales (hPa)
Gradiente	°C/m
</details><details> <summary><b>¿Cómo obtengo el gradiente vertical?</b></summary>
El gradiente vertical (∂T/∂Z) se calcula:

text
Gradiente = (T₂ - T₁) / (Z₂ - Z₁)
Valores típicos: -0.01 a 0.02 °C/m

</details><details> <summary><b>¿Los resultados se guardan automáticamente?</b></summary>
No en la versión 1.0. Recomendamos:

Anotar manualmente

Capturar pantalla

Copiar el resultado

</details><details> <summary><b>¿Puedo cambiar el idioma?</b></summary>
¡Sí! Usa el switch 🌐 en la esquina superior derecha para alternar entre Español e Inglés.

</details>
📚 Glosario
Término	Definición
KRL	Coeficiente de Refracción Local. Parámetro que cuantifica la refracción atmosférica
Refracción Atmosférica	Desviación de ondas electromagnéticas por variaciones en densidad del aire
Gradiente Vertical	Tasa de cambio de temperatura con altura (∂T/∂Z)
hPa	Hectopascal. Unidad de presión (1 hPa = 1 mbar)
Geodesia	Ciencia que estudia la forma y dimensiones de la Tierra
👥 Público Objetivo
🔬 Investigadores - Geodesia, geofísica, meteorología

👷 Ingenieros geodestas - Mediciones de precisión

🎓 Estudiantes de posgrado - Ciencias de la Tierra

🔧 Técnicos de laboratorio - Procesamiento de datos atmosféricos

📄 Licencia
Este proyecto está bajo la licencia MIT.

<div align="center">
Desarrollado con ❤️ para la comunidad científica

Reportar Problema · Solicitar Feature · Ver Demo

</div>
