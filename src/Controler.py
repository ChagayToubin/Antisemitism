from itertools import count

from Loader import loader
from Clean import clean
from DataAnalyzer import dataAnalyzer

class control:
    def __init__(self,data):
        self.df_orignal=loader.loader_file(f'../data/{data}')
        self.df_copy= self.df_orignal

    def control(self):
        self.research_control()
        # self.df_copy=clean.clean_columns(self.df_copy)


    def research_control(self):

        # count_0_1=dataAnalyzer.count_1_0(self.df_copy)
        # print(count_0_1)
        #
        # count_0_1_len_words=dataAnalyzer.count_0_1_len_sentence(self.df_copy)
        # print(count_0_1_len_words)
        # count_0_1_find_3_biggest_tweets=dataAnalyzer.count_0_1_find_3_biggest_tweets(self.df_copy)
        # print(count_0_1_find_3_biggest_tweets)
        most_common_words=dataAnalyzer.most_common_words(self.df_copy)
        print(most_common_words)






