#Generador de passwords

import random

letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
simbolos = ["!", "·", "$", "%", "&", "/", "?", "¿", "*"]

password_list = []
final_password = []



l = int(input("Cuantas letras quiere en su password?: "))
n = int(input("Cuantos números quiere en su password?: "))
s = int(input("Cuantas símbolos quiere en su password?: "))


for char in range(0, l):
    password_list += random.choice(letras)
for char in range(0, n):
    password_list += random.choice(numeros)
for char in range(0, s):
    password_list += random.choice(simbolos)

password_list = []

for char in range(0, l):
    password_list.append(random.choice(letras))
for char in range(0, n):
    password_list.append(random.choice(numeros))
for char in range(0, s):
    password_list.append(random.choice(simbolos))

random.shuffle(password_list)
password = ""
for char in password_list:
    password += char
print(f"El password generadoComo es: {password}")
