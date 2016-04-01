# Author: Jiahao Huang
# Data: Feb-22-2016
# This program is for count the difference of dict_index between bundle_1 and bundle_n for n > 1 and get the diff of price
# Out put will be several diff_1_n.csv file for some n > 1

import csv
import os
file_path = "output/diff_1_2.csv"
price_source = "input/price_source.csv"

price12 = []
with open(file_path) as csvfile:
	csv_opened = csv.DictReader(csvfile)
	for row in csv_opened:
		with open(price_source) as price_csv:
			csv_opened2 = csv.DictReader(price_csv)
			temp_price = []
			for row2 in csv_opened2:
				if row["ItemID(LIsting_id)"] == row2["ItemID(LIsting_id)"] and row2["bundle_index"] in row["two_bundle_index"] and row2["bundle_price"] not in temp_price:
					temp_price += [row2["bundle_price"]]
		price12 += [temp_price]
print(len(price12))


file_path = "output/diff_1_3.csv"
price13 = []
with open(file_path) as csvfile:
	csv_opened = csv.DictReader(csvfile)
	for row in csv_opened:
		with open(price_source) as price_csv:
			csv_opened2 = csv.DictReader(price_csv)
			temp_price = []
			for row2 in csv_opened2:
				if row["ItemID(LIsting_id)"] == row2["ItemID(LIsting_id)"] and row2["bundle_index"] in row["two_bundle_index"] and row2["bundle_price"] not in temp_price:
					temp_price += [row2["bundle_price"]]
		price13 += [temp_price]
print(len(price13))

file_path = "output/diff_1_4.csv"
price14 = []
with open(file_path) as csvfile:
	csv_opened = csv.DictReader(csvfile)
	for row in csv_opened:
		with open(price_source) as price_csv:
			csv_opened2 = csv.DictReader(price_csv)
			temp_price = []
			for row2 in csv_opened2:
				if row["ItemID(LIsting_id)"] == row2["ItemID(LIsting_id)"] and row2["bundle_index"] in row["two_bundle_index"] and row2["bundle_price"] not in temp_price:
					temp_price += [row2["bundle_price"]]
		price14 += [temp_price]
print(len(price14))

file_path = "output/diff_1_5.csv"
price15 = []
with open(file_path) as csvfile:
	csv_opened = csv.DictReader(csvfile)
	for row in csv_opened:
		with open(price_source) as price_csv:
			csv_opened2 = csv.DictReader(price_csv)
			temp_price = []
			for row2 in csv_opened2:
				if row["ItemID(LIsting_id)"] == row2["ItemID(LIsting_id)"] and row2["bundle_index"] in row["two_bundle_index"] and row2["bundle_price"] not in temp_price:
					temp_price += [row2["bundle_price"]]
		price15 += [temp_price]
print(len(price15))


file_path = "output/diff_1_6.csv"
price16 = []
with open(file_path) as csvfile:
	csv_opened = csv.DictReader(csvfile)
	for row in csv_opened:
		with open(price_source) as price_csv:
			csv_opened2 = csv.DictReader(price_csv)
			temp_price = []
			for row2 in csv_opened2:
				if row["ItemID(LIsting_id)"] == row2["ItemID(LIsting_id)"] and row2["bundle_index"] in row["two_bundle_index"] and row2["bundle_price"] not in temp_price:
					temp_price += [row2["bundle_price"]]
		price16 += [temp_price]
print(len(price16))

file_path = "output/diff_1_7.csv"
price17 = []
with open(file_path) as csvfile:
	csv_opened = csv.DictReader(csvfile)
	for row in csv_opened:
		with open(price_source) as price_csv:
			csv_opened2 = csv.DictReader(price_csv)
			temp_price = []
			for row2 in csv_opened2:
				if row["ItemID(LIsting_id)"] == row2["ItemID(LIsting_id)"] and row2["bundle_index"] in row["two_bundle_index"] and row2["bundle_price"] not in temp_price:
					temp_price += [row2["bundle_price"]]
		price17 += [temp_price]
print(len(price17))


file_path = "output/diff_1_8.csv"
price18 = []
with open(file_path) as csvfile:
	csv_opened = csv.DictReader(csvfile)
	for row in csv_opened:
		with open(price_source) as price_csv:
			csv_opened2 = csv.DictReader(price_csv)
			temp_price = []
			for row2 in csv_opened2:
				if row["ItemID(LIsting_id)"] == row2["ItemID(LIsting_id)"] and row2["bundle_index"] in row["two_bundle_index"] and row2["bundle_price"] not in temp_price:
					temp_price += [row2["bundle_price"]]
		price18 += [temp_price]
print(len(price18))





