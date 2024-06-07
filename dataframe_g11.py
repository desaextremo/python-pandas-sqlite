'''
1  Utilizar sqlite para conectarnos  la base de datos y ejecutar la consulta:
2  Utilizar pandas para ejecutar la consulta: SELECT * FROM estudiantes, y
   obtener un dataframe con sus datos
3  Imprimir los datos del dataframe
4  Recorrer el dataframe, generar valor aleatorio para la edad con valores entre 18 y 40 años
   y actualizar la columna Edad en el dataframe
'''
import numpy as np
import sqlite3
import pandas as pd
from funciones_captura import limpiar_pantalla
from bd import *

limpiar_pantalla()

conexion = sqlite3.connect('g11.db')
dataframe_g11 = pd.read_sql('SELECT * FROM estudiantes',conexion)

#print(dataframe_g11)

#1  recorrer el dataframe for y iloc

for i in range(len(dataframe_g11)):
    #print(dataframe_g11.iloc[i])  #acceder a la fila completa
    #print("__________________________________________")
    #print(f"{dataframe_g11.iloc[i]['id']} {dataframe_g11.iloc[i]['nombres']} {dataframe_g11.iloc[i]['apellidos']} {dataframe_g11.iloc[i]['edad']}")
    
    #dataframe_g11.iloc[i]['edad'] = np.random.randint(1,41)

    if i%2 == 0:
        dataframe_g11.loc[i, 'edad'] = np.random.randint(18,41)

    #dataframe_g11.iloc[i, dataframe_g11.columns.get_loc('edad')] = np.random.randint(18,41)
    #dataframe_g11.at[i, 'edad'] = np.random.randint(18,41)

print("__________________________________________________")
print(f"Longitud: {len(dataframe_g11)}")
print(dataframe_g11)

#eliminar los valores nulos
df_sinnulos = dataframe_g11.dropna()
print("__________________________________________________")
print(f"Longitud: {len(df_sinnulos)}")
print(df_sinnulos)

'''
promedio_edad_por_genero = df_sinnulos.groupby('genero')['edad'].mean()
print("\nPromedio de edad por género:")
print(promedio_edad_por_genero)

conteo_genero = df_sinnulos['genero'].value_counts()
print("\nConteo de estudiantes por género:")
print(conteo_genero)

#2 terar sobre los elementos de iterrows
for index, row in dataframe_g11.iterrows():
    print(f"{index} -  {row['nombres']}")
    if index%2 == 0:
        dataframe_g11.loc[index, 'edad'] = np.random.randint(18,41)

print(dataframe_g11)


#3 terar sobre los elementos de iterrows

index = 0
for row in dataframe_g11.itertuples():
    print(row.nombres)
    if index%2 == 0:
        dataframe_g11.loc[index, 'edad'] = np.random.randint(18,41)
    index +=1


update_estudiante(conexion,(18,1))
update_estudiante(conexion,(30,2))
update_estudiante(conexion,(35,3))
update_estudiante(conexion,(40,4))
update_estudiante(conexion,(50,5))
'''

#actualizar información de la edad en la base de datos
for i in range(len(df_sinnulos)):
    #fue necesario realziar una conversion previa porque el tipo de datos no era realmente entero
    codigo = int(df_sinnulos.iloc[i]['id'])
    edad = int(df_sinnulos.iloc[i]['edad'])
    #print(f"id {codigo} id tipo {type(codigo)} edad {edad} edad tipo {type(edad)}")

    update_estudiante(conexion,(edad,codigo,))

#trae información sobre registros sin id vacio o nulo
#dataframe_1 = pd.read_sql('SELECT * FROM estudiantes WHERE edad is null',conexion)

# Definir una función que incremente el valor si el índice es par
'''
def incrementar_si_par(value, index):
    if index % 2 == 0:  # Verificar si el índice es par
        return np.random.randint(18,41)
    else:
        return 0

limpiar_pantalla()

dataframe_g11['edad'] = dataframe_g11.apply(lambda row: incrementar_si_par(row['id'], row.name), axis=1)
print(dataframe_g11)
'''

estudiantes_con_edad = pd.read_sql('SELECT * FROM estudiantes WHERE edad is not null',conexion)

print(f"\n\n{estudiantes_con_edad}")