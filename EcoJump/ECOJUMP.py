import tkinter as tk
from tkinter import ttk
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

    # Frame para la barra azul inferior
    bar_height = 80
    bottom_bar = tk.Frame(root, bg="#376da0")
    bottom_bar.place(x=0, y=img_height-bar_height, width=img_width, height=bar_height)

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
            quiz_bg_img = Image.open("src/app/QuizesFondo.png")
            quiz_bg_photo = ImageTk.PhotoImage(quiz_bg_img)
            canvas.delete("all")
            canvas.create_image(0, 0, anchor="nw", image=quiz_bg_photo)
            canvas.quiz_bg_photo = quiz_bg_photo  # evitar garbage collection

            # Eliminar widgets previos de encuestas si existen
            if hasattr(root, 'quiz_widgets'):
                for w in root.quiz_widgets:
                    w.destroy()
            root.quiz_widgets = []

            # Frame de encuestas sobre el canvas principal
            from tkinter import ttk
            encuestas_frame = tk.Frame(root, bg="#e3f2ff")
            encuestas_frame.place(x=0, y=120, width=img_width, height=img_height-bar_height-120)
            root.quiz_widgets.append(encuestas_frame)

            # Quitar el título de la encuesta

            # Frame con scrollbar y canvas para scroll vertical correcto
            frame = tk.Frame(encuestas_frame, bg="#e3f2ff")
            frame.pack(fill="both", expand=True)
            canvas_enc = tk.Canvas(frame, bg="#e3f2ff", highlightthickness=0)
            from tkinter import ttk
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

    callbacks = [lambda e: open_win_canvas(root), lambda e: open_win_table(root), lambda e: show_main_bg(), lambda e: show_quiz_bg(), lambda e: open_win_form(root)]
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