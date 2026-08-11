from pathlib import Path
import csv
dataset=Path(r"C:\Users\migue\Downloads\repaso1.py\dataset")
ruta=dataset/"inventario_diario.csv"
class CSVAnalyzer:
    def __init__(self,ruta):
        self.__file_path=ruta
    def get_valid_stocks(self):
        with open(self.__file_path,"r",newline='',encoding="utf-8") as inventario:
             reader=csv.reader(inventario)
             columna=next(reader,None)
             validos=[]
             for linea in reader:
                if linea:
                     validos.append(linea)
             return

            
        
    def parseo(self):
        total=lambda stock,precio:stock*precio
        with open(self.__file_path,"r",newline='',encoding="utf-8") as inventario:
                reader=csv.reader(inventario)
                next(reader,None)
                resultado=[]
                errores=[]
                for line in reader:
                     try:
                          nombre,stock,precio=line
                          stock_int=int(stock)
                          precio_flo=float(precio)
                          calculo=total(stock_int,precio_flo)
                          resultado.append(calculo)
                          print(f"Producto: {nombre}, total:{calculo}")
                          
                     except Exception as error:
                          errores.append(error)
                print(errores,resultado)
                return

prueba=CSVAnalyzer(ruta)
prueba.parseo()
        
                        

                          
        