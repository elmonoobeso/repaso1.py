import pandas as pd

data = {
    "producto": ["Paracetamol", "Ibuprofeno", "Aspirina", "Omeprazol", "Amoxicilina"],
    "categoria": ["Analgésico", "Analgésico", "Analgésico", "Gastro", "Antibiótico"],
    "stock": [120, 8, 0, 45, "60"],
    "precio": [3.20, 4.50, 2.90, 6.10, 8.75],
    "fecha_entrada": ["01/03/2024", "15/02/2024", "10/01/2024", "20/03/2024", "05/03/2024"]
}
df = pd.DataFrame(data)
print(df.info())
print(df.dtypes)#stock me aparece como object no como int
df["stock"]=df["stock"].astype("int")
#print(df.dtypes)
df["fecha_entrada"]=pd.to_datetime(df["fecha_entrada"],format="%d/%m/%Y")
print(df.dtypes)
filtro=df["stock"]<10
productos=df[filtro]
print(productos)
print("siguiente ejercicio:")
#usar loc para mostrar para mostrar solo las columnas producto y precio de los productos de categoría "Analgésico"
filtro2=df["categoria"]=="Analgésico"
analgesicos=df[filtro2]
print(analgesicos.loc[:,["producto","precio"]])
#columnasp_p=df.loc["producto","precio"]
#print(columnasp_p["analgesicos"])
print(df[["precio"]].describe())#vamos a buscar el valor
filtro3=df["precio"]==8.75
productomax=df[filtro3]
print(productomax["producto"])