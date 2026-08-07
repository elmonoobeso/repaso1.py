precios = [120, 0, 130, 0, 150, 0]
pre=[]
i=0
def depuracion(precios:list,i:int):
    while i in precios:
        precios.remove(i)
    return precios
pr=depuracion(precios,0)
print(pr)
#si la lista no tiene 0 el bucle no empieza nunca la lista se queda igual.
#el peligro es un bucle infinito, en este ejercio no hay problema porque si hay i en la lista acaba con la primera vuelta del bucle al eliminarlo.

def validacion_integridad(id_lote:int="",datos:list=None):
    if not id_lote  and not datos :
        print("ahuevo maricarmen")
    return

prr=validacion_integridad()

#5
def inicializacion(sensores:list=None,valor:str="Pendiente_Sincronizacion"):
    dicc=dict.fromkeys(sensores,valor)
    
    print(dicc)
    return dicc
sensores = ["S_101", "S_102", "S_103"]
pi=inicializacion(sensores,"Pendiente_Sincronizacion")
   
#si no recuerdo mal los diccionarios si pueden tener elementos duplicados al contrario que los sets.
#fromkeys es el metodo para hacer un diccionario con las claves de las listas lo unico que no consigo luego en la misma linea añadir el mismo valor a todo, he intentado con update y con la forma clasica de dicc[]=valor pero no he sido capaz, no se si sera por algun fallo menor de sintaxis o de logica