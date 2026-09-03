import pandas as pd
import numpy as np
import requests
import json
from pathlib import Path
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.environ["Gemini_API_KEY"])

url="https://api.fda.gov/drug/enforcement.json"
params={"limit": 100}#filtro tipo query, pero no es SQL, puedo por ejemplo filtrar por tipo de medicamento.
def obtencion_datos(url,params):
    try:
        respuesta=requests.get(url,params=params,timeout=15)
        respuesta.raise_for_status()
        datos=respuesta.json()
        return datos["results"]
    except requests.exceptions.Timeout:
        print("la respuesta tardo demasiado")
    except requests.exceptions.HTTPError as error:
        print(f"Error HTTP: {error}")
    except requests.exceptions.ConnectionError:
        print("No se pudo conectar con la A")
    

class AgenteFDA:
    def __init__(self):
        self.datos=None
        self.memoria=[{"role":"system","content":"Eres un analista regulatorio con formación farmacéutica. Tu objetivo es interpretar los datos de alertas y retiradas de medicamentos de la FDA que te proporciona el script, y explicar en lenguaje claro qué patrones o riesgos son relevantes para un farmacéutico."}]
    def agregar_mensaje_usuario(self, mensaje):
        self.memoria.append({"role":"user","content":mensaje})
    def respuesta_agente(self, respuesta):
        self.memoria.append({"role":"analista","content":respuesta})
    def obtener_memoria_completa(self):
        return self.memoria


    def obtener_datos(self):
        self.datos=obtencion_datos(url,params)
    def validar_clases(self):
        valor_error=[]
        clave_error=[]
        no_validos=[]
        error_varios=[]
        validos_clase=[]
        validos_no_vac=[]
        for registro in self.datos:
            try:
                if registro["classification"] in ["Class I","Class II","Class III"]:
                    validos_clase.append(registro)
                else:
                    no_validos.append(registro)
                    
                if not None in  [registro["product_description"],registro["reason_for_recall"],registro["recalling_firm"]]:
                    validos_no_vac.append(registro)

                else:
                    no_validos.append(registro)
            except ValueError as error:
                valor_error.append(error)
            except KeyError as error:
                clave_error.append(error)
            except Exception as error:
                error_varios.append(error)
        return(valor_error,clave_error,no_validos,error_varios,validos_clase,validos_no_vac)
    def analisis_estadistico(self,valor_error,clave_error,no_validos,error_varios,validos_clase,validos_no_vac):
        df1=pd.DataFrame(no_validos)
        df2=pd.DataFrame(validos_no_vac)
        df3=pd.DataFrame(validos_clase)
        df_errores=pd.DataFrame(error_varios)
        analisis_nov=pd.DataFrame({"Tipodato":df2.dtypes,"no_nulos":df2.count(),"nulos":df2.isnull().sum()})
        if df2.empty:
            analisis_clasificacion=pd.Series(dtype="int64")
            analisis_farmaceutica=pd.Series(dtype="int64")
        else:
            analisis_clasificacion=df2.groupby("classification")["reason_for_recall"].count()
            analisis_farmaceutica=df2.groupby("recalling_firm")["classification"].count()
        if df_errores.empty:
            analisis_errores=pd.DataFrame()
        else:
            analisis_errores=df_errores.describe()
        analisis_nc=df3.describe()
        analisis_farm=df3.groupby("recalling_firm")["reason_for_recall"].count()

        analisis={"info":analisis_nov,"analisis_clasificacion":analisis_clasificacion,"analisis_farmaceutica":analisis_farmaceutica,"analisis_errores":analisis_errores,"analisisdf3":analisis_nc,"analisisdf3":analisis_farm}
        return analisis

    def exportar_resultados(self, analisis):
        
        carpeta=Path("analisis_es")
        carpeta.mkdir(exist_ok=True)
        with pd.ExcelWriter(carpeta/"analisis.xlsx") as writer:
            for nombre_hoja, tabla in analisis.items():
                tabla.to_excel(writer,sheet_name=nombre_hoja)
    def interpretar_analisis(self, analisis):
        resumen_texto = ""
        for nombre_hoja, tabla in analisis.items():
            resumen_texto += f"\n\n--- {nombre_hoja} ---\n{tabla.to_string()}"
        self.agregar_mensaje_usuario(
            f"Aquí tienes el análisis de recalls de la FDA. Explícame qué es lo más relevante:{resumen_texto}")
        prompt = self.memoria[0]["content"] + "\n\n" + self.memoria[-1]["content"]
        modelo = genai.GenerativeModel("gemini-flash-latest")
        respuesta = modelo.generate_content(prompt)
        self.respuesta_agente(respuesta.text)
        return respuesta.text
if __name__ == "__main__":
    agente = AgenteFDA()
    agente.obtener_datos()
    resultados = agente.validar_clases()
    analisis = agente.analisis_estadistico(*resultados)
    agente.exportar_resultados(analisis)
    interpretacion = agente.interpretar_analisis(analisis)
    print(interpretacion)

        





        

