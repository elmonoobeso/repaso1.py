import pandas as pd
data = {
    "producto": ["Paracetamol", "Ibuprofeno", "Aspirina", "Omeprazol", "Amoxicilina",
                 "Paracetamol", "Loratadina", "Enantyum"],
    "categoria": ["Analgésico", "Analgésico", "Analgésico", "Gastro", "Antibiótico",
                  "Analgésico", "Alergia", None],
    "stock": [120, 8, 0, 45, 60, 120, None, 30],
    "precio": [3.20, 4.50, 2.90, 6.10, 8.75, 3.20, 5.40, 145.00],
    "fecha_entrada": ["01/03/2024", "15/02/2024", "10/01/2024", "20/03/2024",
                      "05/03/2024", "01/03/2024", "12/03/2024", "18/03/2024"]
}
df = pd.DataFrame(data)
print(df.shape)
print(df.dtypes)
print(df.info())
df["fecha_entrada"]=pd.to_datetime(df["fecha_entrada"],format="%d/%m/%Y")
print(df["fecha_entrada"].dtypes)
print(df.duplicated().sum())
duplicados=df[df.duplicated()]
print(duplicados.loc[:,["producto","categoria"]])
df.drop_duplicates()
print(df.isnull().sum())
print(df.isnull().sum().sum())
#df["categoria"].fillna("sin categoria")#si hay varios nulos puedo elegir exactamente cual rellenar? no la columna entera
print(df[df["categoria"].isnull()])
df.loc[7,"categoria"]="sin categoria"#porque no me ha funcionado??
print(df[df["categoria"].isnull()])
df["stock"].fillna(df["stock"].median())
print(df[df["stock"].isnull()])#porque no sale el valor corregido???
print(df["precio"].describe())
#outlier, lo son? que hacemos con ellos? si mi variable no va a seguir una distribucion normal como en el caso normalmente de precios en vez de z usamos iqr:
iqr=6.762500-3.200000#aqui viven el 50% de mis datos aprox
#averiguamos limites el 1,5 es un valor estadistico aceptado no es random
limite_inf=3.200000-1.5*iqr
print(limite_inf)
limite_sup=6.762500+1.5*iqr
print(f"el valor max de 145 es muy superior al {limite_sup} por lo que lo declaramos outlier")
print(df.duplicated().sum())
df.drop_duplicates()
filtro=df["categoria"]=="Analgésico"
analgesicos=df[filtro]
print(analgesicos.loc[:,["producto","precio"]])
#normalizacion de nombres de columnas, muy importante si vamos a combinar tablas.
df.columns=["producto","categoria","stock","precio","fecha_entrada"]#en el ejercicio pone que las pongamos en mins pero quiero hacerlo en mayusculas por cambiar
#df.columns=df.columns.str.upper()
print(df.info)
import matplotlib.pyplot as plt

df["precio"].hist(bins=20)
plt.show()   # importante: sin esto, en muchos entornos (como VS Code) el gráfico no se llega a mostrar