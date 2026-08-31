def maximo_subcadena_fuerte(datos:list, k:int):
    lista_top=[]
    for i in range(len(datos)-k+1):
        partio=datos[i:i+k]
        maximo=max(partio)
        lista_top.append(maximo)

    return lista_top
datos = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
prueba=maximo_subcadena_fuerte(datos,k)
print(prueba)
