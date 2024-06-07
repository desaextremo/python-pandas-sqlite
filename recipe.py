def agregar_receta(diccionario_recetas,id_siguiente):
    #convierte el numero a cadena
    id_receta = str(id_siguiente)
    

def listar_recetas(diccionario_recetas):
    #validar si recibio el diccionario con las recetas
    if diccionario_recetas:
        print("Listado de Recetas")
        for id_receta,receta in diccionario_recetas.items():
            print(f"-ID {id_receta} Nombre: {receta['nombre']} Categoría : {receta['categoria']}")
    else:
        print("Aun no hay recetas")

def buscar_receta_por_id(diccionario_recetas,id_receta):
    if id_receta in diccionario_recetas:
        receta = diccionario_recetas[id_receta]
        print(f"-ID {id_receta} Nombre: {receta['nombre']} Categoría : {receta['categoria']}")
    else:
        print(f"No existe una receta con el id {id_receta}, por favor verifique...")