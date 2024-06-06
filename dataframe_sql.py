'''Importar sqlite3 y pandas'''
import sqlite3
import pandas as pd
import random

#conectarse a la bd
conn = sqlite3.connect('g10.db')

#usar pandas y la funcion adecuada para procesar la sentencia sql:
# SELECT * FROM estudiantes
#y descargar los datos en un DataFrame de Pandas

dataFrame_est = pd.read_sql('SELECT * FROM estudiantes',conn)

#imprimir el DataFrame
#print(dataFrame_est)

'''
for i in range(len(dataFrame_est)):
    #dataFrame_est.at[i, 'edad'] = random.randrange(18,41)
    dataFrame_est.loc[i, 'edad'] = random.randrange(18,41)

print(dataFrame_est)
'''

dataFrame_est['edad'] = dataFrame_est['edad'].apply(lambda x: random.randrange(18,41))

print(dataFrame_est)

#Calcular promedio de edad x Genero

#Contar edades x genero
