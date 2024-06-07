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

def nota_aleatoria():
    return round(random.uniform(1.0,5.0),2)



print("_____________________________________________________")
print("     1  recorrer el dataframe for y iloc             ")
print("_____________________________________________________")
#1  recorrer el dataframe for y iloc
'''
for i in range(len(dato_g10)):
    dato_g10.loc[i, 'edad'] = actualizar_edad(dato_g10.iloc[i]['id'])
'''
#Agregar 3 columnas
dato_g10['nota1'] = 0
dato_g10['nota2'] = 0
dato_g10['nota3'] = 0

'''
for i in range(len(dato_g10)):
    dato_g10.loc[i, 'nota1'] = round(random.uniform(1.0,5.0),2)
    dato_g10.loc[i, 'nota2'] = round(random.uniform(1.0,5.0),2)
    dato_g10.loc[i, 'nota3'] = round(random.uniform(1.0,5.0),2)
'''


#dato_g10.apply(funcion anonima variable: instrucccion o funcion, axis=1)

#actualizar edades
dato_g10['edad'] = dato_g10.apply(lambda filita: actualizar_edad(filita['id']),axis=1)

dato_g10['nota1'] = dato_g10.apply(lambda fila: nota_aleatoria(), axis=1)
dato_g10['nota2'] = dato_g10.apply(lambda fila: nota_aleatoria(), axis=1)
dato_g10['nota3'] = dato_g10.apply(lambda fila: nota_aleatoria(), axis=1)
#filtrado de datos (nota1*30 + nota2 *30 + nota3 * 40) / 3
dato_g10['definitiva'] = round(((dato_g10['nota1'] *.30) + (dato_g10['nota2'] * .30) + (dato_g10['nota3'] * .40) / 3),2)

pasaron = dato_g10[dato_g10['definitiva'] > 3]

reprobaron = dato_g10[dato_g10['definitiva'] < 3]


print(f"\n\n{dato_g10}")

print(f"\n\n{pasaron}")

print(f"\n\n{reprobaron}")

