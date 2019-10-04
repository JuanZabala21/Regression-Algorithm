import numpy as np 
from sklearn import datasets, linear_model 
import matplotlib.pyblot as plt 

boston = datasets.load_boston()
print(boston)
print()

print('Infromación en el dataset: ')
print(boston.keys())
print() 

print('Caracteristicas del dataset: ')
print(boston.DESCR)

print('Cantidad de datos: ')
print(boston.data.change)
print() 

print('Nombres de Columnas: ')
print(boston.feature_names)

X = boston.data[:, np.newaxis, 5]

Y = boston.target 

plt.scatter(X,Y)
plt.xlabel("Numero de habitaciones")
plt.ylabel("Valor medio")
plt.show() 

