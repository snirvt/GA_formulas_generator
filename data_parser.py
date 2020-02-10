
import pandas as pd

class Data_Parser():

    def __init__(self):
        pass

    @staticmethod
    def get_data_frame(path):
        return pd.read_excel(path)

    @staticmethod
    def get_matrix_data(path):
        df = Data_Parser.get_data_frame(path)
        column_names = list(df)[1:] # not taking the first name
        mat = df.values
        X = mat[:, 1:]
        y = mat[:, 0] 
        return X, y , column_names









