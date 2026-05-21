import customtkinter as ctk
from CTkToolTip import CTkToolTip
from PIL import Image
import math
import os
import sys

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

def resource_path(relative_path):
    """Obtiene la ruta correcta para recursos en PyInstaller"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Idioma por defecto
        self.current_language = "es"
        
        # Cargar iconos de banderas
        self.load_flag_icons()
        
        # Diccionarios de traducción
        self.translations = {
            "es": {
                "title": "Predictor KRL",
                "window_title": "Predictor KRL",
                "dark_mode": "Modo Oscuro",
                "altitude": "Altura (m)",
                "altitude_tooltip": "Altura del punto sobre el nivel del mar (metros)",
                "temperature": "Temperatura (°C)",
                "temperature_tooltip": "Temperatura del aire en grados Celsius",
                "pressure": "Presión (hPa)",
                "pressure_tooltip": "Presión atmosférica en hectopascales",
                "gradient": "Gradiente (°C/m)",
                "gradient_tooltip": "Gradiente vertical de temperatura (∂T/∂Z)",
                "calculate": "Calcular KRL",
                "clear": "Limpiar",
                "result_prefix": "KRL = ",
                "error_numeric": "⚠️ Error: ingrese valores numéricos válidos.",
                "legend": "🟢 Bajo (≤ 0.11)  |  🟡 Normal (0.11 – 0.20)  |  🔴 Alto (> 0.20)"
            },
            "en": {
                "title": "KRL Predictor",
                "window_title": "KRL Predictor",
                "dark_mode": "Dark Mode",
                "altitude": "Altitude (m)",
                "altitude_tooltip": "Height above sea level (meters)",
                "temperature": "Temperature (°C)",
                "temperature_tooltip": "Air temperature in Celsius degrees",
                "pressure": "Pressure (hPa)",
                "pressure_tooltip": "Atmospheric pressure in hectopascals",
                "gradient": "Gradient (°C/m)",
                "gradient_tooltip": "Vertical temperature gradient (∂T/∂Z)",
                "calculate": "Calculate KRL",
                "clear": "Clear",
                "result_prefix": "KRL = ",
                "error_numeric": "⚠️ Error: please enter valid numeric values.",
                "legend": "🟢 Low (≤ 0.11)  |  🟡 Normal (0.11 – 0.20)  |  🔴 High (> 0.20)"
            }
        }
        
        self.setup_ui()
    
    def load_flag_icons(self):
        """Carga los iconos de las banderas"""
        try:
            # Cargar iconos .ico y convertirlos a CTkImage
            es_path = resource_path("BE.ico")
            en_path = resource_path("BF.ico")
            
            # Abrir con PIL y convertir a modo RGBA para soporte de transparencia
            es_img = Image.open(es_path).convert("RGBA")
            en_img = Image.open(en_path).convert("RGBA")
            
            # Redimensionar a tamaño apropiado para el botón (24x16 o 32x22)
            es_img = es_img.resize((24, 16), Image.Resampling.LANCZOS)
            en_img = en_img.resize((24, 16), Image.Resampling.LANCZOS)
            
            self.es_flag_icon = ctk.CTkImage(light_image=es_img, dark_image=es_img, size=(24, 16))
            self.en_flag_icon = ctk.CTkImage(light_image=en_img, dark_image=en_img, size=(24, 16))
            
        except Exception as e:
            print(f"Error cargando iconos de banderas: {e}")
            # Fallback: usar emojis si los iconos no se cargan
            self.es_flag_icon = None
            self.en_flag_icon = None
    
    def t(self, key):
        """Obtiene la traducción para la clave dada"""
        return self.translations[self.current_language].get(key, key)
    
    def setup_ui(self):
        """Configura la interfaz de usuario"""
        self.title(self.t("window_title"))
        self.geometry("650x600")
        
        # Icono de la ventana
        try:
            icon_path = resource_path("ico.ico")
            self.iconbitmap(icon_path)
        except Exception as e:
            print(f"Nota: No se pudo cargar el icono ({e}). La app funcionará sin él.")
        
        self.resizable(False, False)
        
        # Frame superior para controles (switch + bandera)
        top_frame = ctk.CTkFrame(self, fg_color="transparent")
        top_frame.pack(fill="x", padx=20, pady=5)
        
        # Botón de cambio de idioma (bandera) - A LA IZQUIERDA DEL SWITCH
        # Mostrar icono inglés inicialmente (porque el idioma inicial es español, 
        # y al hacer clic cambiará a inglés, por eso mostramos la bandera de destino)
        initial_icon = self.en_flag_icon if self.en_flag_icon else "🇬🇧"
        
        self.lang_button = ctk.CTkButton(
            top_frame, 
            image=self.en_flag_icon if self.en_flag_icon else None,
            text="" if self.en_flag_icon else "🇬🇧",
            width=40,
            height=30,
            command=self.toggle_language,
            fg_color="transparent",
            hover_color="#e0e0e0"
        )
        self.lang_button.pack(side="right", padx=(0, 10))
        
        # Switch modo oscuro/claro
        self.switch_mode = ctk.CTkSwitch(
            top_frame, 
            text=self.t("dark_mode"), 
            command=self.toggle_mode
        )
        self.switch_mode.pack(side="right")
        
        # Título
        self.title_label = ctk.CTkLabel(self, text=self.t("title"), font=("Helvetica", 22, "bold"))
        self.title_label.pack(pady=10)
        
        # Frame de inputs
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        self.entries = {}
        self.create_input_fields()
        
        # Botones
        self.btn_frame = ctk.CTkFrame(self)
        self.btn_frame.pack(pady=15)
        
        self.calc_button = ctk.CTkButton(
            self.btn_frame, 
            text=self.t("calculate"), 
            command=self.calcular, 
            width=120
        )
        self.calc_button.pack(side="left", padx=10)
        
        self.clear_button = ctk.CTkButton(
            self.btn_frame, 
            text=self.t("clear"), 
            command=self.limpiar, 
            width=120
        )
        self.clear_button.pack(side="left", padx=10)
        
        # Resultado
        self.result_label = ctk.CTkLabel(self, text=self.t("result_prefix"), font=("Helvetica", 18, "bold"))
        self.result_label.pack(pady=10)
        
        # Medidor visual
        self.canvas = ctk.CTkCanvas(self, width=400, height=60, highlightthickness=0)
        self.canvas.pack(pady=10)
        self.bar = self.canvas.create_rectangle(50, 20, 350, 40, outline="black", width=2)
        self.value_label = self.canvas.create_text(200, 55, text="", font=("Helvetica", 10))
        
        self.dibujar_gradiente()
        self.indicator = self.canvas.create_line(50, 10, 50, 50, fill="#9d1885", width=3)
        
        # Leyenda
        self.leyenda_label = ctk.CTkLabel(
            self,
            text=self.t("legend"),
            font=("Helvetica", 12)
        )
        self.leyenda_label.pack(pady=(0, 10))
    
    def create_input_fields(self):
        """Crea los campos de entrada con sus tooltips"""
        # Limpiar frame existente si hay
        for widget in self.frame.winfo_children():
            widget.destroy()
        
        self.entries = {}
        
        fields = [
            ("altitude", "altitude_tooltip"),
            ("temperature", "temperature_tooltip"),
            ("pressure", "pressure_tooltip"),
            ("gradient", "gradient_tooltip")
        ]
        
        for field_key, tooltip_key in fields:
            row = ctk.CTkFrame(self.frame)
            row.pack(fill="x", pady=10)
            
            label = ctk.CTkLabel(row, text=self.t(field_key), width=180, anchor="w")
            label.pack(side="left", padx=10)
            
            entry = ctk.CTkEntry(row, width=200)
            entry.pack(side="left", padx=10)
            self.entries[field_key] = entry
            
            help_btn = ctk.CTkButton(
                row, 
                text="?", 
                width=30, 
                height=30, 
                corner_radius=15,
                fg_color="#2a7dbf", 
                hover_color="#084a7f", 
                cursor="hand2"
            )
            help_btn.pack(side="left", padx=5)
            CTkToolTip(help_btn, message=self.t(tooltip_key))
    
    def toggle_language(self):
        """Cambia el idioma entre español e inglés"""
        if self.current_language == "es":
            self.current_language = "en"
            # Cambiar a icono español (para poder volver al español)
            if self.es_flag_icon:
                self.lang_button.configure(image=self.es_flag_icon, text="")
            else:
                self.lang_button.configure(text="🇪🇸")
        else:
            self.current_language = "es"
            # Cambiar a icono inglés (para poder ir al inglés)
            if self.en_flag_icon:
                self.lang_button.configure(image=self.en_flag_icon, text="")
            else:
                self.lang_button.configure(text="🇬🇧")
        
        self.update_language()
    
    def update_language(self):
        """Actualiza todos los textos de la interfaz al idioma actual"""
        # Actualizar título de ventana
        self.title(self.t("window_title"))
        
        # Actualizar título principal
        self.title_label.configure(text=self.t("title"))
        
        # Actualizar switch
        self.switch_mode.configure(text=self.t("dark_mode"))
        
        # Guardar valores actuales de los entries antes de recrearlos
        current_values = {key: entry.get() for key, entry in self.entries.items()}
        
        # Recrear campos de entrada (para actualizar labels y tooltips)
        self.create_input_fields()
        
        # Restaurar valores en los entries
        for key, value in current_values.items():
            if key in self.entries:
                self.entries[key].insert(0, value)
        
        # Actualizar botones
        self.calc_button.configure(text=self.t("calculate"))
        self.clear_button.configure(text=self.t("clear"))
        
        # Actualizar resultado (mantener valor si existe)
        current_result = self.result_label.cget("text")
        if "KRL =" in current_result and len(current_result) > 6:
            try:
                value = current_result.split("=")[1].strip()
                self.result_label.configure(text=f"{self.t('result_prefix')}{value}")
            except:
                self.result_label.configure(text=self.t("result_prefix"))
        else:
            self.result_label.configure(text=self.t("result_prefix"))
        
        # Actualizar leyenda
        self.leyenda_label.configure(text=self.t("legend"))
    
    def toggle_mode(self):
        mode = "dark" if self.switch_mode.get() == 1 else "light"
        ctk.set_appearance_mode(mode)
        bg_color = "#2b2b2b" if mode == "dark" else "#f0f0f0"
        self.canvas.configure(bg=bg_color)
        
        # Actualizar color del botón de idioma según el modo
        if mode == "dark":
            self.lang_button.configure(hover_color="#404040")
        else:
            self.lang_button.configure(hover_color="#e0e0e0")
    
    def calcular(self):
        try:
            # Usar las claves en inglés para acceder a los entries
            altura = float(self.entries["altitude"].get())
            temp_c = float(self.entries["temperature"].get())
            presion = float(self.entries["pressure"].get())
            gradiente = float(self.entries["gradient"].get())
            
            temp_k = temp_c + 273.15
            kl = 121 * (presion * 1.3332) / (temp_k ** 2) * (0.0343 + gradiente)
            
            self.result_label.configure(text=f"{self.t('result_prefix')}{kl:.5f}")
            self.actualizar_medidor(kl)
        except ValueError:
            self.result_label.configure(text=self.t("error_numeric"))
    
    def dibujar_gradiente(self):
        """Dibuja el gradiente una sola vez."""
        self.canvas.delete("gradient")
        w = 300
        for i in range(w):
            r = min(255, int(255 * (i / w * 2))) if i < w / 2 else 255
            g = 255 if i < w / 2 else max(0, int(255 * (2 - i / w * 2)))
            color = f'#{r:02x}{g:02x}00'
            self.canvas.create_line(50 + i, 20, 50 + i, 40, fill=color, tags="gradient")
    
    def actualizar_medidor(self, kl):
        min_kl, max_kl = 0.05, 0.25
        x = max(0, min(1, (kl - min_kl) / (max_kl - min_kl)))
        pos = 50 + x * 300
        self.canvas.coords(self.indicator, pos, 10, pos, 50)
    
    def limpiar(self):
        for entry in self.entries.values():
            entry.delete(0, "end")
        self.result_label.configure(text=self.t("result_prefix"))
        self.canvas.coords(self.indicator, 50, 10, 50, 50)

if __name__ == "__main__":
    App().mainloop()