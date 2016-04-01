import csv
import os
import pandas as pd

code_path = os.getcwd()
parent_path = os.sep.join(code_path.split(os.sep)[:-1])

lst_path = "../input/lst_700D_Yi_Feb142016_giftindex_corrected.csv"
dic_path = "../input/dict_700d_750d_youyi.csv"
lst = pd.DataFrame.from_csv(lst_path)
dic = pd.DataFrame.from_csv(dic_path)
result = pd.merge(lst, dic, left_on='dict_yi_index')