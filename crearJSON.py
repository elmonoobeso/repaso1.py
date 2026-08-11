from pathlib import Path
import json
import os
carpeta_destino=Path("dataset")
nombre_archivo="doc_prueba.json"
carpeta_destino.mkdir(parents=True, exist_ok=True)
ruta=Path(carpeta_destino/nombre_archivo)
#carpeta_destino.makedir(exists_ok=True)
columnas=["Producto","Stock","Precio"]
datos=[["Aspirina", 100, 4.5],
    ["Paracetamol", "error", 2.0],
    ["Omeprazol", 250, 10.5],
    ["Ibuprofeno", 0, 3.0],
    ["Ibuprofeno", 50, 3.0]
]
# Mapeo automático de columnas a datos
data_mapeada = [dict(zip(columnas, fila)) for fila in datos]

# Ahora tu JSON será una lista de objetos: 
# [{"Producto": "Aspirina", "Stock": 100, "Precio": 4.5}, ...]
with open(ruta,"w",encoding="UTF-8") as doc_prueba:
    json.dump(data_mapeada,doc_prueba,indent=4,ensure_ascii=False)

