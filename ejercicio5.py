"""
Caso 1: Nombre con Mayor Cantidad de Caracteres
Escriban un programa en Python que permita a los usuarios ingresar 3 nombres por
pantalla y almacenarlos en una lista. Luego, el programa debe determinar y mostrar el
nombre que tiene la mayor cantidad de caracteres en un mensaje de salida por pantalla.

Caso 2: Nombres y Apellidos Ordenados
Creen dos listas, una para nombres y otra para apellidos. Almacenen 3 nombres y 3
apellidos en estas listas. Luego, muestren de forma ordenada los nombres y apellidos.

Caso 3: Agregar Nombres y Eliminar el Menos Extenso
Creen un programa que permita almacenar nombres en una lista. El sistema debe
preguntar si desean agregar otro nombre y seguir permitiendo la entrada de nombres
hasta que la respuesta sea "no". Después de ingresar n nombres, eliminen el nombre con
la menor cantidad de caracteres.


"""
#caso 1

nombres = []
for i in range(3):
   nombre = input("ingrese un nombre  :")
   nombres.append(nombre)

nombreMasLargo=max(nombres, key=len)
print("el nombre con mas caracteres es ", nombreMasLargo)
# caso 2

nombres1 = []
apellidos = []
for i in range (3):
   nombre1= input("ingrese un nombre :")
   apellido= input("ingrese un apellido :")
   nombres1.append(nombre1)
   apellidos.append(apellido) 
nombres.sort()
apellidos.sort()
print("nombres ordenados  :")
for nombre1,apellido in zip(nombres1,apellidos):
   print(nombre1,apellido)
# caso 3

nombres2= []
respuesta = "s"
while respuesta.lower()== "s":
   nombre2 =input("ingrese un nombre :  ")
   nombres2.append(nombre2)
   respuesta = input("desea agregar otro nombre?  s/n :")
nombre_menos_extenso = min(nombres2,key=len)
nombres2.remove(nombre_menos_extenso)
print ("nombres despues de eliminar el mas corto  :",nombres2)    
