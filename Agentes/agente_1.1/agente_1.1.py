import numpy as np


class Agente:
    def __init__(self,ventas=None,cod_estupes=None):
        self.ventas=ventas
        self.cod_estupes= cod_estupes or {"N02AA01","N02AA02","N02AA03","N02AA05","N02AA59","N02AB02","N02AB03","N02AC03","N02AE01","N02AX02","N02AX06","N01AH01","N01AH02","N01AH03","N01AH06"}


    def cargar(self,ruta_archivo="ventas_mes.csv"):
      self.ventas=np.genfromtxt(ruta_archivo,delimiter=",",dtype=None,names=True, encoding="utf-8")

    def detectar_stock_negativo(self):
      lista_stock_negativo=[]
      nombre_med=np.array(self.ventas["nombre_medicamento"],dtype=str)
      codigo_med=np.array(self.ventas["codigo_nacional"],dtype=str)
      stocks=np.array(self.ventas["stock_actual"], dtype=int)
      codigos_unicos= np.unique(codigo_med)

      for venta in codigos_unicos:
         filtro=codigo_med==venta
         stock_filtrado=stocks[filtro][-1]
         if stock_filtrado<0:
            ultimo_nombre=nombre_med[filtro][-1]
            lista_stock_negativo.append({"nombre_medicamento":ultimo_nombre,"codigo_nacional":venta,"stock":int(ultimo_stock)})

      return lista_stock_negativo


    def abuso_estupes(self,limite_estupes=10):
       lista_abuso=[]

       estupes=np.isin(self.ventas["cod_estupes"],list(self.cod_estupes))
       sub=self.ventas[estupes]
       clientes=np.unique(sub["id_paciente"])
       for cliente in clientes:
          ventas_cliente = sub[sub["id_paciente"] == cliente]
          suma = np.sum(ventas_cliente["cantidad"])

          if suma>limite_estupes:
             meds_unicos = ", ".join(np.unique(ventas_cliente["nombre_medicamento"]))
             cods_unicos = ", ".join(
                np.unique(np.array(ventas_cliente["codigo_nacional"], dtype=str)))
             lista_abuso.append({"id_paciente":cliente,"nombre_medicamento":meds_unicos,"cantidad":suma,"codigo_nacional":cods_unicos})
       return lista_abuso

    def anomalias_precio(self, margen_precio_para=0.25,margen_precio=0.05):
       lista_precio=[]
       nombre_med=np.array(self.ventas["nombre_medicamento"],dtype=str)
       codigo_med=np.array(self.ventas["codigo_nacional"],dtype=str)
       precio_med=np.array(self.ventas["puc"],dtype=float)
       codigo_med_unico=np.unique(codigo_med)
       for venta in codigo_med_unico:
         filtro=codigo_med==venta
         precio_filtrado=precio_med[filtro]
         if len(precio_filtrado)>1:
            media=np.mean(precio_filtrado)
            if venta.startswith(("6","7")):
               umbral=margen_precio
            else:
               umbral=margen_precio_para
            #calculo variacion
               variacion=np.std(precio_filtrado, ddof=1)/ media
              #cual es la razon por la que se compara con la media, ya no hay que pasarlo a porcentaje?
         if variacion>umbral:
                  lista_precio.append({"nombre":nombre_med[filtro][0],"codigo_nacional":venta,"Precio max":np.max(precio_filtrado),"Precio min":np.min(precio_filtrado),"variacion":round(variacion*100,2)})
    return lista_precio

from pathlib import Path
import csv
    def extraer_listas(self,lista_stock_negativo,lista_abuso,lista_precio):
      ruta=Path("listas_agente")
      ruta.mkdir(parents=True, exist_ok=True)
      ruta_abuso=ruta/"lista_abuso.csv"
      ruta_stock=ruta/"lista_stock_negativo.csv"
      ruta_precio=ruta/"lista_precio.csv"
      with open (ruta_abuso,"w",newline="",encoding="utf-8") as abuso_file:
         writer=csv.DictWriter(abuso_file, fieldnames=["id_paciente","nombre_medicamento","cantidad","codigo_nacional"])
         writer.writeheader()
         writer.writerows(lista_abuso)
      with open (ruta_stock,"w",newline="",encoding="utf-8") as stock_file:
         writer=csv.DictWriter(stock_file, fieldnames=["nombre_medicamento","codigo_nacional","stock"])
         writer.writeheader()
         writer.writerows(lista_stock_negativo)
      with open (ruta_precio,"w",newline="",encoding="utf-8") as precio_file:
         writer=csv.DictWriter(precio_file, fieldnames=["nombre","codigo_nacional","Precio max","Precio min","variacion"])
         writer.writeheader()
         writer.writerows(lista_precio)
