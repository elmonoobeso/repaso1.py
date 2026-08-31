#Escribe una función limpiar_registro(datos: list) -> list que elimine todos los elementos duplicados de una lista de entrada, manteniendo estrictamente el orden original de primera aparición
def limpiar_registro(datos:list):
    lista_limpia=[]
    for n in datos:
        if n  in lista_limpia:
            continue
        else:
            lista_limpia.append(n)
    return list(dict.fromkeys(lista_limpia))#transformamos en dicc 1 para limpiar duplicados
datos=[35, 1.77, "Brais", 35, "Moure", "Brais", 10]
datos_limpios=limpiar_registro(datos)
print(datos_limpios)