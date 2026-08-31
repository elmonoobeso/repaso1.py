from pathlib import Path
import csv
import numpy as np

csv_prueba=Path(r"C:\Users\migue\Downloads\ventas_farmacia.csv")
ruta=csv_prueba/"ventas_farmacia"
with open(csv_prueba,"r",newline="",encoding="UTF-8") as ventas:
     escritor=csv.reader(ventas)
     limpio=next(escritor,None)
     primero=np.array(limpio)
     rango=limpio.range()
     unos=np.ones((5,5),dtype='int32')
     copia_unos=np.full_like(unos,5)
     aleatorio=np.random.randint(0,8,0,8)
     dimension=np.ndim(limpio)
     forma=limpio.shape()
     item=np.itemsize(limpio)
     precio_stock=limpio[:2,4]
     copia_slice=np.copy(precio_stock)
     copia_slice=5

     
