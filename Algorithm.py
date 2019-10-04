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

from sklearn.model_selection import train_test_split 

X_train, X_test, Y_test = train_test_split(X, Y, test_size=0.2)

lr = linear_nodel.LinearRegression()

lr.fit(X_train, Y_train)

Y_pred = lr.predict(X_test)

plt.scatter(X_test, Y_test)
plt.plot(X_test, Y_pred, color="red", linewidth=3)
plt.title("Regresion Lineal Simple")
plt.xlabel("Numero de habitaciones")
plt.ylabel("Valor medio")
plt.show()

print()
print('Datos del modelo de regresion')
print()
print('Valor de la pendiente')
print(lr.intercept_)
print() 
print('La ecuacion del modelo es igual a: ')
print('y =', lr.coef_, 'x ', lr.intercept_)

print()
print('Precision del modelo: ')
print(lr.score(X_train, Y_train))


