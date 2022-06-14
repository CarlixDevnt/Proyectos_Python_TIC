# No te asustes por ver el título, aquí las funciones son mucho más útiles

# Una función te sirve para ejecutar un código dependiente de una serie de parámetros.
# Para definir una función se usa la palabra def de la siguiente manera
def miFuncion(): # Es importante pegar unos paréntesis al lado del nombre de la función, sirven para identificarla como tal y para especificar parámetros
# Vamos a hacer una función matemática para elevar al cuadrado (lo siento)
    entry = input("Escribe un número para elevar al cuadrado: ") # Importantísimas las tabulaciones. Dependiendo de ellas depende el contenido de la función
    num = int(entry)
    print(num**2)

# Ahora ejecutaremos la función con llamarla
miFuncion()

print("----------------")

# Python posee muchas funciones predefinidas, como print(), if(), str()...
# Una función distinta es for. Sirve para crear bucles y tiene la siguiente estructura:
# for x in rango, donde x es un elemento y rango es el número de veces que se va a hacer el bucle
# Gracias a esto, podemos saber qué elementos hay en una lista. Volvamos a los coches
coches = [
    "Toyota",
    "Renault",
    "Mercedes",
    "Audi",
    "Fiat",
    "Peugeot"
]
# Vamos a ver cuántos elementos hay en la lista usando la función len() (para imprimirla la pondré dentro de otra función str()), y vamos a imprimir cada uno de ellos
print("Hay " + str(len(coches)) + " elementos en el Array \"coches\"")
for element in coches: # Esto quiere decir "por cada elemento en el array coches"
    print(element) # Imprime cada elemento

print("----------------") # Una vez más, la importancia de las tabulaciones para que el separador no forme parte del bucle

# Puedes usar los bucles para repetir un proceso en un rango (función range()) de veces
for i in range(1, 10):
    print("Hola, soy un programa acosador")



# Hecho por Carlos, alumno de TIC de 2º de Bachillerato en el IES Auga da Laxe