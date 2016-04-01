import csv
import os
file_path = "output/diff_1_2.csv"
price_source = "input/dict_700d_750d_youyi.csv"


price = []
with open(file_path) as csvfile:
	csv_opened = csv.DictReader(csvfile)
	for row in csv_opened:
		with open(price_source) as csvfile:
			csv_opened2 = csv.DictReader(csvfile)
			temp_price = []
			for j in csv_opened2:
				if j["dict_yi_index"] in row["only_in_other"]:
					temp_price += [j['price_lower_bound']]
		price += [temp_price]
print(price)
print(len(price))

with open(file_path) as csvfile:
	csv_opened = csv.DictReader(csvfile)
	for row in csv_opened:
		with open(price_source) as csvfile:
			csv_opened2 = csv.DictReader(csvfile)
			temp_price = []
			for j in csv_opened2:
				if j["dict_yi_index"] in row["only_in_one"]:
					temp_price += [j['price_lower_bound']]
		price += [temp_price]
print(price)
print(len(price))
