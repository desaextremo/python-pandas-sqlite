from funciones_captura import *
from recipe import *

'''Programa para administrar recetas

Bienvenido al Administrador de Recetas

1. Agregar receta
2. Eliminar receta
3. Buscar receta por ID
4. Buscar receta por nombre
5. Listar todas las recetas
6. Salir

formato de nuestros datos:

{
    '1':{
        'nombre':'Tarta de Manzana',
        'categoria':'Postre',
        'ingredientes':['Manzanas','Azucar','Harina','Mantequilla'],
        'preparacion':'Mezclar ingredientes.......'
    },
    '2':{
        'nombre':'Spaghetti Bolognesse',
        'categoria':'Plato Principal',
        'ingredientes':['Spaghetti','Carne Molida','Tomate','Cebolla'],
        'preparacion':'Mezclar ingredientes.......'
    },
}
'''

def main():
    #imprime menu
    menu = '''Bienvenido al Administrador de Recetas

    1. Agregar receta
    2. Eliminar receta
    3. Buscar receta por ID
    4. Buscar receta por nombre
    5. Listar todas las recetas
    6. Salir

    Seleccione una opción\t'''
    opcion_seleccionada = 0

    #almacenar recetas
    diccionario_recetas = {
        '1':{
            'nombre':'Tarta de Manzana',
            'categoria':'Postre',
            'ingredientes':['Manzanas','Azucar','Harina','Mantequilla'],
            'preparacion':'Mezclar ingredientes.......'
        },
        '2':{
            'nombre':'Spaghetti Bolognesse',
            'categoria':'Plato Principal',
            'ingredientes':['Spaghetti','Carne Molida','Tomate','Cebolla'],
            'preparacion':'Mezclar ingredientes.......'
        },
    }
    id_siguiente=3 
    #ciclo de ejecucion
    while(opcion_seleccionada!=6):
        limpiar_pantalla()

        opcion_seleccionada = presenta_menu(menu,1,6)

        limpiar_pantalla()
        #1. Agregar receta
        if opcion_seleccionada==1:
            print("1. Agregar receta")

            #capturo los datos
            nombre = leer_cadena("Ingrese el nombre de la receta?\t","Debe ingresar el nombre de la receta...")
            categoria =  leer_cadena("Ingrese la categoría de la receta?\t","Debe ingresar la categoría de la receta...")
            ingredientes = []
            
            while True:
                ingrediente = leer_cadena("Ingrese un ingrediente, (SALIR para terminar)","Ingrese un ingrediente, o SALIR para terminar...")

                if ingrediente.upper() == "SALIR":
                    break

                ingredientes.append(ingrediente)

            preparacion = leer_cadena("Ingrese la preparacion de la receta?\t","Debe ingresar la preparacion de la receta...")

            
        #2. Eliminar receta        
        elif opcion_seleccionada==2:
            print("2. Eliminar receta")        
        #3. Buscar receta por ID
        elif opcion_seleccionada==3:
            print("3. Buscar receta por ID")
            id_receta = leer_cadena("Seleccione el id de la receta:","Debe selecciona un ide valido:")
            buscar_receta_por_id(diccionario_recetas,id_receta)
        #4. Buscar receta por nombre
        elif opcion_seleccionada==4:
            print("4. Buscar receta por nombre")
        elif opcion_seleccionada == 5:
            print("5. Listar todas las recetas")
            #llamado a la función para imprimir el listado de todas las recetas
            listar_recetas(diccionario_recetas)

        #6. Salir
        elif opcion_seleccionada == 6:
            print("6. Salir")
        else:
            print("Opción no permitida...")

        tiempo_espera(5)

if __name__=="__main__":
    main()