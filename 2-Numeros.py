# No, usar Python no te va a librar de los números

# Sabes lo que es un número, ¿no? Pues bien, Python interpreta los números sueltos como unidades numéricas...
# Pero no interpreta como números los que vayan dentro de un String o unidos a otro elemento como una función o una variable

# Los números son muy útiles en este lenguaje. Nor sirven para hacer operaciones, crear probabilidades, seleccionar elementos de una lista...
# Vamos a definir dos variables numéricas
a = 2
b = 3
# Ahora haremos operaciones básicas con ellas. Para ello, tienes una lista de signos aquí abajo:
# + para sumar
# - para restar
# * para multiplicar
# / para dividir
# ** para elevar a un exponente

# Pasaré los números a strings para que pueda dar la expresión matemática
print(str(a) + "+" + str(b) + "=" + str(a+b))
print(str(a) + "-" + str(b) + "=" + str(a-b))
print(str(a) + "*" + str(b) + "=" + str(a*b))
print(str(a) + "/" + str(b) + "=" + str(a/b))
print(str(a) + "^" + str(b) + "=" + str(a**b))

print("----------------") # ¡Hola de nuevo, separadores!

# Los números también nos sirven para llamar a un elemento de un array, pero hay un pequeño problema
# Nosotros empezamos contando desde 1, en plan; 1, 2, 3..., n; siendo 1 el primer elemento y n el último
# Python empieza desde 0, en plan; 0, 1, 2..., n; siendo el elemento 0 el primero de la lista y n el último
# Volvamos a los coches
coches = [
    "Toyota",
    "Renault",
    "Mercedes",
    "Audi",
    "Fiat",
    "Peugeot"
]
# Ahora llamaremos a uno de los elementos de la lista con [num] siendo num el número del elemento dentro de la lista
print("Quiero un " + coches[0])

# Usaremos los números en las siguientes prácticas, ya que los usaremos para hacer comparativas y bucles

# Hecho por Carlos, alumno de TIC de 2º de Bachillerato en el IES Auga da Laxe