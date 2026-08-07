#la respuesta a la teoria del 1 es: import math.pi from math as pi, si solo vas a usar pi no hace falta importar el modulo entero eso causa desgaste y mal uso de la memria lo que puede enlentecer el programa.
#practica 1:
raw_data = [22.5, 0, 19.8, None, "", 25.3, 0.0, " "]
def ejercicio1(raw_data:list):
    data=[float(i) for i in raw_data if type(i) is float and int]#el valor cero no hay que filtrarlo se filtra solo con el if automaticamente
    print(data)
    return (data)
raw_data = [22.5, 0, 19.8, None, "", 25.3, 0.0, " "]
ejercicio1(raw_data)

#ejercicio2 teoria:
#un set elimina duplicados directamente al contrario que una lista, por otra parte los valores dentro de set no siempre corresponden al mismo indice por lo que estan desordenados, buscar el mismo valor por un indice en set es imposible, mejor una lista.
#ejercicio 2 pract:
config = {"provider_a": {"id": 101, "status": "active"}, "provider_b": {"id": 202, "status": ""}}
clave1=(list(config.keys())[0])
clave2=(list(config.keys())[1])
valores1=list(config[clave1].values())
valores2=list(config[clave2].values())
valor1=[i for i in valores1 if type(i) is int]
valor2=[i for i in valores2 if type(i) is int]
print(valor1+valor2)

#ejercicio2 otra forma?#no he terminado de hacer la funcion de abajo, creo que debe haber una forma que incluso con las restricciones del ejercicio se pueda hacer de manera mas pythoniana y mas corta, aun asi la de arriba funciona.

def ejercicio2(config:dict):
    lista_valor=(list(config.values())[0])
    print(type(lista_valor))
    lim=[i for i in lista_valor if type(i) is int]
    print(lim)
    return(lim,lista_valor)
ejercicio2(config)
#una mejor forma de hacer el ejercicio 2: val 
        #for provider_data in config.values() 
        #for val in provider_data.values() 
        #if type(val) is int
#3 teoria:
#timedelta se usa para calcular diferencias de tiempo, sin embargo datetime se usa para establecerlo, te da dias mes año y minuto
#puedes restar y operar con objetos de tiempo pero tienen que ser del mismo tipo, typeerror
#ejercicio 3 practica:
from datetime import time,datetime,time,timedelta
from typing import Optional
class DataPipeline:
    def __init__(self,inicio:datetime,fin:Optional[datetime]=None):
        self.__inicio=inicio
        #si el usuario no pasa fin cogemos el momento actual
        self.__fin=fin if fin else datetime.now()
    def __calcular_duracion(self):
        diferencia=self.__inicio- self.__fin
        return diferencia
#modulo typing para asegurar que dato esperar.. optional es de ahi o any

#no estoy seguro si era lo que me pedia el ejercicio creo que si, tengo dudas con datetime.now() en el constructor y con lo de opcionional aunque creo que esta cubierto por el argumento inicio.
#ejercicio4
batch1 = [1, 2, 3]
batch2 = [4, 5]
params={"factor": 2}

def ejercicio4(*lotes:list[int],params:Optional[dict]=None):
    processed_data=[i*(params["factor"]) for lote in lotes for i in lote if not lotes is None]
    print(processed_data)
params={"factor": 2}
uno=ejercicio4(batch1,batch2,params=params)
#ES CLAVE: ACORDARSE QUE DESPUES DE * TENEMOS UNA TUPLA.. Si no hubiesemos hecho un for dentro de un for hubieramos multiplado las tuplas enteras(duplicandolas) no lo valores de dentro!

#ejercicio5
dataset = [{"val": 10, "div": 2}, {"val": 5, "div": 0}, {"val": None, "div": 1}]
def ejercicio5(dataset:list):
    try:
        limpio=[i for grupo in dataset for i in grupo if type(i) is int]
    except:
        