

import pandas as pd
import numpy as np

from ga import GA
from data_parser import Data_Parser


X = np.random.rand(2000,5)
y = X[:,0]**2 + X[:,1]**2
column_names = [0,1,2,3,4]

# path = 'data.xlsx'

# X, y, column_names = Data_Parser.get_matrix_data(path)
if __name__ == '__main__':    
    ga = GA(X=X[:1000,:], X_test=X[1000:,:], y=y[:1000], y_test= y[1000:], column_names = column_names, parlal=False)
    ga.natural_selection()
    # ga.natural_selection_paralal()