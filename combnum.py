#Combinanciones Numerica Poaibles

import itertools

# Pedimos al usuario que ingrese una serie de números separados por comas
nums = input("Ingrese una serie de números separados por comas: ")

# Convertimos la entrada en una lista de números
nums_list = list(map(int, nums.split(",")))

# Calculamos todas las posibles combinaciones
combos = list(itertools.permutations(nums_list))

# Mostramos la cantidad de combinaciones
print(f"Se pueden crear {len(combos)} combinaciones con los números ingresados.")

# Mostramos todas las combinaciones
for combo in combos:
    print(combo)

