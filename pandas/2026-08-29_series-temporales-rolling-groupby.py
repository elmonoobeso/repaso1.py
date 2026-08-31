import pandas as pd
import numpy as np

np.random.seed(7)
fechas = pd.date_range(start="2024-01-01", periods=20, freq="D")

datos = {
    "fecha": fechas,
    "producto": np.random.choice(["Paracetamol", "Ibuprofeno", "Aspirina", None], size=20, p=[0.35, 0.35, 0.25, 0.05]),
    "unidades_vendidas": np.random.randint(10, 150, size=20),
    "precio": np.random.choice([3.20, 4.50, 2.90], size=20)
}
df = pd.DataFrame(datos)
print(type(datos["unidades_vendidas"]))
def es_ventas_fuerte(i):
    int(i)=datos["unidades_vendidas"]
    condicion={i for i in unidades_vendidas if i>=100}
    #print(condicion)
prueba={"unidades_vendidas":120}
uno=es_ventas_fuerte(prueba)
print(df.shape)
print(df.info())
print(df[df["producto"].isnull()].index)
df.loc[4,"producto"]="sin informacion"
print(df.isnull().sum())
df["ingresos"]=df["precio"]*df["unidades_vendidas"]
np.array(df["ingresos"])
df["clasificacion"]=np.where(df["ingresos"]>100,"caro","barato")
print(df["ingresos"],df["clasificacion"])
df.set_index("fecha")
df.sort_index()
df["media_movil5d"]=df["ingresos"].rolling(window=5).mean()
print(df["media_movil5d"])
df["ingresos_medio_producto"]=df.groupby("producto")["ingresos"].mean()
df["ingresos_medio_producto2"]=df.groupby("producto")["ingresos"].transform("mean")
df["por_encima_de_su_producto"]=np.where(df["ingresos"]>df["ingresos_medio_producto"],True, False)
print(df["por_encima_de_su_producto"])
filtro=(df["clasificacion"]=="caro") & (df["producto"]!="sin informacion")
print(df.loc[filtro,["producto","clasificacion","ingresos"]])