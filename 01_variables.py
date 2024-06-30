# Variables
str_variable = 'My string variable'
print(str_variable)

int_variable = 46
print(int_variable)

int_to_str_variable = str(int_variable)
print(int_to_str_variable)
print(type(int_to_str_variable))

bool_variable = True
print(bool_variable)

# Concatenación de variables
print(str_variable, int_to_str_variable, bool_variable)
print("Este es el valor de:", bool_variable)

# Funciones del Sistema
print(len(str_variable)) # Cuenta los caracteres

# Variables en una sola línea
name, surname, alias, age = "Marcos", "Pérez", "socramdev", 46
print("Nombre:", name, surname, ". Edad:", age,". Alias:", alias)

# Inputs
name = input("What is your name?: ")
age = input("How old are you?: ")
print(name)
print(age)

# Cambiamos el tipo de datos de la variable
name = 35
age = "Marcos"
print(name)
print(age)

# ¿Forzamos el tipo? Sólo es visual para quien escriba el código
address: str = "Pablo Neruda"
address = 1
print(address)