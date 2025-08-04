
import pandas as pd
pd.options.mode.copy_on_write = True
class clean:
    @staticmethod
    def clean_columns(df):

        df=df[["Text","Biased"]]
        df["Text"]=df["Text"].str.lower()
        df["Text"]=df["Text"].str.replace(","," ")
        # print(df)

        return df

