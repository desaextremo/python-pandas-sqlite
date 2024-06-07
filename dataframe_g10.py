from funciones_captura import limpiar_pantalla
import pandas as pn
import sqlite3 
import random

limpiar_pantalla()
conexion = sqlite3.connect("g10.db")
dato_g10 = pn.read_sql("Select * from estudiantes",conexion)


print("_____________________________________________________")
print("     1  recorrer el dataframe for y iloc             ")
print("_____________________________________________________")
#1  recorrer el dataframe for y iloc
for i in range(len(dato_g10)):
    print(f"id {dato_g10.iloc[i]['id']} Nombres: {dato_g10.iloc[i]['nombres']} Apellidos: {dato_g10.iloc[i]['apellidos']}")

    #Esta forma de actualziacion no sirve y presenta problemas
    # dato_g10.iloc[i]['edad'] = random.randint(18,41)

    #dato_g10.loc[i, 'edad'] = random.randint(18,41)

    #dato_g10.iloc[i, dato_g10.columns.get_loc('edad')] = random.randint(18,41)
    #dato_g10.at[i, 'edad'] = random.randint(18,41)

    #if dato_g10.iloc[i]['id'] % 2 == 0

#2 terar sobre los elementos de iterrows
print("_____________________________________________________")
print("     2 terar sobre los elementos de iterrows         ")
print("_____________________________________________________")
for i, row in dato_g10.iterrows():
    print(f"{i} -  id {row['id']} Nombres: {row['nombres']} Apellidos: {row['apellidos']}")

#3 iterar sobre los elementos de iterrows
print("_____________________________________________________")
print("     3 iterar sobre los elementos de iterrows        ")
print("_____________________________________________________")
index = 0
for row in dato_g10.itertuples():
    print(f"id {row.id} Nombres: {row.nombres} Apellidos: {row.apellidos}")

print(f"\n{dato_g10}") 