##############################################################
#Ruta del archivo
##############################################################

file = 'C:/Users/Arman/OneDrive/Escritorio/Datos/prueba.csv'


##############################################################
#Leer archivos CSV (comma separated values) con pandas
##############################################################

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(file)


##############################################################
#  k means
##############################################################

from sklearn.cluster import KMeans #instalar scikit-learn

test = df[["Población urbana","Gasto nacional bruto (% del PIB)"]]
test = test.dropna(axis = 0, how = 'any')

kmeans = KMeans(n_clusters=6,n_init='auto').fit(test)
centroids = kmeans.cluster_centers_
# print(centroids)
# 
# # Predicciones (cuál es la clase) de acuerdo a los centros calculados
# 
cla = kmeans.predict(test)                   # obtiene las clases de los datos iniciales
# print(cla)
# 
# # Predicción para un nuevo dato
# data = {'danceability': ['.27'], 'energy': [.5]}
# newdf = pd.DataFrame(data)  
# print(kmeans.predict(newdf))
# 
# 
plt.scatter(df["Población urbana"],df["Gasto nacional bruto (% del PIB)"],c=cla)
for i in range(len(centroids)):
    plt.scatter(centroids[i][0],centroids[i][1],marker="*",c="red")
plt.show()