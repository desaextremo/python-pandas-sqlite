import sqlite3
import pandas as pn
import random
from funciones_captura import limpiar_pantalla

limpiar_pantalla()


def generar_nota():
    return round(random.uniform(1.0,5.0),1)

def generar_edad(id):
    if id % 2 == 0:
        return random.randint(18,41)
    else:
        return None

conexion = sqlite3.connect("g11.db")

dataframe_g11 = pn.read_sql("SELECT * FROM estudiantes",conexion)

print(f"Antes de:\n\n{dataframe_g11}")

#apply=> recorrer un dataframe ejecutando una funcion o condicion en filas o columna
#dataframe.apply(funcion anonima parametro: funcion o condicion, axis=1)  axis=0 columnas axis=1 filas
dataframe_g11['edad']  = dataframe_g11.apply(lambda fila:generar_edad(fila['id']),axis=1)

#Agregar columnas <nombre del dataframe>['nombre nueva columna'] = 'valor'
dataframe_g11['nota1'] = dataframe_g11.apply(lambda fila:generar_nota(),axis=1)
dataframe_g11['nota2'] = dataframe_g11.apply(lambda fila:generar_nota(),axis=1)
dataframe_g11['nota3'] = dataframe_g11.apply(lambda fila:generar_nota(),axis=1)
dataframe_g11['definitiva'] = round((dataframe_g11['nota1'] * .30) + (dataframe_g11['nota2'] * .30)  + (dataframe_g11['nota3'] * .40) / 3,2)


#Filtrar estudiantes que pasan
pasaron = dataframe_g11[dataframe_g11['definitiva'] >= 3]

#Filtrar estudiantes que reprueban
reprueban = dataframe_g11[dataframe_g11['definitiva'] < 3]

print(f"pasaron de:\n\n{pasaron}")

print(f"reprueban de:\n\n{reprueban}")
