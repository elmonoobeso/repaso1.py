#respuesta teorica if comentario!="":´
#nivel1:
#Tienes una lista de precios de productos procedentes de un scraping. Algunos valores son `0` o `None` debido a errores de captura.
#**El Reto:** Crea una función que reciba la lista y elimine los ceros.
def elimina_ceros(precios:list):
    lista_limpia=[]
    for i in precios:
        if i!=0:
            lista_limpia.append(i)
    print(lista_limpia)
    return lista_limpia
precios = [12.50, 0, 34.90, None, 0, 5.25, 0.0, 18.00, None, 0, 55.60]
elimina_ceros(precios)
# --- Datos de Prueba ---
metricas_lote_1 = {"id_registro": 4041, "tiempo_ms": 120, "filas_leidas": 500}
metricas_lote_2 = {"id_registro": 4042, "tiempo_ms": 85, "filas_leidas": 320}
metricas_vacias = {}

# --- El Reto ---
# Define la firma correctamente evitando el "Anti-patrón de firma de funciones"
def procesar_registro(metricas, ids_exitosos=...):
    
    # 1. Validación: Si el diccionario de métricas está vacío, retorna inmediatamente (usa Truthiness)
    
    # 2. Tu lógica para añadir el "id_registro" a la lista ids_exitosos
    
    # 3. Retorna la lista actualizada
    pass

metricas_lote_1 = {"id_registro": 4041, "tiempo_ms": 120, "filas_leidas": 500}
metricas_lote_2 = {"id_registro": 4042, "tiempo_ms": 85, "filas_leidas": 320}
metricas_vacias = {}

def logs(*metricas:dict!=None,idd:list=None):
    if idd is None:
        idd=[]
    for metrica in metricas:#se ha vuelto una tupla con el args
        valor=metrica.get("id_registro")
        idd.append(valor)
    print (idd)
    return idd
logs(metricas_lote_1,metricas_lote_2)

#teoria respuesta 3:
#porque dict.values da lugar a una variable no operable que se llama dict values, para operar con esta tienes que transformarla como yo he hecho abajo en una lista.
valor=list(metricas_lote_1.values())

print(type(valor))
#problema 3:
datos = {"Ventas": ["CRM", "Email"], "IT": ["Server", "Cloud"]}
listapre=list(datos.values())
print(listapre)
dat1=set(datos["Ventas"])
dat2=set(datos["IT"])
dif=dat1.union(dat2)
li=list(dif)
print(li)
#pregunta teoria 4:
#no te estaras refieriendo a un bucle if?, bueno si no hay mas codigo debajo tanto el else como el continue no hacen nada, estan para decir todo lo que no haya cumplido esta condicion que haga esto, pero si no tienen nada mas que hacer...no hay motivo para ponerlo.
def compresion(transacciones:list):
    lista_limpia=[i for i in transacciones if i % 2==0]#filtro con list compr
    print(lista_limpia)
    return lista_limpia
#pregunta teorica 5
#es un error memory in place, al hacer eso de modificar sobre la misma variable con una funcion, la memoria es el problema no se guarda y no podra ser el usado el resultado de la funcion en otra operacion despues... la solucion es usar otra variable nueva.
class Inventario:
    def __init__(self,almacen,productos:list):
       self.almacen=almacen
       self.__productos=productos
    def agregar_nombre(self,nombre):
        self.__productos.append(nombre)
        return self.__productos
    def obtener_resumen(self):
        return([texto.upper() for texto in self.__productos])
        
    def obtener_resumen2(self):
        lista_may=[]
        for i in self.__productos:
            u=i.upper()
            lista_may.append(u)
        return lista_may
    
    
    