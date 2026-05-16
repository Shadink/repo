import customtkinter as ctk
import nfc
import threading
import ndef


from PIL import Image


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class PantallaInicio(ctk.CTkFrame):

    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        ctk.CTkLabel(
            self,
            text="Inicio",
            font=ctk.CTkFont(size=32, weight="bold"),
        ).pack(pady=(60, 10))

        ctk.CTkLabel(
            self,
            text="Bienvenid@. Navegue entre pantallas usando las figuras NFC.",
            font=ctk.CTkFont(size=14),
            text_color="gray70",
            justify="center",
        ).pack(pady=(0, 40))


class PantallaActividades(ctk.CTkFrame):

    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        ctk.CTkLabel(
            self,
            text="Actividades Extraescolares",
            font=ctk.CTkFont(size=32, weight="bold"),
        ).pack(pady=(60, 30))

        ctk.CTkLabel(
            self,
            text="Clase de refuerzo (16:00-17:00)",
            font=ctk.CTkFont(size=20),
            image=ctk.CTkImage(light_image=Image.open('images/clase.png'), size=(180,180)),
            compound="top"
        ).pack(pady=(30, 0))

        ctk.CTkLabel(
            self,
            text="Juegos de memoria (18:00-19:00)",
            font=ctk.CTkFont(size=20),
            image=ctk.CTkImage(light_image=Image.open('images/taller de memoria.png'), size=(180,180)),
            compound="top"
        ).pack(pady=(30, 0))

        ctk.CTkLabel(
            self,
            text="Película (20:00-22:00)",
            font=ctk.CTkFont(size=20),
            image=ctk.CTkImage(light_image=Image.open('images/película.png'), size=(180,180)),
            compound="top"
        ).pack(pady=(30, 0))

class PantallaMenu(ctk.CTkFrame):

    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        ctk.CTkLabel(
            self,
            text="Menú del Día",
            font=ctk.CTkFont(size=32, weight="bold"),
        ).pack(pady=(60, 30))

        ctk.CTkLabel(
            self,
            text="Primero - Estofado de Carne",
            font=ctk.CTkFont(size=20),
            image=ctk.CTkImage(light_image=Image.open('images/estofado.png'), size=(180,180)),
            compound="top"
        ).pack(pady=(30, 0))

        ctk.CTkLabel(
            self,
            text="Segundo - Macarrones con Queso",
            font=ctk.CTkFont(size=20),
            image=ctk.CTkImage(light_image=Image.open('images/macarrones carbonara.png'), size=(180,180)),
            compound="top"
        ).pack(pady=(30, 0))

        ctk.CTkLabel(
            self,
            text="Postre - Manzana",
            font=ctk.CTkFont(size=20),
            image=ctk.CTkImage(light_image=Image.open('images/manzana.png'), size=(180,180)),
            compound="top"
        ).pack(pady=(10, 0))

