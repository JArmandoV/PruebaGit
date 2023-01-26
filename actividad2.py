##############################################################
#Ruta del archivo
##############################################################

file = 'C:/Users/Arman/OneDrive/Escritorio/Datos/prueba.csv'


##############################################################
#Leer archivos CSV (comma separated values) con pandas
##############################################################

import pandas as pd

df = pd.read_csv(file)

import matplotlib.pyplot as plt       #pandas se apoya en matplotlib para las gráficas

##############################################################
# Correlación
##############################################################

pd.set_option("display.max_rows",None, "display.max_columns",None)
print(df.corr(numeric_only=True))      # es un dataframe


##############################################################
# Mapa de calor
##############################################################

import seaborn as sns

# vmin int, valor mínimo de la escala
# vmax int, valor mínimo de la escala
# annot boolean, muestra el valor de la correlación, default = False
# cmap mapa de color, colores usados para el mapa, https://matplotlib.org/stable/gallery/color/colormap_reference.html

plt.figure(figsize=(15, 5))
sns.heatmap(df.corr(numeric_only=True), vmin=-1, vmax=1, annot=True,cmap="RdYlGn");
plt.show()


# Triángulo
import numpy as np
plt.figure(figsize=(15, 5))
mask = np.tril(np.ones_like(df.corr(numeric_only=True), dtype=bool))     # tril para triángulo superior
sns.heatmap(df.corr(numeric_only=True), mask=mask, vmin=-1, vmax=1, annot=True, cmap='Greens')
plt.show()


#Observar una sola variable
plt.figure(figsize=(15, 5))
column = df.corr(numeric_only=True)[['Población, total']].sort_values(by='Población, total', ascending=False)
sns.heatmap(column, vmin=-1, vmax=1, annot=True, cmap='GnBu')
# 
plt.show()