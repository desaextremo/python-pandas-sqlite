#importar pandas
import pandas as pd

#importar sqlite3 para conectarse a la base de datos
import sqlite3

#generar 

#conectarse a la base de datos
conn = sqlite3.connect('g10.db')

#me conecto a la base de datos, le envio el query y la conexion a la base de datos
dataframe = pd.read_sql("SELECT * FROM estudiantes",conn,index_col='id')

print("Datos de la tabla 'estudiantes':")
print(dataframe)

#promedio_edad_por_genero = df.dataframe('genero')['edad'].mean()
#print("\nPromedio de edad por género:")
#print(promedio_edad_por_genero)

#Contar la cantidad de hombres y mujeres:
conteo_genero = dataframe['genero'].value_counts()
print("\nConteo de estudiantes por género:")
print(conteo_genero)


