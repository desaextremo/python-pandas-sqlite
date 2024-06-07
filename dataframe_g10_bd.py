from funciones_captura import limpiar_pantalla
from bd import update_estudiante
import pandas as pn
import sqlite3 
import random

limpiar_pantalla()
conexion = sqlite3.connect("g10.db")
dato_g10 = pn.read_sql("Select * from estudiantes",conexion)

def actualizar_edad(id):
    if id % 2 == 0:
        return random.randint(18,41)
    else:
        return None

print("_____________________________________________________")
print("     1  recorrer el dataframe for y iloc             ")
print("_____________________________________________________")
#1  recorrer el dataframe for y iloc
for i in range(len(dato_g10)):
    dato_g10.loc[i, 'edad'] = actualizar_edad(dato_g10.iloc[i]['id'])

print(f"\n{dato_g10}")

#filtrado de datos
sin_nulos = dato_g10.dropna()

#recorro el dataset y voy actualziando registro a registro
for i in range(len(sin_nulos)):
    #leer
    id = int(sin_nulos.iloc[i]['id'])
    edad = sin_nulos.iloc[i]['edad']

    #print(f"Id es de tipo: {type(id)} edad es de tipo: {type(edad)}")

    #creo una tupla con la edad y el id
    estudiante = (edad,id)
    #invoco funcion para actualziar edad en la bd
    update_estudiante(conexion, estudiante)


estudiantes_edad = pn.read_sql("SELECT * FROM estudiantes WHERE edad is not null",conexion)
    
print(f"\n{estudiantes_edad}")
