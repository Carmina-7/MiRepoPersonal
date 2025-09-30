# Proyecto Integrador - MVP (Tkinter)

## 📌 Descripción General
Este proyecto es una aplicación de escritorio desarrollada en **Python** utilizando la librería **Tkinter**.  
Funciona como un **MVP (Producto Mínimo Viable)** para demostrar distintas funcionalidades de interfaces gráficas, organizadas en ventanas independientes.

La aplicación incluye las siguientes características principales:
1. **Pantalla de Inicio (Home/Bienvenida)**  
2. **Formulario con validación y guardado de datos en archivo**  
3. **Gestión de Lista (CRUD básico)**  
4. **Tabla con datos cargados desde un archivo CSV (Treeview)**  
5. **Canvas para dibujo gráfico**  

El objetivo es mostrar ejemplos prácticos de **interactividad, validación, persistencia de datos y visualización gráfica**.

---

## 📂 Estructura del Proyecto
```
proyecto/
│── main.py
│── app/
│   ├── win_home.py
│   ├── win_form.py
│   ├── win_list.py
│   ├── win_table.py
│   ├── win_canvas.py
│── data/
│   └── sample.csv
```
- `main.py`: Archivo principal que inicializa la aplicación.  
- `app/`: Carpeta con los módulos de cada ventana independiente.  
- `data/sample.csv`: Archivo de ejemplo con datos para la tabla.  

---

## 📖 Explicación de los Archivos

### 🔹 main.py
- Crea la **ventana principal** de la aplicación.  
- Incluye un **menú de botones** para acceder a cada ventana secundaria.  
- Maneja el ciclo principal con `root.mainloop()`.  
- Opciones disponibles:
  - Home / Bienvenida
  - Formulario
  - Lista (CRUD básico)
  - Tabla (Treeview con datos de CSV)
  - Canvas (dibujos básicos)
  - Botón de salida

### 🔹 win_home.py
- Ventana de bienvenida.  
- Contiene un mensaje inicial y un botón que muestra un `messagebox` con información.  
- Incluye opción para cerrar la ventana.  

### 🔹 win_form.py
- Ventana con **formulario de entrada** para `nombre` y `edad`.  
- Valida que:
  - El campo de nombre no esté vacío.  
  - La edad sea un número entero válido.  
- Permite **guardar los datos en un archivo `.txt`** usando `filedialog`.  
- Muestra confirmación con `messagebox`.  

### 🔹 win_list.py
- Implementa un **CRUD básico** con `Listbox`.  
- Funciones disponibles:
  - **Agregar**: Inserta un nuevo ítem en la lista.  
  - **Eliminar**: Borra el ítem seleccionado.  
  - **Limpiar**: Elimina todos los elementos de la lista.  
- Se incluyen validaciones para evitar entradas vacías.  

### 🔹 win_table.py
- Muestra datos en una **tabla (Treeview)** con columnas `nombre`, `valor1` y `valor2`.  
- Los datos se leen desde `data/sample.csv`.  
- Si el archivo no existe, se muestra un mensaje de advertencia.  
- Ejemplo de contenido esperado del CSV:
  ```csv
  nombre,valor1,valor2
  A,10,20
  B,15,25
  C,12,30
  ```

### 🔹 win_canvas.py
- Ventana para **dibujos gráficos** utilizando `Canvas`.  
- Incluye ejemplos de:
  - Rectángulo  
  - Óvalo con color de relleno  
  - Línea con grosor personalizado  
  - Texto dentro del canvas  

---

## 🚀 Ejecución del Proyecto

1. Clonar o descargar este repositorio.  
2. Verificar que esté instalada la versión de **Python 3.8+**.  
3. Ejecutar el archivo principal:

```bash
python main.py
```

---

## ✅ Tecnologías Utilizadas
- **Python 3**  
- **Tkinter** (interfaz gráfica estándar de Python)  
- **ttk** (estilos modernos de Tkinter)  
- **csv y pathlib** (lectura de archivos y manejo de rutas)  

---

## 📌 Posibles Mejoras
- Agregar persistencia en base de datos (SQLite).  
- Extender el CRUD con edición de registros.  
- Personalizar los estilos visuales con `ttk.Style`.  
- Implementar manejo de imágenes en el canvas.  
- Validación avanzada en el formulario.  

---

## 👨‍💻 Autor
Proyecto desarrollado como **ejemplo educativo** de interfaces gráficas en Python con Tkinter.
