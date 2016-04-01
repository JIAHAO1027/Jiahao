import csv
import os
import pandas as pd

lst_path = "input/lst_700D_Yi_Feb142016_giftindex_corrected - Sheet1.csv"
dic_path = "input/dict_700d_750d_youyi.csv"
with open(lst_path) as csvfile:
	csv_opened = csv.DictReader(csvfile)
	for row in csv_opened:
		print(1)
		
