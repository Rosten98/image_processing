import numpy as np

array = np.array([1,2,3,4,5])
# print(array)
print(type(array))
print(array.ndim)  # Dimension
print(array.shape) # (5,) -> 5 columnas

array = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
])
# print(array)
print(array.ndim)  # Dimension
print(array.shape) # (2, 5) -> 2 filas con 5 columnas
print(array.dtype) # Type of the array contents

# Crear matrices
print(np.zeros([3, 3])) # Matriz de zeros de 3 x 3
print(np.ones([2, 3])) # Matriz de unos de 3 x 3
print(np.eye(2)) # matriz de identidad

### OPERACIONES ###
# Suma/resta -> Mismo numero de dimensiones
# Multiplicación/Division/Potencia -> Numero de columnas
# del primer array coincide con numero de filas del segundo 
