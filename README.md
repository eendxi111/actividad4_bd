#  Taller Unidad 4 — Makeup API + MongoDB + EDA

**Curso:** Bases de Datos para Ciencia de Datos — Universidad de Antioquia  
**Docente:** Miguel Ramos García  

---

## Descripción del Proyecto

Flujo completo de Ciencia de Datos que:
1. **Extrae** productos de maquillaje reales desde la [Makeup API](http://makeup-api.herokuapp.com/)
2. **Almacena** los datos crudos en MongoDB (`taller4_db` > `raw_data`)
3. **Analiza** los datos con pandas y genera visualizaciones estadísticas (EDA)

### API Utilizada
**Makeup API** — `http://makeup-api.herokuapp.com/api/v1/products.json`  
Provee información real de productos de maquillaje: nombre, marca, precio, tipo, categoría y rating.  
Se descargaron **+400 productos** usando 10 tipos de producto distintos.

---

## Estructura del Repositorio

```
taller4_makeup/
│
├── ingesta.py          # Fase 1+2: Extracción API → MongoDB
├── analisis.ipynb      # Fase 3: Procesamiento y EDA
├── requirements.txt    # Dependencias del proyecto
├── .gitignore          # Exclusiones de Git
└── README.md           # Este archivo
```

---

## Cómo Ejecutarlo

### 1. Clonar el repositorio
```bash
git clone https://github.com/TU_USUARIO/taller4-makeup-eda.git
cd taller4-makeup-eda
```

### 2. Crear y activar un entorno virtual
```bash
python -m venv venv

# En Windows:
venv\Scripts\activate

# En Mac/Linux:
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Asegurarse de que MongoDB esté corriendo
```bash
# En Windows (si MongoDB está instalado como servicio):
net start MongoDB

# En Mac/Linux:
sudo systemctl start mongod
```

### 5. Ejecutar la ingesta
```bash
python ingesta.py
```
Esto descarga los productos de la API y los guarda en MongoDB.

### 6. Abrir el Notebook de análisis
```bash
jupyter notebook analisis.ipynb
```
Ejecutar todas las celdas en orden (`Kernel > Restart & Run All`).

---

## Variables Analizadas

| Variable | Descripción |
|---|---|
| `name` | Nombre del producto |
| `brand` | Marca del producto |
| `price` | Precio en USD |
| `product_type` | Tipo (lipstick, foundation, mascara…) |
| `rating` | Calificación promedio de usuarios (0-5) |
| `category` | Subcategoría del producto |

---

## Insights Principales

1. El precio promedio de los productos es ~$13 USD con fuerte sesgo a la derecha
2. `lipstick` y `foundation` son los tipos de producto más frecuentes
3. Una sola marca domina el catálogo en volumen de productos
4. Los productos de ojos tienen el rating promedio más alto (~4.2/5.0)
5. El tipo de producto no determina necesariamente su precio

---

## Requisitos del Sistema

- Python 3.10+
- MongoDB 6.0+ (local en puerto 27017)
- Conexión a Internet (para la ingesta)
