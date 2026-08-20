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
np.savetxt('resultado_pca.csv',dataset_reducido,delimiter=',',header='parm_1,parm_2,parm3,parm4,parm5,parm6',comments='')


