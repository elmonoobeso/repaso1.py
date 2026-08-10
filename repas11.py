raw_sensor_data = [
    {"sensor_a": 10, "sensor_b": None, "sensor_c": 5},
    {"sensor_a": 0, "sensor_b": 8, "sensor_c": ""},
    {"sensor_a": 12, "sensor_b": 0, "sensor_c": 15}
]
import typing
class SensorProcessor:


    def __init__(self,raw_sensor_data:list[dict[str,any]]):
        self.__data=raw_sensor_data
    def get_clean_values(self):
        lista_limpia=[]
        for sensor in self.__data:
            for valor in sensor.values():
                if type(valor) is int:
                    lista_limpia.append(valor)
        return (lista_limpia)

    def gett_clean(self):
        return [valor for sensor in self.__data for valor in sensor.values() if valor]
    #El objetivo es filtrar los ceros, los nulos (None) y los strings vacíos ("") sin usar comparaciones explícitas como != 0 o is not None.
#la cllave de la Evaluación Implícita (Truthiness) en Python es entender que el número 0 (al igual que None y "") es considerado por el intérprete como un valor Falsy (falso lógico).

#por lo tanto, al escribir simplemente if valor: dentro de la comprensión de listas, Python evalúa automáticamente si el elemento "tiene contenido o entidad real". Si el valor es 0, None o "", Python lo desecha por defecto sin necesidad de escribir operadores de desigualdad.

uno = SensorProcessor(raw_sensor_data)
print(uno.get_clean_values())

dos = SensorProcessor(raw_sensor_data)
print(dos.gett_clean())
#esa pregunta teorica no tengo ni idea, la libreria typing se usa para asegurar que nuestra intencion es poner ese tipo de valores como parametros
#no se como filtrar los ceros...!=0 iba a hacer esto pero lo has prohibido
#estas seguro que esa pregunta es la que le harian a un candidato de data analyst?
#
#ejercicio2
ecommerce_payload = {
    "campaign_alpha": {"clicks": 1200, "conversions": 45, "revenue": None},
    "campaign_beta": {"clicks": 0, "conversions": 0, "revenue": 1500.50},
    "campaign_gamma": {"clicks": 3400, "conversions": 120, "revenue": 4500.0}
}
print(type(ecommerce_payload))
class ECommerceAnalyzer:
    def __init__(self,ecommerce_payload:Dict[str,Dict[str,anyy]]):
        self.__ecommerce_payload=ecommerce_payload
    def get_valid_revenues(self):
        
        return[num 
               for campaña in self.__ecommerce_payload.values() 
               for num in campaña.values() if num]
tres=ECommerceAnalyzer(ecommerce_payload)
print(tres.get_valid_revenues()) 

#ejercicio3
pharmacy_batches = (
    [{"item": "Paracetamol", "qty": 50, "urgent": True}, {"item": "Ibuprofen", "qty": 0, "urgent": False}],
    [{"item": "Omeprazol", "qty": 20, "urgent": False}, {"item": "", "qty": None, "urgent": True}],
    [{"item": "Aspirina", "qty": 15, "urgent": True}, {"item": "Amoxicilina", "qty": 5, "urgent": False}]
)
from typing import Tuple,List,Dict,Any
class PharmacyBatchAnalyzer:
    def __init__(self,pharmacy_batches:Tuple(List[dict[str,any]])):
        self.__pharmacy_batches=pharmacy_batches
    def get_critical_urgent_items(self):
        lista1=list(self.__pharmacy_batches)
        return[diccionario["item"]
               for listas in lista1
               for diccionario in listas 
               if diccionario["qty"] and diccionario["urgent"] is True]
cuatro=PharmacyBatchAnalyzer(pharmacy_batches)
print(cuatro.get_critical_urgent_items())
#empezar a incorporar el desempaquetado for nombre, qty, urgent in [tuple(diccionario.values())]

#ejercicio4
store_transactions = {
    "branch_north": {"sales": 12500, "returns": 0, "manager": "Ana"},
    "branch_south": {"sales": 0, "returns": 150, "manager": "Luis"},
    "branch_east": {"sales": 8400, "returns": None, "manager": "Sofia"}
}
class StoreAnalyzer:
    def __init__(self,store_transactions:Dict[str,Dict[str,Any]]):
        self.__store_transactions=store_transactions
    def get_valid_sales(self):
        return[sales
               for branch in store_transactions.values()
               for sales,returns,manager in [tuple(branch.values())]
               if sales]
cinco=StoreAnalyzer(store_transactions)
seis=cinco.get_valid_sales()
print(seis)       

#ejercicio5
incoming_batch = [
    {"product": "Aspirina", "stock": "100", "price": 4.5},
    {"product": "Paracetamol", "stock": "error_valor", "price": 2.0},
    {"product": None, "stock": 50, "price": 12.0},
    {"product": "Omeprazol", "stock": 200, "price": "10.5"}
]
class SecurePipeline:
    def __init__(self,incoming_batch:List[dict[str,any]]):
        self.__records=incoming_batch
    def process_safe_stocks(self):
        try:
            return[stock
                     for diccionario in self.__records
                     for product,stock,price in [tuple(diccionario.values())]
                     if type(stock) is int] 
        except Exception as error:
            print(error)
            print("ha habido un fallo")
siete=SecurePipeline(incoming_batch)
print(siete.process_safe_stocks())
         