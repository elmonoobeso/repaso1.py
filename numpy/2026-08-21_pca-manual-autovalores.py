import numpy as np
datos=np.genfromtxt(r"C:\Users\migue\Downloads\dataset_pca_practica.csv",delimiter=',',skip_header=1)
datos_cov=np.cov(datos.T)

autovalores,autovectores=np.linalg.eig(datos_cov)
autovalores=autovalores.real#evitamos o.j en el resultado los numeros complejos
#deberiamos hacer pca? np.cumsum

#ordenamos autovectores por autovalores
orden=np.argsort(autovalores)[::-1]#esto solo nos da indices, queremos valores
autovalores_orden=autovalores[orden]
varianza_exp=np.cumsum(autovalores_orden)/sum(autovalores_orden)*100
print(varianza_exp)
autovectores_ordenados=autovectores[:,orden]
top_6=autovectores_ordenados[:,:6]#filas no tocamos solo columnas, indexado con listas.realmente al hacer pca no quitamos columnas solo las combinaciones de datos de la matriz original que menos aportan, lo miramos con la linea de cumsum, y observamos que los 6 primeros explican mas del 95%
top_6=top_6.real
datos=datos.real
dataset_reducido=np.matmul(datos,top_6)
print(dataset_reducido.shape)
print(f"aqui va el bicho\n {dataset_reducido}")
#np.savetxt('resultado_pca.csv',dataset_reducido,delimiter=',',header='parm_1,parm_2,parm3,parm4,parm5,parm6',comments='')
datos_copia=datos.copy()
fraccion1=datos_copia[0:7,0:7]
fila_demax= np.max(fraccion1,axis=0)#maximos por columna
fraccion_fila=np.vstack([fraccion1,fila_demax])
max_total=np.max(fraccion1)
min_total=np.min(fraccion1)
columna_demax=np.max(fraccion_fila,axis=1).reshape(-1,1)#maximos por fila
fraccion_todo=np.hstack([fraccion_fila,columna_demax])
np.savetxt('resultado_fraccion',fraccion_todo,delimiter=',',comments='')
print(f"maximos y minimos:{max_total},{min_total}")
#practica con nan y mascaras
fraccion_nan=np.isnan(fraccion1)
condicion1= fraccion1<40
combi_mascaras= ~fraccion_nan & condicion1 


