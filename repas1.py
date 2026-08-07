def invertir_palabras(frase:str):
    resultado=[]
    for word in frase.split():
        if len(word)>5:
            resultado.append(word[::-1])
        else:
            resultado.append(word)
        
    return (" ".join(resultado))#hemos aprendido a usar join para convertir una lista en un texto¡
frase ="Hola que tal estabamos coloreados"

#frase1="".join(frase)


prueba=invertir_palabras(frase)
print(prueba)




        