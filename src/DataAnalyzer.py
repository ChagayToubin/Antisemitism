class dataAnalyzer:
    @staticmethod
    def count_1_0(df):
        mesk=(df['Biased']==1)
        count=(len(df[mesk]))

        return {"1":int(count),"0":int(len(df)-count)}

    @staticmethod
    def count_0_1_len_sentence(df):
        mesk_1=df['Biased']==1
        df_1=df[mesk_1]
        count1=0

        for i in df_1['Text']:
            count1+=len(i.split())

        mesk_0 = df['Biased'] == 0
        df_0 = df[mesk_0]
        count0 = 0

        for i in df_0['Text']:
            count0 += len(i.split())

        return {"1":count1/len(df_1),"0":count0/len(df_0)}