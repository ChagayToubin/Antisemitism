import pandas as pd
class loader:
    @staticmethod
    def loader_file(path):
        return pd.read_csv(path)
