# Documentación del Proyecto - Aplicación Demo con Tkinter

## 📌 Descripción General
Este proyecto es una **aplicación de escritorio en Python** desarrollada con `tkinter`.  
El objetivo es crear una interfaz gráfica con **ventanas interactivas**, cada una demostrando diferentes componentes de `tkinter`:

- Ventana principal (menú de navegación).
- Subventanas: **Home**, **Formulario**, **Lista CRUD**, **Tabla (Treeview)**, **Canvas (dibujo)**.

---

## 📂 Estructura del Proyecto

```
/src/app/
    main.py          # Ventana principal con menú de navegación
    win_home.py      # Ventana de bienvenida con Labels y MessageBox
    win_form.py      # Ventana de formulario con validación y guardado en archivo
    win_list.py      # Ventana de lista con operaciones CRUD básicas
    win_table.py     # Ventana de tabla con carga desde CSV
    win_canvas.py    # Ventana de dibujo en Canvas
/data/
    sample.csv       # Archivo CSV de ejemplo cargado en win_table.py
```

---

## 🚀 Archivos del Proyecto

### 1. **main.py**
- Ventana principal de la aplicación.
- Incluye botones para abrir cada una de las 5 subventanas.
- Usa `ttk.Frame`, `ttk.Label`, `ttk.Button`, `ttk.Separator`.
- Dispone de un botón **Salir** para cerrar la app.

### 2. **win_home.py**
- Ventana de bienvenida.
- Muestra etiquetas (`Label`) con texto explicativo.
- Incluye un botón para mostrar un **MessageBox informativo**.
- Botón de cierre.

### 3. **win_form.py**
- Ventana de formulario con **campos de texto** (nombre, edad).
- Valida que:
  - El nombre no esté vacío.
  - La edad sea un número entero.
- Permite **guardar los datos en un archivo `.txt`** mediante `filedialog.asksaveasfilename`.
- Incluye mensajes de confirmación o error.

### 4. **win_list.py**
- Ventana con una **Listbox**.
- Implementa un CRUD básico:
  - **Agregar** ítem a la lista.
  - **Eliminar** ítem seleccionado.
  - **Limpiar** lista completa.
- Incluye validaciones para evitar ítems vacíos.

### 5. **win_table.py**
- Ventana con un **Treeview** (tabla).
- Carga datos desde un archivo CSV (`/data/sample.csv`).
- Si no existe el archivo, muestra advertencia (`messagebox.showwarning`).
- Muestra las columnas: `nombre`, `valor1`, `valor2`.

Ejemplo de `sample.csv`:
```csv
nombre,valor1,valor2
A,10,20
B,15,25
C,12,30
```

### 6. **win_canvas.py**
- Ventana con un **Canvas** donde se dibujan figuras de ejemplo:
  - Rectángulo.
  - Óvalo.
  - Línea.
  - Texto.
- Espacio para que los usuarios experimenten con gráficos.

---

## 🛠️ Tecnologías Utilizadas
- **Python 3**
- **Tkinter (ttk, messagebox, filedialog, Canvas, Treeview)**
- **CSV (módulo csv)**
- **Pathlib (para manejo de rutas)**

---

## 📖 Flujo de la Aplicación
1. Se ejecuta `main.py` → abre la **ventana principal**.
2. El usuario elige una opción:
   - **Home** → muestra un mensaje de bienvenida.
   - **Formulario** → captura datos y guarda en archivo.
   - **Lista** → maneja ítems con CRUD básico.
   - **Tabla** → muestra datos desde un CSV.
   - **Canvas** → dibuja figuras gráficas.
3. Todas las ventanas incluyen un botón **Cerrar**.

---

## ✅ Conclusiones
Este proyecto demuestra:
- Uso práctico de `tkinter` para GUIs en Python.
- Manejo de múltiples ventanas (`Toplevel`).
- Validación de entradas y persistencia en archivos (`txt`, `csv`).
- CRUD básico con `Listbox`.
- Representación gráfica con `Canvas`.

Es un **MVP (Minimum Viable Product)** de una aplicación de escritorio con interfaz gráfica modular.
