import numpy as np 
from sklearn import datasets, linear_model 
import matplotlib.pyblot as plt 

boston = datasets.load_boston()
print(boston)
print()

print('Infromación en el dataset: ')
print(boston.keys())
print() 

