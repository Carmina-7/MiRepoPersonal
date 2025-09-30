# Documentación del Proyecto

## 1. Resumen

Este proyecto es una **aplicación de escritorio con interfaz gráfica en Python**, desarrollada con la librería estándar `tkinter`. El objetivo es demostrar un **MVP (Producto Mínimo Viable)** con diferentes ventanas que muestran funcionalidades típicas de GUI:

- Ventana de bienvenida.
- Formulario con validación y guardado en archivo.
- Lista con operaciones CRUD básicas.
- Tabla con datos cargados desde CSV.
- Lienzo (Canvas) con dibujos.

## 2. Requisitos

- Python 3.8 o superior.
- Librerías: solo `tkinter` (incluida en la librería estándar de Python).
- Archivo CSV de ejemplo: `data/sample.csv`.

## 3. Estructura del repositorio

```
repo-root/
├─ main.py
├─ app/
│  ├─ win_home.py
│  ├─ win_form.py
│  ├─ win_list.py
│  ├─ win_table.py
│  └─ win_canvas.py
└─ data/
   └─ sample.csv
```

## 4. Ejecución

En la raíz del proyecto:

```bash
python main.py
```

Se abrirá la ventana principal con botones para acceder a las distintas secciones.

## 5. Explicación de archivos

### `main.py`
- **Propósito:** Ventana principal del proyecto. Funciona como menú para abrir cada módulo.
- **Detalles:**
  - Crea la raíz `Tk`.
  - Añade botones que llaman a las funciones `open_win_*` de los módulos en `app/`.
  - Mantiene el loop principal con `root.mainloop()`.

### `app/win_home.py`
- **Propósito:** Ventana de bienvenida.
- **Funciones:**
  - Muestra un mensaje de bienvenida.
  - Botón para mostrar un `messagebox` informativo.
  - Botón para cerrar la ventana.

### `app/win_form.py`
- **Propósito:** Formulario de entrada de datos (nombre y edad).
- **Características:**
  - Validación de campos: el nombre no puede estar vacío y la edad debe ser un número.
  - Usa `filedialog.asksaveasfilename` para guardar los datos en un archivo `.txt`.
  - Muestra mensajes de éxito o error con `messagebox`.

### `app/win_list.py`
- **Propósito:** CRUD básico sobre un `Listbox`.
- **Funciones:**
  - `Agregar`: añade un ítem si el campo no está vacío.
  - `Eliminar`: borra el elemento seleccionado.
  - `Limpiar`: vacía toda la lista.
  - Botón para cerrar la ventana.

### `app/win_table.py`
- **Propósito:** Mostrar datos en una tabla (`Treeview`) a partir de un archivo CSV.
- **Detalles:**
  - Define columnas `nombre`, `valor1`, `valor2`.
  - Carga datos desde `data/sample.csv` usando `csv.DictReader`.
  - Si el archivo no existe, muestra advertencia con `messagebox`.

### `app/win_canvas.py`
- **Propósito:** Ventana con un lienzo de dibujo.
- **Detalles:**
  - Dibuja ejemplos: rectángulo, óvalo, línea y texto.
  - Incluye botón para cerrar la ventana.

### `data/sample.csv`
Archivo de muestra con columnas `nombre`, `valor1`, `valor2`. Ejemplo:

```
nombre,valor1,valor2
A,10,20
B,15,25
C,12,30
```

## 6. Flujo de uso

1. El usuario ejecuta `main.py`.
2. Se muestra el menú principal con botones.
3. Cada botón abre una ventana independiente (`Toplevel`).
4. Cada ventana ofrece una funcionalidad distinta (mensajes, formularios, CRUD, tabla, canvas).

## 7. Estilo de código y convenciones
- Uso de `tkinter` y `ttk` para componentes.
- Convención de nombres: funciones `open_win_*` para cada ventana.
- Código modular en archivos separados.

## 8. Posibles mejoras
- Persistencia de datos en BD o archivo JSON en lugar de Listbox en memoria.
- Manejo de excepciones al cargar/guardar archivos.
- Internacionalización (i18n) para soportar múltiples idiomas.
- Pruebas unitarias para las funciones de validación.

---

**Autor:** Equipo de desarrollo Python.

**Versión:** 1.0

