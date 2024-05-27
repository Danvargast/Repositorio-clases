informacion = ("Daniel Vargas", 20, "Puerto Montt")
print(informacion[0])
print(informacion[1])
print(informacion[2])
nombre,edad,ciudad = informacion
print(nombre)
print(edad)
print(ciudad)
numeros = (1,2,3,4,5,6,7,8,9,10)
suma = sum(numeros)
maximo = max(numeros)
minimo = min(numeros)
numero_5 = numeros.count(5)
print(suma)
print(maximo)
print(minimo)
print(numero_5)
letras = ("a","b","c","d","e","f","g","h","i","j")
primerasLetras = letras[:5]
ultimasLetras = letras[:-4:-1]
rebanadoSaltos = letras[::2]
print(primerasLetras)
print(ultimasLetras)
print(rebanadoSaltos)