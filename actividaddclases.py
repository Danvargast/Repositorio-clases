#Numeros
import random
numerosAleatorios = [random.randint(1,100),random.randint(1,100)]
suma = sum(numerosAleatorios)
numeroUsuario = int(input("Intenta adivinar la suma de los números: "))
if numeroUsuario == suma:
    print(f"Adivinaste la respuesta, los numeros eran {numerosAleatorios[0]} y {numerosAleatorios[1]}")
else: 
    print("Número equivocado")
#vocales
vocales = ["a","e","i","o","u"]
palabra = input("Ingrese una cadena de texto: ").lower()
contador = 0
for vocal in vocales:
    for letra in palabra:
        if i == letra:
            contador +=1

print(contador)