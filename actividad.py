file = 'C:/Users/Arman/OneDrive/Escritorio/Datos/test.csv'
#Copie y pegue la ruta de su carpita con el divisor / y escriba correctamente el nombre del archivo
import pandas as pd
df = pd.read_csv(file)

columna = df["Crecimiento de la población (% anual)"]
columna2 = df["Población urbana (% del total)"]


#print(df.head()) #head and tail tienen por default n = 5
#print(df.tail())
print("Numero de variables y numero de registros")
print(df.shape) #tupla con numero de renglones y numero de columnas
#pd.set_option("display.max_rows",None, "display.max_columns",None)
print("Lista de las columnas")
print(df.columns) #Lista con nombres de las columnas
print("Tipos de datos")
print(df.dtypes) #tipos de datos de cada columna

print("Valores unicos: ")
print(df["Crecimiento de la población (% anual)"].unique())

#quita los renglones (axis=0) que contiene cualquier (how='any','all') columna vacia, inplace significa
#df.dropna(axis = 0, how = 'any', inplace = True)




print("Valores Maximos del crecimiento de poblacion anual ")
print(columna.max()) #valor maximo
print("Valores Minimos del crecimiento de poblacion anual")
print(columna.min()) #valor minimo
print("Desviacion Estandar del crecimiento de poblacion anual")
print(columna.std()) #desviacion estandar, que tan dispersos estan los datos al rededor de la media
print("Media del crecimiento de poblacion anual: ")
print(columna.mean()) #promedio
print("Mediana: del crecimiento de poblacion anual ")
print(columna.median()) #mediana (el valor que se encuentra al centro de la lista ordenada

print("Valores Maximos de la poblacion urbana ")
print(columna2.max()) #valor maximo
print("Valores Minimos de la poblacion urbana: ")
print(columna2.min()) #valor minimo
print("Desviacion Estandar de la poblacion urbana: ")
print(columna2.std()) #desviacion estandar, que tan dispersos estan los datos al rededor de la media
print("Media de la poblacion urbana: ")
print(columna2.mean()) #promedio
print("Mediana de la poblacion urbana: ")
print(columna2.median()) #mediana (el valor que se encuentra al centro de la lista ordenada




#estadisticas basicos en formato de tabla

#print(df.describe())

import matplotlib.pyplot as plt

df.hist(column="Crecimiento de la población (% anual)", color="darkturquoise")
plt.show()
df.hist(column="Población urbana (% del total)", color="darkturquoise")
plt.show()