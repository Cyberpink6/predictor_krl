<div align="center">

# 🔬 Predictor KRL

### Herramienta profesional para el cálculo del Coeficiente de Refracción Local

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Plataforma-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey?style=flat-square)](/)
[![License](https://img.shields.io/badge/Licencia-MIT-green?style=flat-square)](LICENSE)
[![Version](https://img.shields.io/badge/Versión-1.0-blue?style=flat-square)](/)
[![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-orange?style=flat-square)](https://github.com/TomSchimansky/CustomTkinter)

[📥 Descargar ejecutable](#-instalación) · [📖 Documentación](#-guía-rápida) · [🐛 Reportar problema](../../issues) · [💡 Solicitar feature](../../issues)

</div>

---

## 📖 Tabla de Contenidos

- [¿Qué es el KRL?](#-qué-es-el-krl)
- [Características](#-características)
- [Requisitos del Sistema](#-requisitos-del-sistema)
- [Instalación](#-instalación)
- [Guía Rápida](#-guía-rápida)
- [Interfaz de Usuario](#-interfaz-de-usuario)
- [Interpretación de Resultados](#-interpretación-de-resultados)
- [Solución de Problemas](#-solución-de-problemas)
- [Preguntas Frecuentes](#-preguntas-frecuentes)
- [Glosario](#-glosario)
- [Público Objetivo](#-público-objetivo)

---

## 🔬 ¿Qué es el KRL?

El **Coeficiente de Refracción Local (KRL)** es un parámetro que cuantifica cómo las condiciones atmosféricas afectan la trayectoria de las ondas electromagnéticas al atravesar diferentes capas de aire. Es esencial en aplicaciones que requieren alta precisión de medición.

La fórmula implementada es:

$$KL = 121 \times \frac{P \times 1.3332}{T^2} \times \left(0.0343 + \frac{\partial T}{\partial Z}\right)$$

Donde **P** es la presión en hPa, **T** la temperatura absoluta en Kelvin y **∂T/∂Z** el gradiente vertical de temperatura.

**Aplicaciones principales:**

| Área | Uso |
|------|-----|
| 🌍 Geodesia de alta precisión | Corrección de errores por refracción en mediciones |
| 📡 Telecomunicaciones | Estudios de propagación de señales de radio |
| 🌤️ Meteorología | Análisis de fenómenos atmosféricos |
| 🔬 Investigación climática | Modelado y corrección de datos atmosféricos |

---

## ✨ Características

| Característica | Descripción |
|---|---|
| 🎨 **Doble modo** | Claro / Oscuro para adaptarse a cualquier entorno |
| 🌐 **Multilenguaje** | Español e Inglés integrados, alternables en tiempo real |
| 📊 **Medidor visual** | Barra con gradiente de colores para interpretación inmediata |
| 💡 **Tooltips interactivos** | Información contextual en cada campo de entrada |
| 🎯 **Cálculo preciso** | Resultados con 5 decimales de precisión |
| 🖥️ **Multiplataforma** | Ejecutable en Windows, Linux y macOS sin modificaciones |

---

## 💻 Requisitos del Sistema

<details>
<summary><b>Hardware</b></summary>

| Componente | Mínimo | Recomendado |
|---|---|---|
| Procesador | 1 GHz | 2 GHz+ |
| Memoria RAM | 512 MB | 2 GB |
| Espacio en disco | 50 MB | 100 MB |
| Resolución de pantalla | 1024 × 768 | 1920 × 1080 |

</details>

<details>
<summary><b>Software</b></summary>

| Software | Versión mínima |
|---|---|
| Windows | 10 o superior |
| Linux | Ubuntu 18.04+ |
| macOS | 10.14 (Mojave)+ |
| Python | 3.8 o superior |

</details>

<details>
<summary><b>Dependencias Python</b></summary>

```text
customtkinter==5.2.2
CTkToolTip==0.9
darkdetect==0.8.0
pillow==12.2.0
packaging==26.2
```

</details>

---

## 🚀 Instalación

### Opción 1: Ejecutable *(Recomendado)*

> No requiere Python ni dependencias adicionales.

1. Ve a la sección [**Releases**](../../releases/latest)
2. Descarga `KRLv_1.exe`
3. Ejecuta el archivo directamente

### Opción 2: Desde código fuente

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/predictor_krl.git
cd predictor_krl

# 2. Crear entorno virtual (recomendado)
python -m venv venv

# Activar en Linux / macOS
source venv/bin/activate

# Activar en Windows
venv\Scripts\activate

# 3. Instalar dependencias
pip install customtkinter==5.2.2 CTkToolTip==0.9 darkdetect==0.8.0 pillow==12.2.0

# 4. Ejecutar la aplicación
python main.py
```

---

## 📱 Guía Rápida

```
1. Ingresa la altura del punto de medición (metros)
2. Ingresa la temperatura del aire (°C)
3. Ingresa la presión atmosférica (hPa)
4. Ingresa el gradiente vertical de temperatura (°C/m)
5. Haz clic en "Calcular KRL"
6. Observa el resultado numérico y el medidor visual
```

> 💡 **Tip:** Pasa el cursor sobre el ícono `?` junto a cada campo para obtener información contextual sobre el parámetro.

---

## 🖥️ Interfaz de Usuario

```
┌─────────────────────────────────────────────────────────────┐
│                    PREDICTOR KRL            [Modo] [Idioma] │
├─────────────────────────────────────────────────────────────┤
│  📏 Altura (m)                                          [?] │
│  ┌──────────────────────────────────────────────────────┐   │
│  └──────────────────────────────────────────────────────┘   │
│  🌡️ Temperatura (°C)                                    [?] │
│  ┌──────────────────────────────────────────────────────┐   │
│  └──────────────────────────────────────────────────────┘   │
│  📊 Presión (hPa)                                       [?] │
│  ┌──────────────────────────────────────────────────────┐   │
│  └──────────────────────────────────────────────────────┘   │
│  📈 Gradiente (°C/m)                                    [?] │
│  ┌──────────────────────────────────────────────────────┐   │
│  └──────────────────────────────────────────────────────┘   │
│                                                             │
│        [ Calcular KRL ]        [ Limpiar ]                  │
│                                                             │
│  Resultado: KRL = 0.15432                                   │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ ▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │   │
│  └──────────────────────────────────────────────────────┘   │
│   ● Bajo (verde)         ● Normal (amarillo)   ● Alto (rojo)│
└─────────────────────────────────────────────────────────────┘
```

**Descripción de campos:**

| Campo | Descripción | Ejemplo |
|---|---|---|
| Altura (m) | Altura sobre el nivel del mar | `100` |
| Temperatura (°C) | Temperatura del aire en grados Celsius | `20` |
| Presión (hPa) | Presión atmosférica en hectopascales | `1013.25` |
| Gradiente (°C/m) | Tasa de cambio de temperatura con la altura (∂T/∂Z) | `0.01` |

---

## 🎨 Interpretación de Resultados

El medidor visual utiliza un gradiente de colores para facilitar la lectura del resultado:

| Rango | Valores de KRL | Indicador | Significado |
|---|---|---|---|
| **Bajo** | KRL ≤ 0.11 | 🟢 Verde | Condiciones estables, refracción baja |
| **Normal** | 0.11 < KRL ≤ 0.20 | 🟡 Amarillo | Condiciones típicas, refracción moderada |
| **Alto** | KRL > 0.20 | 🔴 Rojo | Alta refracción — se requieren correcciones |

**Ejemplo práctico** — estación meteorológica a 100 m sobre el nivel del mar:

| Parámetro | Valor |
|---|---|
| Altura | 100 m |
| Temperatura | 20 °C |
| Presión | 1013.25 hPa |
| Gradiente | 0.01 °C/m |
| **Resultado** | **KRL ≈ 0.15432 → Rango Normal** |

---

## 🛠️ Solución de Problemas

<details>
<summary><b>⚠️ Error: "ingrese valores numéricos válidos"</b></summary>

**Causas comunes y correcciones:**

| ❌ Incorrecto | ✅ Correcto |
|---|---|
| `1013,25` (coma decimal) | `1013.25` (punto decimal) |
| Campo vacío | Completar todos los campos |
| `20°C` (con unidad) | `20` (solo el número) |

</details>

<details>
<summary><b>🖥️ La interfaz no se muestra correctamente</b></summary>

1. Verifica que tu pantalla tenga resolución mínima de **1024 × 768 px**
2. Ajusta el **escalado de pantalla** en la configuración de tu sistema operativo
3. Reinicia la aplicación

</details>

---

## ❓ Preguntas Frecuentes

<details>
<summary><b>¿Qué unidades debo usar?</b></summary>

| Parámetro | Unidad requerida |
|---|---|
| Altura | metros (m) |
| Temperatura | grados Celsius (°C) |
| Presión | hectopascales (hPa) |
| Gradiente | °C por metro (°C/m) |

</details>

<details>
<summary><b>¿Cómo obtengo el gradiente vertical de temperatura?</b></summary>

Se calcula midiendo la temperatura en dos alturas conocidas:

```
Gradiente = (T₂ - T₁) / (Z₂ - Z₁)
```

Valores típicos en condiciones estándar: **−0.01 a 0.02 °C/m**

</details>

<details>
<summary><b>¿Los resultados se guardan automáticamente?</b></summary>

No en la versión 1.0. Por ahora puedes:
- Anotar el resultado manualmente
- Tomar una captura de pantalla
- Copiar el valor mostrado en pantalla

</details>

<details>
<summary><b>¿Puedo cambiar el idioma de la interfaz?</b></summary>

Sí. Usa el switch 🌐 en la esquina superior derecha para alternar entre **Español** e **Inglés** en tiempo real.

</details>

---

## 📚 Glosario

| Término | Definición |
|---|---|
| **KRL** | Coeficiente de Refracción Local — parámetro adimensional que cuantifica el efecto de la refracción atmosférica |
| **Refracción Atmosférica** | Desviación de ondas electromagnéticas causada por variaciones en la densidad del aire |
| **Gradiente Vertical (∂T/∂Z)** | Tasa de cambio de la temperatura con respecto a la altura |
| **hPa (Hectopascal)** | Unidad de presión atmosférica; 1 hPa = 100 Pa = 1 mbar |
| **Geodesia** | Ciencia que estudia la forma, dimensiones y campo gravitatorio de la Tierra |
| **Tooltip** | Información contextual que aparece al pasar el cursor sobre un elemento de la interfaz |

---

## 👥 Público Objetivo

- 🔬 **Investigadores** en geodesia, geofísica y meteorología
- 👷 **Ingenieros geodestas** que realizan mediciones de precisión
- 🎓 **Estudiantes de posgrado** en ciencias de la Tierra y atmosféricas
- 🔧 **Técnicos de laboratorio** que procesan datos atmosféricos

---

<div align="center">

Desarrollado con ❤️ para la comunidad científica

</div>
