from pathlib import Path 
import csv
import os
carpeta_destino="dataset"
os.makedirs(carpeta_destino,exist_ok=True)
nombre_archivo="inventario_diario.csv"
ruta=Path(carpeta_destino)/(nombre_archivo)
columnas=["Producto","Stock","Precio"]
datos=[
    ["Aspirina", 100, 4.5],
    ["Paracetamol", "error", 2.0],
    ["Omeprazol", 250, 10.5],
    ["Ibuprofeno", 0, 3.0],
    ["Ibuprofeno", 50, 3.0]
]
with open(ruta,"w+",newline='',encoding="utf-8") as inventario:
    writer=csv.writer(inventario)
    writer.writerow(columnas)
    writer.writerows(datos)