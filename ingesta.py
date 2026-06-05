"""
ingesta.py
----------
Fase 1 + Fase 2 del Taller Unidad 4
- Extrae productos de la Makeup API (makeup-api.herokuapp.com)
- Guarda el JSON crudo en MongoDB: taller4_db > raw_data
"""

import requests
import pymongo
import sys

# ─── Configuración ────────────────────────────────────────────────────────────
MONGO_URI   = "mongodb://localhost:27017/"
DB_NAME     = "taller4_db"
COLLECTION  = "raw_data"
BASE_URL    = "http://makeup-api.herokuapp.com/api/v1/products.json"

# Tipos de producto para paginar y alcanzar ≥ 100 registros
PRODUCT_TYPES = [
    "blush", "bronzer", "eyebrow", "eyeliner", "eyeshadow",
    "foundation", "lip_liner", "lipstick", "mascara", "nail_polish"
]

# ─── Extracción ───────────────────────────────────────────────────────────────
def fetch_products() -> list[dict]:
    all_products: list[dict] = []
    seen_ids: set[int] = set()

    for ptype in PRODUCT_TYPES:
        url = f"{BASE_URL}?product_type={ptype}"
        try:
            resp = requests.get(url, timeout=30)
            resp.raise_for_status()
            products = resp.json()
            for p in products:
                if p.get("id") not in seen_ids:
                    seen_ids.add(p["id"])
                    all_products.append(p)
            print(f"  [{ptype}] → {len(products)} productos  | acumulado: {len(all_products)}")
        except requests.RequestException as e:
            print(f"  ERROR en {ptype}: {e}", file=sys.stderr)

    return all_products

# ─── Carga en MongoDB ─────────────────────────────────────────────────────────
def load_to_mongo(products: list[dict]) -> None:
    client = pymongo.MongoClient(MONGO_URI)
    db     = client[DB_NAME]
    col    = db[COLLECTION]

    # Limpia la colección para evitar duplicados en re-ejecuciones
    col.drop()
    result = col.insert_many(products)
    print(f"\n✅  {len(result.inserted_ids)} documentos insertados en {DB_NAME}.{COLLECTION}")
    client.close()

# ─── Main ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=== Makeup API → MongoDB ===\n")
    print("📡 Descargando productos...")
    products = fetch_products()

    total = len(products)
    print(f"\n📦 Total único descargado: {total}")

    if total < 100:
        print("⚠️  Se obtuvieron menos de 100 registros. Verifica la API.")
        sys.exit(1)

    print("\n💾 Guardando en MongoDB...")
    load_to_mongo(products)
    print("\n🎉 Ingesta completada exitosamente.")