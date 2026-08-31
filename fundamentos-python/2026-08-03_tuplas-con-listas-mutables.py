
def agregar_transaccion(registro:tuple,monto:int):
    regis=list(registro)
    for n in regis:
        if type(n)==list: 
           n.append(monto)
    return (regis)
registro = ("ID-9921", "ACTIVO", [100, 250, 300])
monto=150
nuevo=agregar_transaccion(registro,monto)
print(nuevo)
#no hacia falta al principio de esta funcion transformarla en lista para modificar la lista dentro de la tupla
#la forma mas pro es esta:2. Práctica estándar: isinstance evalúa si el elemento es una lista de forma segura.
#if isinstance(item, list):

def congelar_registro(registro:tuple):
    regi=list(registro)
    registro1=tuple(regi)




