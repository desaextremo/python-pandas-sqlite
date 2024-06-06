def mostrar_menu():
    print("\nBienvenido al Administrador de Recetas")
    print("1. Agregar receta")
    print("2. Eliminar receta")
    print("3. Buscar receta por ID")
    print("4. Buscar receta por nombre")
    print("5. Listar todas las recetas")
    print("6. Salir")

def agregar_receta(diccionario_recetas, siguiente_id):
    id_receta = str(siguiente_id)
    nombre_receta = input("Ingrese el nombre de la nueva receta: ")
    categoria = input("Ingrese la categoría de la receta: ")
    ingredientes = []
    while True:
        ingrediente = input("Ingrese un ingrediente (o 'done' para terminar): ")
        if ingrediente.lower() == 'done':
            break
        ingredientes.append(ingrediente)
    diccionario_recetas[id_receta] = {
        'nombre': nombre_receta,
        'categoria': categoria,
        'ingredientes': ingredientes
    }
    print(f"Receta agregada con el ID {id_receta}.")
    return siguiente_id + 1

def eliminar_receta(diccionario_recetas):
    id_receta = input("Ingrese el ID de la receta que desea eliminar: ")
    if id_receta in diccionario_recetas:
        del diccionario_recetas[id_receta]
        print(f"Receta con ID {id_receta} eliminada.")
    else:
        print("La receta no existe.")

def buscar_receta_por_id(diccionario_recetas):
    id_receta = input("Ingrese el ID de la receta que desea buscar: ")
    if id_receta in diccionario_recetas:
        receta = diccionario_recetas[id_receta]
        print(f"Receta '{receta['nombre']}' ({receta['categoria']}): {', '.join(receta['ingredientes'])}")
    else:
        print("La receta no existe.")

def buscar_receta_por_nombre(diccionario_recetas):
    nombre_receta = input("Ingrese el nombre de la receta que desea buscar: ").lower()
    for receta in diccionario_recetas.values():
        if receta['nombre'].lower() == nombre_receta:
            print(f"Receta '{receta['nombre']}' ({receta['categoria']}): {', '.join(receta['ingredientes'])}")
            return
    print("La receta no existe.")

def listar_recetas(diccionario_recetas):
    if diccionario_recetas:
        print("Recetas:")
        for id_receta, receta in diccionario_recetas.items():
            print(f"- ID: {id_receta}, Nombre: {receta['nombre']}, Categoría: {receta['categoria']}")
    else:
        print("No hay recetas.")

def main():
    # Recetas iniciales
    diccionario_recetas = {
        '1': {
            'nombre': 'Tarta de Manzana',
            'categoria': 'Postre',
            'ingredientes': ['Manzanas', 'Azúcar', 'Harina', 'Mantequilla']
        },
        '2': {
            'nombre': 'Spaghetti Bolognese',
            'categoria': 'Plato Principal',
            'ingredientes': ['Spaghetti', 'Carne Molida', 'Tomate', 'Cebolla', 'Ajo']
        }
    }
    siguiente_id = 3
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            siguiente_id = agregar_receta(diccionario_recetas, siguiente_id)
        elif opcion == '2':
            eliminar_receta(diccionario_recetas)
        elif opcion == '3':
            buscar_receta_por_id(diccionario_recetas)
        elif opcion == '4':
            buscar_receta_por_nombre(diccionario_recetas)
        elif opcion == '5':
            listar_recetas(diccionario_recetas)
        elif opcion == '6':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

if __name__ == "__main__":
    main()
