import pandas as pd
class clean:
    @staticmethod
    def clean_columns(df):

        df=df[["Text","Biased"]]
        df=df["Text"].str.lower()
        print(df)

