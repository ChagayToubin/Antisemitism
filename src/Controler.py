from itertools import count
import json

from Loader import loader
from Clean import clean
from DataAnalyzer import dataAnalyzer

class control:
    def __init__(self,data):
        self.df_orignal=loader.loader_file(f'../data/{data}')


    def control(self):
        data=self.research_control()
        clean_df = self.clean_df()

        self.load_files(data,clean_df)

    def research_control(self):
        count_0_1=dataAnalyzer.count_1_0(self.df_orignal)

        count_0_1_len_words=dataAnalyzer.count_0_1_len_sentence(self.df_orignal)

        count_0_1_find_3_biggest_tweets=dataAnalyzer.count_0_1_find_3_biggest_tweets(self.df_orignal)

        most_common_words=dataAnalyzer.most_common_words(self.df_orignal)

        count_big_letter=dataAnalyzer.count_big_letter(self.df_orignal)

        dic={"total_tweets":
            {
                "antisemitic":count_0_1["1"],"non_antisemitic":count_0_1["0"],"total":count_0_1["0"]+count_0_1["1"]+count_0_1["unspecified"],"unspecified":count_0_1["unspecified"]},
                "average_length":{"antisemitic":count_0_1_len_words["1"],"non_antisemtic":count_0_1_len_words["0"],"total":count_0_1_len_words["total"]},
                "common_words":{"total":most_common_words},
                "longest_3_tweets":{"antisemtic":count_0_1_find_3_biggest_tweets["1"],"non_antisemtic":count_0_1_find_3_biggest_tweets["0"]},
                "uppercase_words":{"antisemitic":count_big_letter["1"],"non_antisemitc":count_big_letter["0"]}
        }

        return dic

    @staticmethod
    def load_files(dic,clean_df):
        j=json.dumps(dic)
        with open("../results/result.json",'w', encoding='utf-8') as f:
             json.dump(dic, f, ensure_ascii=False, indent=4)

        clean_df.to_csv("../results/tweets_dataset_cleaned.csv", sep='\t', encoding='utf-8')
    def clean_df(self):
        return clean.clean_columns(self.df_orignal)










