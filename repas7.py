log_alerta = ("  eRrOr_stOck_critico  ", 404)
def arreglo_alertas(log_alerta:tuple):
    log_alerta1=list(log_alerta)
    final=[]
    for item in log_alerta1:
        if isinstance(item,str):
           i=item.strip().capitalize()
           final.append(i)
        else:
           final.append(item)
           continue
    return final
prueba=arreglo_alertas(log_alerta)
print(prueba)

restringidos = {"TSLA", "GME"}
cartera = {"AAPL": 150.5, "MSFT": 305.2, "TSLA": 900.0}
def filtro_archivos(cartera:dict,restringidos:set):
    limpio=(set(cartera.keys())).difference(restringidos)
    return limpio
prueba2=filtro_archivos(cartera,restringidos)
print(prueba2)
#respuesta preguntas teoricas:
#creo que si en las keys hubiese numeros no pasa nada
#:uso difference 
#3
precios = [120, 0, 130, 0, 150, 0]
pre=[]
i=0
def depuracion(precios:list,i:int,pre:list):
    
    while i<len(precios):
        if precios[i] != 0:
            pre.append(precios[i])
        
        i+=1
    return(pre)
precios = [120, 0, 130, 0, 150, 0]
pre=[]
i=0
prueba3=depuracion(precios,0,pre)
print(prueba3)

    
    