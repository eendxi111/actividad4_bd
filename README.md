# Taller Unidad 4 — Makeup API + MongoDB + EDA

**Curso:** Bases de Datos para Ciencia de Datos — Universidad de Antioquia  
**Docente:** Miguel Ramos García  
**Estudiante:** Eendxi Cuetia  
**Entrega:** Junio 2026  

---

## Descripción del Proyecto

Flujo completo de Ciencia de Datos que simula un pipeline real:

1. **Extracción** — Se consumen datos reales de productos de maquillaje desde la [Makeup API](http://makeup-api.herokuapp.com/) descargando **931 productos** de 10 categorías distintas.
2. **Almacenamiento RAW** — Los datos se guardan sin modificar en MongoDB local (`taller4_db` → colección `raw_data`).
3. **Análisis EDA** — Se procesan y analizan los datos en Jupyter Notebook con pandas, generando 5 insights y 3 visualizaciones estadísticas.

---

##  Estructura del Repositorio
actividad4_bd/
│
├── ingesta.py          # Fase 1+2: Extracción API → MongoDB (931 productos)
├── analisis.ipynb      # Fase 3: EDA completo con insights y gráficos
├── requirements.txt    # Dependencias del proyecto
├── .gitignore          # Exclusiones de Git
└── README.md           # Este archivo

---

## ⚙️ Cómo Ejecutarlo (Windows)

### 1. Clonar el repositorio
```bash
git clone https://github.com/eendxi111/actividad4_bd.git
cd actividad4_bd
```

### 2. Crear el entorno virtual
```bash
python -m venv venv
```

### 3. Activar el entorno virtual
```bash
.\venv\Scripts\Activate.ps1
```
> Si da error de permisos, ejecuta primero:
> ```bash
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

### 4. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 5. Iniciar MongoDB local
Abre una terminal separada y ejecuta:
```bash
& "C:\Program Files\MongoDB\Server\8.2\bin\mongod.exe" --dbpath "C:\data\db"
```
> ⚠️ Deja esta terminal abierta mientras trabajas.

### 6. Ejecutar la ingesta
```bash
python ingesta.py
```
Descarga 931 productos de la Makeup API y los guarda crudos en `taller4_db.raw_data`.

### 7. Abrir el Notebook de análisis
```bash
jupyter notebook
```
En el navegador abre `analisis.ipynb` y ejecuta las celdas con **Shift+Enter** en orden.

---

## 🗃️ Base de Datos MongoDB

| Parámetro | Valor |
|---|---|
| Motor | MongoDB 8.2 local |
| Base de datos | `taller4_db` |
| Colección | `raw_data` |
| Total documentos | 931 |
| Puerto | 27017 |

---

## 📊 Variables Analizadas

| Variable | Tipo | Descripción |
|---|---|---|
| `name` | texto | Nombre del producto |
| `brand` | texto | Marca del producto |
| `price` | numérico | Precio en USD |
| `product_type` | texto | Tipo (lipstick, foundation, eyeliner…) |
| `rating` | numérico | Calificación promedio 0–5 |

---

## 🔍 Insights Descubiertos

1. 💰 El precio promedio es **$16.51 USD** con rango de $0 a $77
2. 🏆 La marca **NYX** domina con 164 productos (17.6% del catálogo)
3. 💄 **Foundation** es el tipo más frecuente con 166 productos
4. ⭐ Rating promedio de **4.32/5.0** (solo 340 de 931 tienen rating)
5. 💎 Producto más caro: **"Dior Holiday Couture Collection"** a $77.00 USD

---

## 📈 Visualizaciones Generadas

- 🥧 **Gráfico de Torta** — Distribución porcentual por tipo de producto
- 📊 **Gráfico de Barras** — Top 10 marcas con más productos
- 📉 **Histograma** — Distribución de precios con línea de promedio

---

## 🛠️ Requisitos del Sistema

- Windows 10/11
- Python 3.10+
- MongoDB 8.2 local (puerto 27017)
- Conexión a Internet para la ingesta

