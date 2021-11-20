# [1, 1 ,2,2,4]
""" los conjuntos """
list = [1, 1 ,2,2,4]
my_set1= {3,"hola", "mi amor",2}
my_set2 = {2,"hola", 5, 8 , "Adri"}

# print(type(my_set1))

# # la union junta los 2 conjuntos y si hay repetidos solo muestra 1 
# my_setunion = my_set1 | my_set2
# print(my_setunion)

# #interseccion solo muestra los comunes de cada cojunto 
# my_setinterseccion = my_set1 & my_set2
# print(my_setinterseccion)

# #diferencia quitar todos los elementos que estan en un conjunto iguales o no  y dejar solo los que son unicos de ese conjunto

# my_setdiferencia1 = my_set1 - my_set2
# print(my_setdiferencia1)
# my_setdiferencia2 = my_set2 - my_set1
# print(my_setdiferencia2)

# #Diferencia simetrica la union de los 2 conjuntos sin los que se comparten
# my_set_direncia_simetrica = my_set1 ^ my_set2
# print(my_set_direncia_simetrica)

myset = set(list)
print(myset)


