"""
@author Jiazhen Chen

Please Ignore the "UserWarning" warning. The program is fine.

To-do: 
add the price and fake_brand_id into the second filename input
according to the dic_index

enter in console the following line:
ipython price_fake_id.py [inputfile name1] [inputfile name2]
e.g: ipython price_fake_id.py dict_700d_750d.csv dictIdx_table.csv

input:
1. The file as the first argument specified
(inputfile1.xlsx, inputfile2.xlsx)

output:
1. inputfile2_pr_fk_date.xlsx

"""

import sys, os, datetime
import pandas as pd
import numpy as np
import ast
import warnings
warnings.simplefilter(action = "ignore", category = UserWarning)

#get output filename based on input filenames
input_file_1 = "dict_700d_750d_Feb082016_zemin0309.csv"  #dict_700d_750d
input_file_2 = "dictIdx_table.csv" #dictIdx_table


#read file in input dir
filePath_1 = '../input/' + input_file_1
dir = os.path.dirname(__file__)
read_input_1 = os.path.relpath(filePath_1, dir)

filePath_2 = '../output/' + input_file_2
dir = os.path.dirname(__file__)
read_input_2 = os.path.relpath(filePath_2, dir)

#read the excel file
df_input_1_toexcel = pd.read_csv(read_input_1, sep=',', encoding='GB18030')
#print(list(df_input_1_toexcel.columns.values))

df_input_2_toexcel = pd.read_csv(read_input_2)


name_1 = ''
k = 0
while (input_file_1[k] != '.'):
	name_1 += input_file_1[k]
	k += 1

name_2 = ''
i = 0
while (input_file_2[i] != '.'):
	name_2 += input_file_2 [i]
	i += 1


filePath_input_1 =  '../output/' + name_1 + '.xlsx'
df_input_1_toexcel.to_excel(filePath_input_1)
filePath_input_2 = '../output/' + name_2 + '.xlsx'
df_input_2_toexcel.to_excel(filePath_input_2)


df_input_1 = pd.read_excel(filePath_input_1)
df_input_2 = pd.read_excel(filePath_input_2)
#print(list(df_input_1_toexcel.columns.values))
df_input_1.rename(columns={'index_final':'dic_index', 'Avg. Price Esitimate':'price', 'suspect for fake brand':'fake_brand_id'}, inplace=True)
df1 = df_input_1[['dic_index', 'price', 'fake_brand_id']]

#renaming the columns
#df1.rename(columns={'index_final':'dic_index', 'Avg. Price Esitimate ':'price', 'suspect for fake brand':'fake_brand_id'}, inplace=True)

s1 = pd.merge(df_input_2, df1, how = 'left', on=['dic_index'])

i = 0;
out_name = ''
while (input_file_2[i] != '.'):
	out_name += input_file_2[i]
	i += 1

#output the file
output_file = out_name + '_pr_fk' + '.csv'
filePath_new = '../input/' + output_file
#s1.to_csv(filePath_new)
s1.to_csv(filePath_new)

