
import pandas as pd

class Data_Parser():

    def __init__(self):
        pass

    @staticmethod
    def get_data_frame(path):
        return pd.read_excel(path)

    @staticmethod
    def get_matrix_data(path, X_columns = 1, y_column = 0):
        df = Data_Parser.get_data_frame(path)
        df = df.dropna()
        column_names = list(df)[X_columns:] # not taking the first name
        mat = df.values
        X = mat[:, X_columns:]
        y = mat[:, y_column] 
        return X, y , column_names









