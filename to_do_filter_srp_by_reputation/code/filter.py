import sys, os
import pandas as pd
import numpy as np

#get output filename based on input filenames

#read file in input dir
filePath_700d = '../output/700D_with_rank.csv'
dir = os.path.dirname(__file__)
input_700d = os.path.relpath(filePath_700d, dir)

filePath_lst = '../input/lst_700D_Yi_Feb222016_giftindex_price_corrected_juexiao_0306.csv'
dir = os.path.dirname(__file__)
input_lst = os.path.relpath(filePath_lst, dir)

#read the excel file
df_700d = pd.read_csv(input_700d)
df_lst = pd.read_csv(input_lst)


df1 = df_lst[['ItemID(LIsting_id)']]
df2 = df_700d[['item_id', 'rank']]

df1 = df1.drop_duplicates(subset = ['ItemID(LIsting_id)'])
print(df1)
#renaming the columns
df1.rename(columns={'ItemID(LIsting_id)':'item_id'}, inplace=True)

s1 = pd.merge(df1, df2, how = 'left', on=['item_id'])

#output the file
#output_file = 'share_' + camera + '_' + datetime.date.today().strftime('%Y%m%d') + '.csv'
filePath_new = '../output/matched_rep.csv'
s1.to_csv(filePath_new)
#s1.to_csv(filePath_new, encoding = 'utf-8')
