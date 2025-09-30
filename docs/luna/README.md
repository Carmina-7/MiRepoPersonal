
# Proyecto Integrador – MVP (tkinter)

Este proyecto es una **aplicación de escritorio** escrita en Python usando **tkinter** (widgets `ttk`). Sirve como _demo_ de múltiples ventanas y patrones básicos de GUI:

1. **Home/Bienvenida**
2. **Formulario con validación y guardado a archivo**
3. **Lista con CRUD básico (Listbox)**
4. **Tabla en Treeview cargada desde CSV**
5. **Dibujo en Canvas**

> El código es 100% estándar de la librería estándar de Python (no requiere paquetes externos).

---

## Estructura del código

```
.
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

> **Nota:** En los archivos recibidos, los módulos `win_*.py` están en la raíz. Dado que `main.py` importa desde `app.win_*`, debes moverlos a un paquete `app/` (con un `__init__.py` vacío) o **cambiar los imports** en `main.py` para que coincidan con tu layout actual.

---

## Cómo ejecutar

1. **Versión de Python:** 3.10+ (tkinter viene incluido en la mayoría de distribuciones).
2. (Opcional) Crea un entorno virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```
3. Asegura la estructura de directorios (ver arriba) o corrige los imports.
4. Ejecuta:
   ```bash
   python main.py
   ```

La ventana principal ofrece botones para abrir cada demo.

---

## Módulos y responsabilidades

### `main.py`
- **Responsabilidad:** Punto de entrada. Crea la ventana principal y los botones de navegación.
- **Funciones clave:**
  - `main()`: inicializa `tk.Tk()`, define el layout y conecta los botones con `open_win_*` de cada módulo.
- **Detalles UI:**
  - Ventana principal `420x340`, `ttk.Frame` con `padding=16`.
  - Botones:
    - _Home_, _Formulario_, _Lista (CRUD)_, _Tabla (Treeview)_, _Canvas (Dibujo)_, y **Salir**.

### `win_home.py`
- **Responsabilidad:** Ventana de bienvenida sencilla.
- **API:** `open_win_home(parent: tk.Tk)`
- **Comportamiento:**
  - `tk.Toplevel` con título **"Home / Bienvenida"**.
  - Muestra dos `Label` y botones **Mostrar mensaje** (`messagebox.showinfo`) y **Cerrar**.

### `win_form.py`
- **Responsabilidad:** Formulario mínimo con validación y guardado a archivo.
- **API:** `open_win_form(parent: tk.Tk)`
- **Campos:**
  - `Nombre` (`Entry`), `Edad` (`Entry`).
- **Flujo de guardado:**
  1. Valida que `Nombre` no esté vacío.
  2. Valida que `Edad` sea entero (`str.isdigit()`).
  3. Abre un diálogo `asksaveasfilename` (extensión `.txt` por defecto).
  4. Escribe:
     ```
     Nombre: <valor>
     Edad: <valor>
     ```
  5. Confirma con `messagebox.showinfo("OK", "Datos guardados.")`.
- **Botones:** **Guardar** (ejecuta validación + guardado) y **Cerrar**.

### `win_list.py`
- **Responsabilidad:** CRUD básico sobre un `Listbox` en memoria.
- **API:** `open_win_list(parent: tk.Tk)`
- **Elementos:**
  - `Listbox` (altura 10) con `scroll` implícito.
  - `Entry` para capturar ítems.
- **Acciones:**
  - **Agregar:** Inserta el texto no vacío al final del `Listbox`.
  - **Eliminar seleccionado:** Borra el elemento seleccionado (si existe).
  - **Limpiar:** Borra todos los elementos.
  - **Cerrar:** cierra la ventana.

### `win_table.py`
- **Responsabilidad:** Mostrar datos tabulares en un `ttk.Treeview`.
- **API:** `open_win_table(parent: tk.Tk)`
- **Columnas:** `("nombre", "valor1", "valor2")` (encabezados con `capitalize()` y ancho fijo 120).
- **Origen de datos:** CSV ubicado en `data/sample.csv` relativo al repo (calculado como:
  ```python
  Path(__file__).resolve().parents[1] / "data" / "sample.csv"
  ```
  ).
- **Comportamiento:**
  - Si el archivo no existe: `messagebox.showwarning` y **no** muestra datos.
  - Si existe: lo abre con `csv.DictReader` e inserta filas en el `Treeview`.
- **Botón:** **Cerrar**.

### `win_canvas.py`
- **Responsabilidad:** Demostración de dibujo en `Canvas`.
- **API:** `open_win_canvas(parent: tk.Tk)`
- **Dibujo:**
  - `create_rectangle`, `create_oval`, `create_line`, `create_text` con un área `440x240` fondo blanco.
- **Botón:** **Cerrar**.

---

## Datos de ejemplo (`data/sample.csv`)

Crea un archivo `data/sample.csv` con encabezados **exactos** `nombre,valor1,valor2`, por ejemplo:

```csv
nombre,valor1,valor2
Item A,10,20
Item B,5,15
Item C,12,8
```

---

## Recomendaciones y buenas prácticas

- **Paquete `app/`:** añade un archivo vacío `app/__init__.py` para formalizar el paquete. Mantén todos los `win_*.py` ahí (coincide con los imports de `main.py`).
- **Nomenclatura:** `open_win_*` es un patrón claro y coherente; mantenlo para ventanas nuevas.
- **Separación de capas:**
  - Lógica de negocio (validaciones, IO) separada de la capa UI si el proyecto crece.
  - Considera `dataclasses` o modelos para representar filas de `Treeview`.
- **Errores y feedback:**
  - Centraliza `messagebox` en utilidades si las validaciones se vuelven repetitivas.
- **Persistencia:**
  - Para la lista (CRUD), si necesitas persistencia, usa CSV/JSON simple o `sqlite3`.
- **Rutas relativas robustas:**
  - Usa `Path(__file__).resolve()` como en `win_table.py` para derivados portables.
- **Internacionalización (i18n):**
  - Si el proyecto será bilingüe, centraliza los textos en un diccionario o archivos `.po`.

---

## Posibles mejoras

- **Testing de lógica** (no-UI): extrae validaciones a funciones puras y usa `pytest`.
- **Manejo de estados** con `tk.Variable` (`StringVar`, `IntVar`) en formularios.
- **Columnas ajustables** en `Treeview` y ordenamiento al dar clic en encabezados.
- **Arrastrar y soltar** (D&D) en `Listbox` para reordenar.
- **Canvas interactivo**: permitir dibujar con el mouse, limpiar, exportar a imagen (PIL).
- **Empaquetado**: genera un `setup.py` o `pyproject.toml` y un `entry_point` de consola.

---

## Errores y detalles detectados (linting manual)

- **Imports en `main.py`:** `from app.win_* import ...` → asegúrate de que exista el paquete `app/` o cambia a `from win_* import ...` si los módulos permanecen en la raíz.
- **`win_list.py`:** uso correcto de `lb.curselection()` (ya corregido en esta versión; evita olvidar los paréntesis).
- **`win_table.py`:** el bloque `with open(...)` está correcto y debe leer `data/sample.csv`. Si no existe, se muestra un warning y se retorna.

---

## Licencia

Incluye una licencia si se va a publicar (por ejemplo, MIT).

---

## Autoría

- Equipo del **Proyecto Integrador – MVP (tkinter)**.
- Estructura documentada por mantenimiento técnico.
