import pandas as pd
#Loading the table
class loader:
    @staticmethod
    def loader_file(path):
        return pd.read_csv(path)
