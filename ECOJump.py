import os
import sys
import tkinter as tk
from tkinter import ttk

# Al ejecutar este archivo directamente, añadimos la carpeta 'src' al sys.path
# para que las importaciones 'from app.*' funcionen correctamente.
base = os.path.dirname(os.path.dirname(__file__))  # ruta .../src
if base not in sys.path:
    sys.path.insert(0, base)

from app.win_home import open_win_home
from app.win_form import open_win_form
from app.win_list import open_win_list
from app.win_table import open_win_table
from app.win_canvas import open_win_canvas

def main():
    root = tk.Tk()
    root.title("Proyecto Integrador - MVP")

    # Cargar imagen de fondo
    from PIL import Image, ImageTk
    bg_image = Image.open("src/app/PaginaPrincipal.png")
    img_width, img_height = bg_image.size
    root.geometry(f"{img_width}x{img_height}")
    bg_photo = ImageTk.PhotoImage(bg_image)

    canvas = tk.Canvas(root, width=img_width, height=img_height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=bg_photo)
    canvas.bg_photo = bg_photo

    # Función para normalizar iconos sobre fondo azul (se usa más abajo)
    from tkinter import messagebox
    def remove_white_bg(img_path, size):
        try:
            # Fondo azul
            base = Image.new("RGBA", size, (55,109,160,255))
            img = Image.open(img_path).convert("RGBA").resize(size)
            base.paste(img, (0,0), img)
            datas = base.getdata()
            newData = []
            for item in datas:
                # Si el pixel es casi blanco, lo hacemos azul
                if item[0] > 240 and item[1] > 240 and item[2] > 240 and item[3] > 0:
                    newData.append((55, 109, 160, 255))  # azul
                else:
                    newData.append(item)
            base.putdata(newData)
            return ImageTk.PhotoImage(base)
        except Exception as e:
            messagebox.showerror("Error de imagen", f"No se pudo cargar la imagen: {img_path}\n{e}")
            # Imagen azul si falla
            img = Image.new("RGBA", size, (55,109,160,255))
            return ImageTk.PhotoImage(img)

    def make_circular_icon(img_path, size):
        """Devuelve un ImageTk.PhotoImage con la imagen recortada en círculo (RGBA)."""
        try:
            from PIL import ImageDraw
            img = Image.open(img_path).convert("RGBA").resize(size, Image.LANCZOS)
            mask = Image.new('L', size, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, size[0], size[1]), fill=255)
            out = Image.new('RGBA', size, (0, 0, 0, 0))
            out.paste(img, (0, 0), mask)
            return ImageTk.PhotoImage(out)
        except Exception as e:
            # si falla, usar la versión rectangular con fondo azul como respaldo
            try:
                return remove_white_bg(img_path, size)
            except Exception:
                messagebox.showerror("Error de imagen", f"No se pudo cargar el icono: {img_path}\n{e}")
                img = Image.new("RGBA", size, (55,109,160,255))
                return ImageTk.PhotoImage(img)

    def fit_and_center(pil_img, target_size, bg_color=(255,255,255,255)):
        """Resize keeping aspect ratio and paste centered on a background of target_size.
        Returns an ImageTk.PhotoImage.
        """
        try:
            target_w, target_h = int(target_size[0]), int(target_size[1])
            src_w, src_h = pil_img.size
            if src_w == 0 or src_h == 0:
                raise ValueError("Imagen con tamaño inválido")
            scale = min(target_w/src_w, target_h/src_h)
            new_w = max(1, int(src_w * scale))
            new_h = max(1, int(src_h * scale))
            img_resized = pil_img.resize((new_w, new_h), Image.LANCZOS)
            bg = Image.new('RGBA', (target_w, target_h), bg_color)
            paste_x = (target_w - new_w) // 2
            paste_y = (target_h - new_h) // 2
            # If resized has alpha, use it as mask
            if img_resized.mode in ('RGBA', 'LA'):
                bg.paste(img_resized, (paste_x, paste_y), img_resized)
            else:
                bg.paste(img_resized, (paste_x, paste_y))
            return ImageTk.PhotoImage(bg)
        except Exception:
            # Fallback: convert to PhotoImage directly
            try:
                return ImageTk.PhotoImage(pil_img)
            except Exception:
                # return a blank image
                placeholder = Image.new('RGBA', (int(target_size[0]), int(target_size[1])), bg_color)
                return ImageTk.PhotoImage(placeholder)

    # Botón mundo en la esquina superior izquierda (sobre la imagen principal)
    try:
        # tamaño pequeño para el icono del mundo
        world_icon_size = (60, 60)
        img_world_icon = make_circular_icon("src/app/Mundo.png", world_icon_size)
        btn_world_icon = tk.Label(root, image=img_world_icon, bg="#e3f2ff", cursor="hand2")
        btn_world_icon.image = img_world_icon
        btn_world_icon.place(x=10, y=10, width=50, height=50)
    except Exception:
        # si falla la carga, mostrar un label simple
        btn_world_icon = tk.Label(root, text="🌍", bg="#e3f2ff", font=("Segoe UI", 16))
        btn_world_icon.place(x=10, y=10)
    # Enlace al abrir la ventana Mundo: primero mostrar el link destino del botón interno, luego abrir la ventana
    try:
        def show_world_link_and_open(e=None):
            try:
                import os
                from pathlib import Path
                archivo_mapa = os.path.realpath("leon_clima_mapa.html")
                p = Path(archivo_mapa)
                # as_uri() produce file:///... con percent-encoding
                url = p.as_uri()
                from tkinter import messagebox as _mb
                _mb.showinfo("Link del mapa", f"El mapa generado abrirá:\n{url}")
            except Exception:
                # si algo falla, aún abrimos la ventana
                pass
            try:
                open_world_win()
            except Exception:
                pass

        btn_world_icon.bind("<Button-1>", show_world_link_and_open)
    except Exception:
        pass

    # Frame para la barra azul inferior
    bar_height = 80
    bottom_bar = tk.Frame(root, bg="#376da0")
    bottom_bar.place(x=0, y=img_height-bar_height, width=img_width, height=bar_height)

    # Calcular tamaño ideal para cada imagen según el ancho de la ventana
    num_btns = 5
    btn_size = (img_width // num_btns, bar_height)
    img_video = remove_white_bg("src/app/Videos.png", btn_size)
    img_frog = remove_white_bg("src/app/Juego.png", btn_size)
    img_home = remove_white_bg("src/app/Casa.png", btn_size)
    img_tick = remove_white_bg("src/app/Tick.png", btn_size)
    img_bulb = remove_white_bg("src/app/Foco.png", btn_size)

    # Botones con imágenes, sin texto, todos del mismo tamaño y expanden igual
    def create_btn(image):
        frame = tk.Frame(bottom_bar, bg="#376da0", width=btn_size[0], height=btn_size[1])
        frame.pack_propagate(False)
        lbl = tk.Label(frame, image=image, bg="#376da0")
        lbl.pack(fill="both", expand=True)
        return frame, lbl

    btn_video, lbl_video = create_btn(img_video)
    btn_frog, lbl_frog = create_btn(img_frog)
    btn_home, lbl_home = create_btn(img_home)
    btn_tick, lbl_tick = create_btn(img_tick)
    btn_bulb, lbl_bulb = create_btn(img_bulb)

    # Guardar referencias para evitar garbage collection
    bottom_bar.img_video = img_video
    bottom_bar.img_frog = img_frog
    bottom_bar.img_home = img_home
    bottom_bar.img_tick = img_tick
    bottom_bar.img_bulb = img_bulb

    # Efecto hover y selección
    btns = [btn_video, btn_frog, btn_home, btn_tick, btn_bulb]
    lbls = [lbl_video, lbl_frog, lbl_home, lbl_tick, lbl_bulb]
    def show_quiz_bg():
        try:
            # Cargar imagen y crear una ventana separada (Toplevel) para las quizzes
            quiz_bg_img = Image.open("src/app/QuizesFondo.png")
            quiz_bg_photo = ImageTk.PhotoImage(quiz_bg_img)

            # Si ya existe la ventana de quizzes, destruirla antes de crear otra
            existing_quiz = getattr(root, 'quiz_win', None)
            if existing_quiz is not None and getattr(existing_quiz, 'winfo_exists', lambda: False)():
                try:
                    existing_quiz.destroy()
                except:
                    pass
                # limpiar referencia
                try:
                    root.quiz_win = None
                except:
                    pass

            quiz_win = tk.Toplevel(root)
            quiz_win.title("Quizzes")
            # Alineamos tamaño y posición aproximada con la ventana principal
            quiz_win.geometry(f"{img_width}x{img_height}")
            quiz_win.resizable(False, False)
            # Canvas para el fondo dentro de la ventana de quizzes
            q_canvas = tk.Canvas(quiz_win, width=img_width, height=img_height)
            q_canvas.pack(fill="both", expand=True)
            q_canvas.create_image(0, 0, anchor="nw", image=quiz_bg_photo)
            q_canvas.quiz_bg_photo = quiz_bg_photo
            root.quiz_win = quiz_win

            # Frame de encuestas dentro de la ventana de quizzes
            from tkinter import ttk
            encuestas_frame = tk.Frame(quiz_win, bg="#e3f2ff")
            encuestas_frame.place(x=0, y=120, width=img_width, height=img_height-bar_height-120)

            # Frame con scrollbar y canvas para scroll vertical correcto
            frame = tk.Frame(encuestas_frame, bg="#e3f2ff")
            frame.pack(fill="both", expand=True)
            canvas_enc = tk.Canvas(frame, bg="#e3f2ff", highlightthickness=0)
            style = ttk.Style()
            style.theme_use('default')
            style.configure('Blue.Vertical.TScrollbar', background="#e3f2ff", troughcolor="#e3f2ff", bordercolor="#e3f2ff", arrowcolor="#376da0")
            scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas_enc.yview, style='Blue.Vertical.TScrollbar')
            canvas_enc.configure(yscrollcommand=scrollbar.set)
            canvas_enc.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")
            scroll_frame = tk.Frame(canvas_enc, bg="#e3f2ff")
            scroll_id = canvas_enc.create_window((0,0), window=scroll_frame, anchor="nw")
            def _on_frame_configure(event):
                canvas_enc.configure(scrollregion=canvas_enc.bbox("all"))
                canvas_enc.itemconfig(scroll_id, width=canvas_enc.winfo_width())
            scroll_frame.bind("<Configure>", _on_frame_configure)

            # Scroll con mouse para Windows, Linux y macOS
            def _on_mousewheel(event):
                if event.num == 4 or event.delta > 0:
                    canvas_enc.yview_scroll(-1, "units")
                elif event.num == 5 or event.delta < 0:
                    canvas_enc.yview_scroll(1, "units")
            canvas_enc.bind_all("<MouseWheel>", _on_mousewheel)  # Windows/Linux
            canvas_enc.bind_all("<Button-4>", _on_mousewheel)    # macOS scroll up
            canvas_enc.bind_all("<Button-5>", _on_mousewheel)    # macOS scroll down

            # Preguntas sobre el medio ambiente, sin numerar ni tablas, solo 3 respuestas
            preguntas = [
                "¿Reciclas en casa regularmente?",
                "¿Apagas las luces al salir de una habitación?",
                "¿Utilizas transporte público o bicicleta para reducir emisiones?",
                "¿Evitas el uso de plásticos de un solo uso?",
                "¿Participas en actividades de reforestación o limpieza?"
            ]
            respuestas = []
            for pregunta in preguntas:
                pregunta_frame = tk.Frame(scroll_frame, bg="#e3f2ff")
                pregunta_frame.pack(anchor="w", pady=10, padx=18, fill="x")
                # Canvas para rectángulo sin color de fondo
                canvas_preg = tk.Canvas(pregunta_frame, width=img_width-100, height=60, bg="#e3f2ff", highlightthickness=0)
                canvas_preg.pack(fill="x", expand=True)
                canvas_preg.create_rectangle(5, 5, img_width-110, 55, fill="#e3f2ff", outline="#e3f2ff")
                # Título alineado a la izquierda y con wrap para dos renglones
                canvas_preg.create_text(20, 30, text=pregunta, font=("Segoe UI", 12, "bold"), fill="#376da0", width=img_width-180, anchor="w")
                var = tk.StringVar()
                respuestas.append(var)
                for op in ["Sí", "No", "A veces"]:
                    tk.Radiobutton(pregunta_frame, text=op, variable=var, value=op, bg="#e3f2ff", font=("Segoe UI", 11)).pack(anchor="w", padx=36, pady=2)

            import csv
            def mostrar_nuevas_preguntas():
                for widget in scroll_frame.winfo_children():
                    widget.destroy()
                nuevas_preguntas = [
                    "¿Has plantado un árbol este año?",
                    "¿Separas residuos orgánicos e inorgánicos?",
                    "¿Has participado en campañas ambientales?",
                    "¿Consumes productos locales para reducir huella de carbono?",
                    "¿Has compartido información sobre el cuidado ambiental?"
                ]
                nuevas_respuestas = []
                for pregunta in nuevas_preguntas:
                    pregunta_frame = tk.Frame(scroll_frame, bg="#e3f2ff")
                    pregunta_frame.pack(anchor="w", pady=10, padx=18, fill="x")
                    canvas_preg = tk.Canvas(pregunta_frame, width=img_width-100, height=60, bg="#e3f2ff", highlightthickness=0)
                    canvas_preg.pack(fill="x", expand=True)
                    canvas_preg.create_rectangle(5, 5, img_width-110, 55, fill="#e3f2ff", outline="#e3f2ff")
                    canvas_preg.create_text(20, 30, text=pregunta, font=("Segoe UI", 12, "bold"), fill="#376da0", width=img_width-180, anchor="w")
                    var = tk.StringVar()
                    nuevas_respuestas.append(var)
                    for op in ["Sí", "No", "A veces"]:
                        tk.Radiobutton(pregunta_frame, text=op, variable=var, value=op, bg="#e3f2ff", font=("Segoe UI", 11)).pack(anchor="w", padx=36, pady=2)
                def terminar_nueva_encuesta():
                    datos = [var.get() for var in nuevas_respuestas]
                    with open("encuesta_resultados.csv", "a", newline="", encoding="utf-8") as f:
                        writer = csv.writer(f)
                        writer.writerow(datos)
                    from tkinter import messagebox
                    messagebox.showinfo("¡Gracias!", "¡Gracias por responder la segunda encuesta! Sigue mejorando tus hábitos ambientales.")
                    btn_terminar.config(state="disabled")
                btn_terminar.config(command=terminar_nueva_encuesta)

            def terminar_encuesta():
                # Guardar respuestas en un archivo CSV
                preguntas_enc = [
                    "¿Reciclas en casa regularmente?",
                    "¿Apagas las luces al salir de una habitación?",
                    "¿Utilizas transporte público o bicicleta para reducir emisiones?",
                    "¿Evitas el uso de plásticos de un solo uso?",
                    "¿Participas en actividades de reforestación o limpieza?"
                ]
                datos = [var.get() for var in respuestas]
                with open("encuesta_resultados.csv", "a", newline="", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow(datos)
                from tkinter import messagebox
                messagebox.showinfo("¡Gracias!", "¡Gracias por responder! Recuerda que siempre puedes mejorar tus hábitos ambientales. Tus respuestas han sido guardadas.")
                mostrar_nuevas_preguntas()

            style_btn = ttk.Style()
            style_btn.theme_use('default')
            style_btn.configure('Azul.TButton', background="#376da0", foreground="white", borderwidth=0, focusthickness=0, font=("Segoe UI", 12, "bold"))
            btn_terminar = ttk.Button(encuestas_frame, text="Terminar encuesta", command=terminar_encuesta, style='Azul.TButton')
            btn_terminar.pack(pady=18)
            # Si el usuario cierra la ventana del quiz, limpiamos la referencia
            def _on_quiz_close():
                # Al cerrar la ventana de quizzes, destruirla si existe y limpiar la referencia
                try:
                    existing = getattr(root, 'quiz_win', None)
                    if existing is not None and getattr(existing, 'winfo_exists', lambda: False)():
                        existing.destroy()
                except:
                    pass
                try:
                    root.quiz_win = None
                except:
                    pass
            quiz_win.protocol("WM_DELETE_WINDOW", _on_quiz_close)
        except Exception as ex:
            messagebox.showerror("Error", f"No se pudo cargar QuizesFondo.png: {ex}")

    def show_main_bg():
        try:
            main_bg_img = Image.open("src/app/PaginaPrincipal.png")
            main_bg_photo = ImageTk.PhotoImage(main_bg_img)
            canvas.delete("all")
            canvas.create_image(0, 0, anchor="nw", image=main_bg_photo)
            canvas.bg_photo = main_bg_photo  # evitar garbage collection
        except Exception as ex:
            messagebox.showerror("Error", f"No se pudo cargar PaginaPrincipal.png: {ex}")

    # Ventana mundo: integrando el código del mapa/clima en un Toplevel
    def open_world_win(e=None):
        try:
            existing = getattr(root, 'world_win', None)
            if existing is not None and getattr(existing, 'winfo_exists', lambda: False)():
                existing.lift()
                return
            world_win = tk.Toplevel(root)
            world_win.title("Mundo - Clima")
            w_w, w_h = min(900, img_width), min(600, img_height)
            world_win.geometry(f"{w_w}x{w_h}")
            world_win.resizable(False, False)
            # Fondo azul claro
            world_win.configure(bg="#e3f2ff")

            LEON_LAT = 21.1222
            LEON_LON = -101.68

            def obtener_clima():
                try:
                    import requests
                except Exception:
                    messagebox.showerror("Dependencia faltante", "La librería 'requests' no está instalada. Instálala con: pip install requests")
                    return None, None
                try:
                    url = (
                        f"https://api.open-meteo.com/v1/forecast"
                        f"?latitude={LEON_LAT}&longitude={LEON_LON}"
                        f"&current_weather=true"
                    )
                    response = requests.get(url, timeout=10)
                    response.raise_for_status()
                    data = response.json()
                    temperatura = data['current_weather']['temperature']
                    viento = data['current_weather']['windspeed']
                    return temperatura, viento
                except Exception as e:
                    messagebox.showerror("Error al obtener clima", str(e))
                    return None, None

            def abrir_mapa():
                try:
                    import folium
                except Exception:
                    messagebox.showerror("Dependencia faltante", "La librería 'folium' no está instalada. Instálala con: pip install folium")
                    return
                temperatura, viento = obtener_clima()
                if temperatura is None:
                    return
                try:
                    mapa = folium.Map(location=[LEON_LAT, LEON_LON], zoom_start=13)
                    popup_text = (
                        f"<b>León, Guanajuato</b><br>"
                        f"🌡️ Temperatura: {temperatura} °C<br>"
                        f"💨 Viento: {viento} km/h"
                    )
                    folium.Marker(
                        location=[LEON_LAT, LEON_LON],
                        popup=popup_text,
                        tooltip="Haz clic para ver clima",
                        icon=folium.Icon(color="green", icon="cloud")
                    ).add_to(mapa)
                    archivo_mapa = "leon_clima_mapa.html"
                    mapa.save(archivo_mapa)
                    import os
                    archivo_absoluto = os.path.realpath(archivo_mapa)
                    # Además: obtener una imagen estática del mapa para mostrarla en el recuadro
                    try:
                        import requests
                        # Indicador visual mientras se descarga
                        try:
                            map_lbl.config(text="Cargando mapa...", image="")
                        except Exception:
                            pass
                        # Usamos el servicio staticmap.openstreetmap.de para obtener un tile estático
                        static_url = (
                            f"https://staticmap.openstreetmap.de/staticmap.php?center={LEON_LAT},{LEON_LON}&zoom=13&size={box_w}x{box_h}&maptype=mapnik&markers={LEON_LAT},{LEON_LON},red-pushpin"
                        )
                        resp = requests.get(static_url, timeout=10)
                        resp.raise_for_status()
                        from io import BytesIO
                        img_data = BytesIO(resp.content)
                        img_map = Image.open(img_data).convert("RGBA")
                        # Ajustar y centrar dentro del recuadro
                        map_photo = fit_and_center(img_map, (box_w-12, box_h-12))
                        map_lbl.config(image=map_photo, text="")
                        map_lbl.image = map_photo
                    except Exception as e:
                        # fallo en la obtención de la imagen estática: mostrar aviso y texto en la UI
                        try:
                            from tkinter import messagebox as _mb
                            _mb.showwarning("Imagen estática no disponible", f"No se pudo obtener la imagen estática del mapa:\n{e}")
                        except Exception:
                            pass
                        try:
                            map_lbl.config(text="Imagen no disponible", image="")
                        except Exception:
                            pass
                    # Intentar abrir embebido con pywebview (no requiere navegador separado)
                    try:
                        # importar dinámicamente para evitar errores de linter si no está instalado
                        import importlib
                        webview = importlib.import_module('webview')
                        import threading

                        def _open_webview():
                            webview.create_window('Mapa - León', archivo_absoluto)
                            webview.start()

                        t = threading.Thread(target=_open_webview, daemon=True)
                        t.start()
                    except Exception:
                        # Si no está pywebview, abrir en navegador como respaldo
                        import webbrowser
                        webbrowser.open('file://' + archivo_absoluto)
                except Exception as e:
                    messagebox.showerror("Error mapa", str(e))

            frm = tk.Frame(world_win, bg="#e3f2ff")
            frm.pack(fill="both", expand=True)
            lbl = tk.Label(frm, text="Mapa con Clima de León, Gto", font=("Segoe UI", 14, "bold"), bg="#e3f2ff", fg="#0b3b5b")
            lbl.pack(pady=(20,10))

            # Recuadro central donde se mostrará la imagen del mapa
            box_w, box_h = min(700, w_w-80), min(420, w_h-200)
            map_box = tk.Frame(frm, width=box_w, height=box_h, bg="white", relief="groove", bd=2)
            map_box.pack(pady=10)
            map_box.pack_propagate(False)

            # Label dentro del recuadro para la imagen del mapa (se actualizará)
            map_lbl = tk.Label(map_box, bg="white")
            map_lbl.pack(fill="both", expand=True, padx=6, pady=6)

            # Intentar cargar una imagen local 'Mapa' dentro del recuadro (prioridad)
            try:
                import os
                local_png = os.path.realpath("src/app/Mapa.png")
                local_jpg = os.path.realpath("src/app/Mapa.jpg")
                mapa_cargado = False
                for local_path in (local_png, local_jpg):
                    if os.path.exists(local_path):
                        try:
                            img_map = Image.open(local_path).convert("RGBA")
                            map_photo = fit_and_center(img_map, (box_w-12, box_h-12))
                            map_lbl.config(image=map_photo, text="")
                            # Guardar referencia en la ventana para evitar garbage collection
                            world_win.map_photo = map_photo
                            mapa_cargado = True
                            break
                        except Exception:
                            continue
                if not mapa_cargado:
                    # si no hay imagen local, mostrar texto informativo hasta que se descargue la estática
                    map_lbl.config(text="No hay imagen local: se intentará descargar el mapa.", fg="#333333", font=("Segoe UI", 10), compound=None)
            except Exception:
                pass

            btn_map = ttk.Button(frm, text="Mostrar Mapa con Clima", command=abrir_mapa)
            btn_map.pack(pady=10)

            root.world_win = world_win
            def _on_world_close():
                try:
                    existing = getattr(root, 'world_win', None)
                    if existing is not None and getattr(existing, 'winfo_exists', lambda: False)():
                        existing.destroy()
                except:
                    pass
                try:
                    root.world_win = None
                except:
                    pass
            world_win.protocol("WM_DELETE_WINDOW", _on_world_close)
        except Exception as ex:
            messagebox.showerror("Error", f"No se pudo abrir la ventana Mundo: {ex}")

    # Por defecto el tick abre la ventana Home (open_win_home)
    # Orden de botones en la barra: Videos, Juego, Home (main), Tick->Home, Bulb->Mundo
    # callbacks debe tener la misma longitud que btns (5)
    callbacks = [
        lambda e: open_win_canvas(root),
        lambda e: open_win_table(root),
        lambda e: show_main_bg(),
        lambda e: show_quiz_bg(),
        lambda e: open_win_form(root),
    ]
    selected_idx = [None]

    def set_effect(frame, lbl, idx):
        def on_click(e):
            for i, (f, l) in enumerate(zip(btns, lbls)):
                f.config(bg="#376da0")
                l.config(bg="#376da0")
            selected_idx[0] = idx
            callbacks[idx](e)
        frame.bind("<Button-1>", on_click)
        lbl.bind("<Button-1>", on_click)

    for idx, (frame, lbl) in enumerate(zip(btns, lbls)):
        frame.pack(side="left", fill="both", expand=True, padx=0, pady=0)
        set_effect(frame, lbl, idx)

    root.mainloop()

if __name__ == "__main__":
    main()