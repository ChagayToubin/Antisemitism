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

    @staticmethod
    def count_0_1_find_3_biggest_tweets(df):
        mesk_1=df['Biased'] == 1
        most_big_tweet1=["","",""]

        for i in df[mesk_1]['Text']:
            # print(len(i),len(most_big_tweet[0]))

            if len(i) > len(most_big_tweet1[0]):
                most_big_tweet1[0]=i
                most_big_tweet1=sorted(most_big_tweet1,key=len)

        # for i in most_big_tweet1:
        #     print(len(i))

        mesk_0 = df['Biased'] == 0
        most_big_tweet0 = ["", "", ""]

        for i in df[mesk_0]['Text']:

            if len(i) > len(most_big_tweet0[0]):
                most_big_tweet0[0] = i
                most_big_tweet0 = sorted(most_big_tweet0, key=len)
        # print()
        # for i in most_big_tweet0:
        #     print(len(i))
        return {"1":most_big_tweet1,"0":most_big_tweet0}

    @staticmethod
    def most_common_words(df):

        return ""






