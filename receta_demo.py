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
    preparacion = input("Ingrese los pasos de preparación de la receta: ")
    diccionario_recetas[id_receta] = {
        'nombre': nombre_receta,
        'categoria': categoria,
        'ingredientes': ingredientes,
        'preparacion': preparacion
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
        print(f"Receta '{receta['nombre']}' ({receta['categoria']}):")
        print(f"Ingredientes: {', '.join(receta['ingredientes'])}")
        print(f"Preparación: {receta['preparacion']}")
    else:
        print("La receta no existe.")

def buscar_receta_por_nombre(diccionario_recetas):
    nombre_receta = input("Ingrese el nombre de la receta que desea buscar: ").lower()
    for receta in diccionario_recetas.values():
        if receta['nombre'].lower() == nombre_receta:
            print(f"Receta '{receta['nombre']}' ({receta['categoria']}):")
            print(f"Ingredientes: {', '.join(receta['ingredientes'])}")
            print(f"Preparación: {receta['preparacion']}")
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
    diccionario_recetas =  {
        '1': {
            'nombre': 'Tarta de Manzana',
            'categoria': 'Postre',
            'ingredientes': ['Manzanas', 'Azúcar', 'Harina', 'Mantequilla'],
            'preparacion': 'Mezclar ingredientes, hornear a 180 grados por 45 minutos.'
        },
        '2': {
            'nombre': 'Spaghetti Bolognese',
            'categoria': 'Plato Principal',
            'ingredientes': ['Spaghetti', 'Carne Molida', 'Tomate', 'Cebolla', 'Ajo'],
            'preparacion': 'Cocinar los ingredientes, servir caliente con queso parmesano.'
        },
        '3': {
            'nombre': 'Ensalada César',
            'categoria': 'Ensalada',
            'ingredientes': ['Lechuga', 'Pollo', 'Croutones', 'Queso Parmesano', 'Aderezo César'],
            'preparacion': 'Mezclar los ingredientes en un bol grande y añadir el aderezo.'
        },
        '4': {
            'nombre': 'Sopa de Tomate',
            'categoria': 'Sopa',
            'ingredientes': ['Tomates', 'Cebolla', 'Ajo', 'Caldo de Pollo', 'Crema'],
            'preparacion': 'Cocinar tomates, cebolla y ajo. Añadir caldo y crema, luego licuar.'
        },
        '5': {
            'nombre': 'Pizza Margherita',
            'categoria': 'Plato Principal',
            'ingredientes': ['Masa de Pizza', 'Tomate', 'Mozzarella', 'Albahaca', 'Aceite de Oliva'],
            'preparacion': 'Extender la masa, añadir ingredientes y hornear a 220 grados por 15 minutos.'
        },
        '6': {
            'nombre': 'Brownies de Chocolate',
            'categoria': 'Postre',
            'ingredientes': ['Chocolate', 'Azúcar', 'Harina', 'Huevos', 'Mantequilla'],
            'preparacion': 'Mezclar ingredientes, hornear a 180 grados por 25 minutos.'
        },
        '7': {
            'nombre': 'Tacos de Pollo',
            'categoria': 'Plato Principal',
            'ingredientes': ['Tortillas', 'Pollo', 'Cebolla', 'Cilantro', 'Lima'],
            'preparacion': 'Cocinar el pollo, servir en tortillas con cebolla, cilantro y un toque de lima.'
        },
        '8': {
            'nombre': 'Smoothie de Fresas',
            'categoria': 'Bebida',
            'ingredientes': ['Fresas', 'Banana', 'Yogur', 'Miel'],
            'preparacion': 'Mezclar todos los ingredientes en una licuadora hasta obtener una mezcla suave.'
        },
        '9': {
            'nombre': 'Guacamole',
            'categoria': 'Aperitivo',
            'ingredientes': ['Aguacates', 'Tomate', 'Cebolla', 'Cilantro', 'Lima'],
            'preparacion': 'Triturar aguacates y mezclar con tomate, cebolla, cilantro y jugo de lima.'
        },
        '10': {
            'nombre': 'Panqueques',
            'categoria': 'Desayuno',
            'ingredientes': ['Harina', 'Leche', 'Huevos', 'Azúcar', 'Polvo de Hornear'],
            'preparacion': 'Mezclar ingredientes, verter en sartén caliente y cocinar hasta dorar.'
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
