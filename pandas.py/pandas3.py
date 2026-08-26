import pandas as pd
import numpy as np

ventas = {
    "producto": ["Paracetamol", "Ibuprofeno", "Aspirina", "Omeprazol", "Amoxicilina",
                 "Loratadina", "Enantyum", "Paracetamol"],
    "categoria": ["Analgésico", "Analgésico", "Analgésico", "Gastro", "Antibiótico",
                  "Alergia", "Antiinflamatorio", "Analgésico"],
    "stock": [120, 8, 0, 45, 60, 25, 30, 90],
    "precio": [3.20, 4.50, 2.90, 6.10, 8.75, 5.40, 7.20, 3.20],
    "unidades_vendidas": [340, 95, 60, 120, 80, 55, 40, 210],
    "fecha_entrada": ["01/03/2024", "15/02/2024", "10/01/2024", "20/03/2024",
                      "05/03/2024", "12/03/2024", "18/03/2024", "22/04/2024"]
}
df = pd.DataFrame(ventas)

inventario_extra = pd.DataFrame({
    "producto": ["Paracetamol", "Ibuprofeno", "Aspirina", "Vitamina C"],
    "proveedor": ["Cofares", "Cofares", "Alliance", "Alliance"]
})
print(df.info())
df["fecha_entrada"]=pd.to_datetime(df["fecha_entrada"],format="%d/%m/%Y")
df["mes_entrada"]=df["fecha_entrada"].dt.month
print(df.info())
df["ingresos"]=df["precio"]*df["unidades_vendidas"]
print(df["ingresos"])
suma_categoria=df.groupby("categoria")["ingresos"].sum().sort_values()
print(suma_categoria)
df["ingresos_medios_categoria"]=df.groupby("categoria")["ingresos"].transform("mean")
print(df["ingresos_medios_categoria"])
df["categoria_precio"]=pd.cut(df["precio"],bins=(0,4,7,100),labels=("Barato","medio","caro"))
print(df["categoria_precio"])