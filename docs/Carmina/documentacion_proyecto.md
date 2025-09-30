# Documentación del Proyecto Tkinter

Este proyecto consiste en una serie de ventanas gráficas desarrolladas
con **Tkinter** y **ttk** en Python. Cada archivo implementa una ventana
independiente con distintos componentes de interfaz de usuario (UI) que
permiten explorar funciones comunes de aplicaciones de escritorio.

------------------------------------------------------------------------

## Ventana 1 --- `win_home.py`

**Funcionalidad principal:** - Ventana de bienvenida. - Muestra
etiquetas (Labels) con texto introductorio. - Botón para mostrar un
`messagebox` de información. - Botón para cerrar la ventana.

**Puntos clave:** - Uso de `ttk.Label` para texto. - Uso de `ttk.Button`
con comandos vinculados a funciones. - Uso de `messagebox.showinfo` para
mostrar un mensaje emergente.

------------------------------------------------------------------------

## Ventana 2 --- `win_form.py`

**Funcionalidad principal:** - Formulario para capturar nombre y edad. -
Validación de datos: - El nombre no debe estar vacío. - La edad debe ser
un número entero. - Guardado de datos en un archivo `.txt` mediante
`filedialog.asksaveasfilename`.

**Puntos clave:** - Uso de `ttk.Entry` para capturar entradas de
texto. - Validación básica de strings (`.strip()`, `.isdigit()`). -
Manejo de archivos con `with open(...)`. - Retroalimentación al usuario
con `messagebox.showerror` y `messagebox.showinfo`.

------------------------------------------------------------------------

## Ventana 3 --- `win_list.py`

**Funcionalidad principal:** - Implementación de un CRUD básico con un
`Listbox`. - Operaciones: - **Agregar:** Inserta un ítem en la lista. -
**Eliminar:** Borra el ítem seleccionado. - **Limpiar:** Vacía toda la
lista.

**Puntos clave:** - Uso de `tk.Listbox` para mostrar elementos en
lista. - Manejo de selección mediante `.curselection()`. - Uso de
botones para ejecutar operaciones CRUD.

------------------------------------------------------------------------

## Ventana 4 --- `win_table.py`

**Funcionalidad principal:** - Muestra datos de un archivo CSV en un
`ttk.Treeview`. - Columnas: `nombre`, `valor1`, `valor2`.

**Puntos clave:** - Uso de `csv.DictReader` para leer archivos CSV. -
Uso de `Treeview` con encabezados personalizados. - Carga dinámica de
filas en la tabla. - Validación de existencia del archivo CSV
(`Path.exists`).

**Ejemplo de archivo esperado (`data/sample.csv`):**

``` csv
nombre,valor1,valor2
A,10,20
B,15,25
C,12,30
```

------------------------------------------------------------------------

## Ventana 5 --- `win_canvas.py`

**Funcionalidad principal:** - Demostración de gráficos en un lienzo
(`Canvas`). - Ejemplos de dibujo: - Rectángulo. - Óvalo. - Línea. -
Texto.

**Puntos clave:** - Uso de `canvas.create_rectangle`,
`canvas.create_oval`, `canvas.create_line`, `canvas.create_text`. -
Configuración de colores, coordenadas y estilos.

------------------------------------------------------------------------

## Conclusión

Este proyecto es una colección de ejemplos prácticos para aprender a
manejar componentes básicos de Tkinter, tales como: - **Labels, Buttons,
MessageBox** - **Entries y validación** - **Listbox con CRUD** -
**Treeview con datos CSV** - **Canvas para gráficos básicos**

Cada ventana es modular e independiente, lo que facilita su
mantenimiento y reutilización en proyectos más grandes.
