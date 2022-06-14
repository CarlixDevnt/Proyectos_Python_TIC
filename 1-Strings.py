# Hoy haremos cosas básicas con strings

# Los Strings generalmente son unidades textuales o numéricas que van entre comillas y que se interpretan como textos
# Si no pones las comillas, se interpretará como una variable no definida, por lo que te dará un error. En ese caso, debes definir la variable

# Aquí defino la variable str como "Hola, soy un String", por lo que cada vez que usemos esa variable, nos referiremos al string definición
variable = "Hola, soy un String"

# Ahora vamos a probar a imprimir la variable. Hazlo usando la función print(), y no olvides los paréntesis, en la práctica 3 explico por qué son importantes
print(variable)

print("----------------") # Esto es un separador que pongo por si ejecutas el código, no le hagas mucho caso

# Un String puede tener varias líneasn simplemente debes poner \n dentro del String en el punto donde quieras crear la nueva línea
print("Ave María, ¿cuándo serás mía?\nSi me quisieras, todo te daría")

print("----------------") # Esto es otro separador

# También podemos meter un string dentro de otro String para crear variaciones del String original
# Definiremos un nombre antes
name = "Carlos"
# Ahora lo imprimimos
print("Hola, mi nombre es " + name)

print("----------------") # Y... otro separador

# Podemos convertir algunas cosas a Strings con la función str(), como Numbers (Números)
suma = 3+7
resultado = str(suma)
print(resultado)

print("----------------") # Creo que a estas alturas ya sabes qué es esto

# También podemos personalizar nuestros strings al recibir una entrada. Esto se hace con las funciones input() y str()
print("ADRIÁN - ¿Dónde estás?")
# Primero definimos la entrada. La función input requiere un parámetro textual
location = input("Escribe tu ubicación para responder: ")
# Pasamos la entrada a String
place = str(location)
print("TÚ - Estoy en " + place)

# Felicidades, acabas de hacer unos diálogos para un juego, o para hacer Whatsapp 2

# También puedes agrupar elementos como Strings en listas llamadas Arrays o Arreglos, representados por []
coches = [
    "Toyota", # Cada elemento debe ir separado por una coma
    "Renault",
    "Mercedes",
    "Audi",
    "Fiat",
    "Peugeot" # Podemos añadir más elementos al array o quitar algunos de los que ya tenga
]
# Usaremos los Arrays en las siguientes prácticas, ya que necesitamos saber sobre números y funciones

# Hecho por Carlos, alumno de TIC de 2º de Bachillerato en el IES Auga da Laxe