#DIFERENTES TIPOS DE ARRAYS, LISTA [], TUPLA (), SET {} y DICCIONARIO
lista = ["Roberto", "Mendoza", True, 185]
#print (lista) omitimos este print
lista[1] = "sanjuan"
lista[3] = "Caracol"
#print (f"Este es el resultado de la lista: {lista}\n") omitimos este print

tupla = ("Juan", "Hernandez", False)
#print (f"Este es el resultado de la tupla: {tupla}\n") omitimos este print

#La lista se puede modificar (variable), y la tupla no se puede modificar (constante)

#creando el set (conjunto)
conjunto = {"Roberto", "Mendoza", True, 185, 185}
#print (conjunto) omitimos este print
#en un conjunto no se pueden tener datos iguales, y no se acceden a los elementos por indices, solo se acceden con bucles adicional de que los datos te los muestra revueltos

#se crea un diccionario
diccionario = {
    "nombre" : "Roberto",
    "Apellido" : "Martinez",
    "Vivo?" : True,
    "Edad" : 27,
    "dato_duplicado" : "Roberto"
}

print (diccionario["Apellido"])
#Para el diccionario se accede con el elemento directo p.e. "nombre" : "Roberto", donde la estructura es key : value