import csv
import os
import ast

dict_file = "../input/dict_700d_750d_Feb082016.csv" 
source_file = "../input/diff_1_"
only_other = []
for i in range(2, 9):
	source_file = source_file + str(i) + ".csv"
	with open(source_file) as csvfile:
		csv_opened = csv.DictReader(csvfile)
		for row in csv_opened:
			x = ast.literal_eval(row["only_in_other"])
			only_other += x
	source_file = "../input/diff_1_"

dic = []
with open(dict_file) as csvfile:
	csv_opened = csv.DictReader(csvfile)
	for row in csv_opened:
		dic += [row["index_final"]]

def important(x):
	if x in only_other:
		return 1
	else:
		return 0


# csv file filed names here
fn = ['Author', 'index_final', 'important']

# Author name
an = "Jiahao"

with open('../output/700d_dict_with_important.csv', 'w') as csvfile:
	writer = csv.DictWriter(csvfile, fieldnames = fn)
	writer.writeheader()
	for i in dic:
		writer.writerow({'Author': an, 'index_final': i, 'important': important(i)})