class PantallaHorario(ctk.CTkFrame):

    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        self.scroll = ctk.CTkScrollableFrame(self)
        self.scroll.pack(fill="both", expand=True)

        ctk.CTkLabel(
            self.scroll,
            text="Horario de Clase de hoy",
            font=ctk.CTkFont(size=32, weight="bold"),
        ).pack(pady=(60, 30))

        ctk.CTkLabel(
            self.scroll,
            text="Lengua (08:00-09:00)",
            font=ctk.CTkFont(size=20),
            image=ctk.CTkImage(light_image=Image.open('images/lenguaje(1).png'), size=(180,180)),
            compound="top"
        ).pack(pady=(20, 0))

        ctk.CTkLabel(
            self.scroll,
            text="Matemáticas (09:00-10:00)",
            font=ctk.CTkFont(size=20),
            image=ctk.CTkImage(light_image=Image.open('images/clase de matemáticas(1).png'), size=(180,180)),
            compound="top"
        ).pack(pady=(20, 0))

        ctk.CTkLabel(
            self.scroll,
            text="Plástica (10:00-11:00)",
            font=ctk.CTkFont(size=20),
            image=ctk.CTkImage(light_image=Image.open('images/educación plástica y visual.png'), size=(180,180)),
            compound="top"
        ).pack(pady=(20, 0))

        ctk.CTkLabel(
            self.scroll,
            text="Recreo (11:00-12:00)",
            font=ctk.CTkFont(size=20),
            image=ctk.CTkImage(light_image=Image.open('images/recreo.png'), size=(180,180)),
            compound="top"
        ).pack(pady=(20, 0))

        ctk.CTkLabel(
            self.scroll,
            text="Transición a la vida adulta (12:00-13:00)",
            font=ctk.CTkFont(size=20),
            image=ctk.CTkImage(light_image=Image.open('images/transición a la vida adulta.png'), size=(180,180)),
            compound="top"
        ).pack(pady=(20, 0))

        ctk.CTkLabel(
            self.scroll,
            text="Educación Física (13:00-14:00)",
            font=ctk.CTkFont(size=20),
            image=ctk.CTkImage(light_image=Image.open('images/educación física(1).png'), size=(180,180)),
            compound="top"
        ).pack(pady=(20, 0))
    
    def subir(self):
        self.after(100, lambda: self.scroll._parent_canvas.yview_moveto(0.0))

    def bajar(self):
        self.after(100, lambda: self.scroll._parent_canvas.yview_moveto(1.0))


class App(ctk.CTk):
    ID_COMEDOR="TAG-0002"
    ID_HORARIO="TAG-0003"
    ID_EXTRA="TAG-0001"
    ID_ACCION="TAG-0004"

    pantalla_actual = "horario"
    
    def __init__(self):
        super().__init__()
        self.title("App Multipantalla")
        self.geometry("900x900")
        self.resizable(False, False)

        self.contenedor = ctk.CTkFrame(self)
        self.contenedor.pack(fill="both", expand=True)
        self.contenedor.grid_rowconfigure(0, weight=1)
        self.contenedor.grid_columnconfigure(0, weight=1)

        self.pantallas: dict[str, ctk.CTkFrame] = {}
        for nombre, Clase in [
            ("inicio",      PantallaInicio),
            ("actividades", PantallaActividades),
            ("menu",        PantallaMenu),
            ("horario",     PantallaHorario)
        ]:
            frame = Clase(self.contenedor, controller=self)
            frame.grid(row=0, column=0, sticky="nsew")
            self.pantallas[nombre] = frame

        self.mostrar_pantalla(self.pantalla_actual)

        threading.Thread(target=self.nfc_loop, daemon=True).start()

    def nfc_loop(self):
        def on_connect(tag):
            id = None
            if tag.ndef:
                for record in tag.ndef.records:
                    if isinstance(record, ndef.TextRecord):
                        id = record.text

            print("¡Tag detectado!")
            print("TAG:", id)

            match id:
                case self.ID_COMEDOR:
                    self.mostrar_pantalla("menu")
                case self.ID_HORARIO:
                    self.mostrar_pantalla("horario")
                case self.ID_ACCION:
                    self.bajar(self.pantalla_actual)
                case self.ID_EXTRA:
                    self.mostrar_pantalla("actividades")

            return True

        with nfc.ContactlessFrontend('usb') as clf:
            print("Lector listo, acerca una tarjeta...")
            clf.connect(rdwr={'on-connect': on_connect},
                        iterations=10,
                        interval=0.5)

    def mostrar_pantalla(self, nombre: str):
        self.pantallas[nombre].tkraise()
    
    def bajar(self, nombre: str):
        pantalla = self.pantallas[nombre]
        if hasattr(pantalla, 'bajar'):
            pantalla.bajar()

    def subir(self, nombre: str):
        pantalla = self.pantallas[nombre]
        if hasattr(pantalla, 'subir'):
            pantalla.subir()

if __name__ == "__main__":
    app = App()
    app.mainloop()