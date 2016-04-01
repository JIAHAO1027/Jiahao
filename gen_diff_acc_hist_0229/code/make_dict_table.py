import csv
import os
import ast

# input: /input/dict_700d_750d_Feb082016.csv
#		 /input/with1_diffDictIdx_output.csv
#		 /input/with1_diffDictIdx_output.csv

# output: /output/dictIdx_table.csv
#         /output/forgraph.csv
#		  /output/for_individual_graph.csv


file_path = "../input/dict_700d_750d_Feb082016_zemin0309.csv"

def get_top2(x):
	return x[:2]

with open(file_path) as csvfile:
	csv_opened = csv.DictReader(csvfile)
	indexID_all = []
	for row in csv_opened:
		t = get_top2(row["index_final"])
		if t not in indexID_all:
			indexID_all += [t]


file_path = "../output/with1_diffDictIdx_output.csv"
with open(file_path) as csvfile:
	csv_opened = csv.DictReader(csvfile)
	findall = []
	for row in csv_opened:
		findall += ast.literal_eval(row["in_both"])



file_path = "../output/with1_diffDictIdx_output.csv"
with open(file_path) as csvfile:
	csv_opened = csv.DictReader(csvfile)
	findall_withindex = []
	for row in csv_opened:
		for d in ast.literal_eval(row["in_both"]):
			findall_withindex += [(int(row["another_bundle_index"]) ,d ,row["ItemID(LIsting_id)"])]



pair = []
for index in indexID_all:
	count = 0
	for i in findall:
		if index == i:
			count += 1
	pair += [(index, count)]




fn = ["ItemID", "index", "dic_index"]

with open('../output/dictIdx_table.csv', 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames = fn)
		writer.writeheader()
		for i in findall_withindex:
			writer.writerow({'ItemID': i[2] ,'index': i[0], 'dic_index': i[1]})


fn = ["index"]

with open('../output/forgraph.csv', 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames = fn)
		writer.writeheader()
		for i in findall:
			writer.writerow({'index': i})

fn = ["bundle_index", "dic_index"]
with open('../output/for_individual_graph.csv', 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames = fn)
		writer.writeheader()
		for i in findall_withindex:
			writer.writerow({'bundle_index': i[0], 'dic_index': i[1]})














