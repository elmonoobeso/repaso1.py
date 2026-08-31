#1
producto = " mOnItOr "
precio = 150
def normalizacion(producto:str,precio:int):
    pro1=producto.strip().capitalize()
    final=f"El precio del {pro1} es de {precio} euros"
    return final
norma=normalizacion(producto,precio)
print(norma)
#2
def segmentacion(transacciones:list,limite:int):
    nueva=[]
    try:
        for i in transacciones:
            if  i>limite:
                nueva.append(i)
            else:
                continue
    except:
        print("error")
    cierre_caja=transacciones[-1]
    return nueva,cierre_caja
transacciones = [120, 50, 200, 80, 300, 20]
limite=100
prueb2=segmentacion(transacciones,limite)
print(prueb2)

#3
A = {101, 102, 103, 104}
B = {103, 104, 105, 106}
todos=A.union(B)
menos=A.difference(B)
print(todos,menos)
#los indices numericos en sets no tienen sentido porque se guardan los valores sin orden alguno
#hay una opcion para saber si un valor esta en el set print(valor in set) es un booleano.
#4Diccionarios y Condicionales:
usuario = {"id": 847, "nombre": "Carlos", "suscripcion": "activa"}
val=[]
if "descuento" not in usuario:
    usuario["descuento"]=0
    valores=usuario.values()
    val.append(valores)

print(val)
#python solo busca en las claves
#5
def pipeline_control(id:list):
    for i in id:
        if id ==5:
            continue
        elif id==15:
            break
        elif i==len(id):
            print("Procesamiento exitoso")




        


