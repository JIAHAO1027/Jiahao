# Author: Jiahao Huang
# Data: Feb-18-2016
# This program is for count the difference of dict_index between bundle_1 and bundle_n for n > 1
# Out put will be several diff_1_n.csv file for some n > 1

import csv
import os

# Set working directory
# os.chdir("/Users/Jiahao/Dropbox/urap_programming/Jiahao/relative_premium")
# Target file
# Put your file path here!
file_path = "input/lst_700D_Yi_Feb222016_giftindex_price_corrected_juexiao.csv"
#file_path = "/Users/Jiahao/Desktop/urap_test/input/table.csv"

# This part is for count

# Compare two array and return the difference
def comp_array(one, other):
	count = 0
	only_in_one = []
	only_in_other = []
	for i in other:
		if i not in one:
			count += 1
			only_in_other += [i]

	for i in one:
		if i not in other:
			count += 1
			only_in_one += [i]

	return (count, only_in_one, only_in_other)

# Find the unique item id.
# Open the csv file.

with open(file_path) as csvfile:
	csv_opened = csv.DictReader(csvfile)
	itemID_all = []
	for row in csv_opened:
		if row["ItemID(LIsting_id)"] not in itemID_all:
			itemID_all += [row["ItemID(LIsting_id)"]]
print("Finished count all item id")
print(len(itemID_all))
l = len(itemID_all)

# get each id's dict_yi_index when bundle_index = 1
with open(file_path) as csvfile:
	csv_opened = csv.DictReader(csvfile)
	dict_yi_index_1 = []
	for itemID in itemID_all:
		csvfile.seek(0)
		temp_dict_index = []
		for row in csv_opened:
			if row["ItemID(LIsting_id)"] == itemID and row["bundle_index"] == "1" and row["dict_yi_index"] not in temp_dict_index:
				temp_dict_index += [row["dict_yi_index"]]
		dict_yi_index_1 += [temp_dict_index]
print("Finished count dict_yi_index_1")
print(len(dict_yi_index_1))



# get each id's dict_yi_index when bundle_index = 2
with open(file_path) as csvfile:
	csv_opened = csv.DictReader(csvfile)
	dict_yi_index_2 = []
	for itemID in itemID_all:
		csvfile.seek(0)
		temp_dict_index = []
		for row in csv_opened:
			if row["ItemID(LIsting_id)"] == itemID and row["bundle_index"] == "2" and row["dict_yi_index"] not in temp_dict_index:
				temp_dict_index += [row["dict_yi_index"]]
		dict_yi_index_2 += [temp_dict_index]
# print(len(dict_yi_index_2))
print("Finished count dict_yi_index_2")
print(len(dict_yi_index_2))


# get each id's dict_yi_index when bundle_index = 3
with open(file_path) as csvfile:
	csv_opened = csv.DictReader(csvfile)
	dict_yi_index_3 = []
	for itemID in itemID_all:
		csvfile.seek(0)
		temp_dict_index = []
		for row in csv_opened:
			if row["ItemID(LIsting_id)"] == itemID and row["bundle_index"] == "3" and row["dict_yi_index"] not in temp_dict_index:
				temp_dict_index += [row["dict_yi_index"]]
		dict_yi_index_3 += [temp_dict_index]
#print(len(dict_yi_index_3))
print("Finished count dict_yi_index_3")
print(len(dict_yi_index_3))

# get each id's dict_yi_index when bundle_index = 4
with open(file_path) as csvfile:
	csv_opened = csv.DictReader(csvfile)
	dict_yi_index_4 = []
	for itemID in itemID_all:
		csvfile.seek(0)
		temp_dict_index = []
		for row in csv_opened:
			if row["ItemID(LIsting_id)"] == itemID and row["bundle_index"] == "4" and row["dict_yi_index"] not in temp_dict_index:
				temp_dict_index += [row["dict_yi_index"]]
		dict_yi_index_4 += [temp_dict_index]
print("Finished count dict_yi_index_4")
print(len(dict_yi_index_4))


# get each id's dict_yi_index when bundle_index = 5
with open(file_path) as csvfile:
	csv_opened = csv.DictReader(csvfile)
	dict_yi_index_5 = []
	for itemID in itemID_all:
		csvfile.seek(0)
		temp_dict_index = []
		for row in csv_opened:
			if row["ItemID(LIsting_id)"] == itemID and row["bundle_index"] == "5" and row["dict_yi_index"] not in temp_dict_index:
				temp_dict_index += [row["dict_yi_index"]]
		dict_yi_index_5 += [temp_dict_index]
print("Finished count dict_yi_index_5")
print(len(dict_yi_index_5))



# get each id's dict_yi_index when bundle_index = 6
with open(file_path) as csvfile:
	csv_opened = csv.DictReader(csvfile)
	dict_yi_index_6 = []
	for itemID in itemID_all:
		csvfile.seek(0)
		temp_dict_index = []
		for row in csv_opened:
			if row["ItemID(LIsting_id)"] == itemID and row["bundle_index"] == "6" and row["dict_yi_index"] not in temp_dict_index:
				temp_dict_index += [row["dict_yi_index"]]
		dict_yi_index_6 += [temp_dict_index]
print("Finished count dict_yi_index_6")
print(len(dict_yi_index_6))


# get each id's dict_yi_index when bundle_index = 7
with open(file_path) as csvfile:
	csv_opened = csv.DictReader(csvfile)
	dict_yi_index_7 = []
	for itemID in itemID_all:
		csvfile.seek(0)
		temp_dict_index = []
		for row in csv_opened:
			if row["ItemID(LIsting_id)"] == itemID and row["bundle_index"] == "7" and row["dict_yi_index"] not in temp_dict_index:
				temp_dict_index += [row["dict_yi_index"]]
		dict_yi_index_7 += [temp_dict_index]
print("Finished count dict_yi_index_7")
print(len(dict_yi_index_7))


# get each id's dict_yi_index when bundle_index = 8
with open(file_path) as csvfile:
	csv_opened = csv.DictReader(csvfile)
	dict_yi_index_8 = []
	for itemID in itemID_all:
		csvfile.seek(0)
		temp_dict_index = []
		for row in csv_opened:
			if row["ItemID(LIsting_id)"] == itemID and row["bundle_index"] == "8" and row["dict_yi_index"] not in temp_dict_index:
				temp_dict_index += [row["dict_yi_index"]]
		dict_yi_index_8 += [temp_dict_index]
print("Finished count dict_yi_index_8")
print(len(dict_yi_index_8))


# price


file_path_price = "diff_1_2.csv"
price_source = "input/price_source.csv"

price12 = []
with open(file_path_price) as csvfile:
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
print("got price 1 2")


file_path_price = "diff_1_3.csv"
price13 = []
with open(file_path_price) as csvfile:
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
print("got price 1 3")

file_path_price = "diff_1_4.csv"
price14 = []
with open(file_path_price) as csvfile:
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
print("got price 1 4")

file_path_price = "diff_1_5.csv"
price15 = []
with open(file_path_price) as csvfile:
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
print("got price 1 5")


file_path_price = "diff_1_6.csv"
price16 = []
with open(file_path_price) as csvfile:
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
print("got price 1 6")

file_path_price = "diff_1_7.csv"
price17 = []
with open(file_path_price) as csvfile:
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
print("got price 1 7")


file_path_price = "diff_1_8.csv"
price18 = []
with open(file_path_price) as csvfile:
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
print("got price 1 8")











# This part is for Write file

# csv file filed names here
fn = ['Author', 'ItemID(LIsting_id)', 'two_bundle_index', 'diff', 'only_in_one', 'only_in_other']
fn_test = ['Author', 'ItemID(LIsting_id)', 'two_bundle_index', 'diff', 'only_in_one', 'only_in_other', 'bundle_price' ,'bundle_price_diff']

# Author name
an = "Jiahao"

def diff(x):
	if len(x) == 2:
		return float(x[1]) - float(x[0])
	else:
		return 0

# for each id compare their dict_yi_index with bundle_index = 1 and bundle_index = 2
with open('output/diff_1_2.csv', 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames = fn_test)
		writer.writeheader()
		for idx in range(0, l):
			one = dict_yi_index_1[idx]
			other = dict_yi_index_2[idx]
			if one == []:
				#print(itemID_all[idx], " bundle_index = 1 does not exist ")
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'two_bundle_index': [1, 2], 'diff': "bundle_index = 1 does not exist", 'only_in_one': [], 'only_in_other': [], 'bundle_price' : 0, 'bundle_price_diff' : 0})
			elif other == []:
				#print(itemID_all[idx], " bundle_index = 2 does not exist ")
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'two_bundle_index': [1, 2], 'diff': "bundle_index = 2 does not exist", 'only_in_one': [], 'only_in_other': [], 'bundle_price' : 0, 'bundle_price_diff' : 0})
			else:
				#print(itemID_all[idx], " diff of bundle_index = 1 and bundle_index = 2 ", comp_array(one, other))
				o = comp_array(one, other)
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'two_bundle_index': [1, 2], 'diff': o[0], 'only_in_one': o[1], 'only_in_other': o[2], 'bundle_price' : price12[idx], 'bundle_price_diff' : diff(price12[idx])})
print("Finished csv file diff_1_2!")


# for each id compare their dict_yi_index with bundle_index = 1 and bundle_index = 3
with open('output/diff_1_3.csv', 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames = fn_test)
		writer.writeheader()
		for idx in range(0, l):
			one = dict_yi_index_1[idx]
			other = dict_yi_index_3[idx]
			if one == []:
				#print(itemID_all[idx], " bundle_index = 1 does not exist ")
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'two_bundle_index': [1, 3], 'diff': "bundle_index = 1 does not exist", 'only_in_one': [], 'only_in_other': [], 'bundle_price' : 0, 'bundle_price_diff' : 0})
			elif other == []:
				#print(itemID_all[idx], " bundle_index = 3 does not exist ")
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'two_bundle_index': [1, 3], 'diff': "bundle_index = 3 does not exist", 'only_in_one': [], 'only_in_other': [], 'bundle_price' : 0, 'bundle_price_diff' : 0})
			else:
				#print(itemID_all[idx], " diff of bundle_index = 1 and bundle_index = 3 ", comp_array(one, other))
				o = comp_array(one, other)
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'two_bundle_index': [1, 3], 'diff': o[0], 'only_in_one': o[1], 'only_in_other': o[2], 'bundle_price' : price13[idx], 'bundle_price_diff' : diff(price12[idx])})
print("Finished csv file diff_1_3!")

# for each id compare their dict_yi_index with bundle_index = 1 and bundle_index = 4
with open('output/diff_1_4.csv', 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames = fn_test)
		writer.writeheader()
		for idx in range(0, l):
			one = dict_yi_index_1[idx]
			other = dict_yi_index_4[idx]
			if one == []:
				#print(itemID_all[idx], " bundle_index = 1 does not exist ")
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'two_bundle_index': [1, 4], 'diff': "bundle_index = 1 does not exist", 'only_in_one': [], 'only_in_other': [], 'bundle_price' : 0, 'bundle_price_diff' : 0})
			elif other == []:
				#print(itemID_all[idx], " bundle_index = 4 does not exist ")
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'two_bundle_index': [1, 4], 'diff': "bundle_index = 4 does not exist", 'only_in_one': [], 'only_in_other': [], 'bundle_price' : 0, 'bundle_price_diff' : 0})
			else:
				#print(itemID_all[idx], " diff of bundle_index = 1 and bundle_index = 4 ", comp_array(one, other))
				o = comp_array(one, other)
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'two_bundle_index': [1, 4], 'diff': o[0], 'only_in_one': o[1], 'only_in_other': o[2], 'bundle_price' : price14[idx], 'bundle_price_diff' : diff(price14[idx])})
print("Finished csv file diff_1_4!")


# for each id compare their dict_yi_index with bundle_index = 1 and bundle_index = 5
with open('output/diff_1_5.csv', 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames = fn_test)
		writer.writeheader()
		for idx in range(0, l):
			one = dict_yi_index_1[idx]
			other = dict_yi_index_5[idx]
			if one == []:
				#print(itemID_all[idx], " bundle_index = 1 does not exist ")
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'two_bundle_index': [1, 5], 'diff': "bundle_index = 1 does not exist", 'only_in_one': [], 'only_in_other': [], 'bundle_price' : 0, 'bundle_price_diff' : 0})
			elif other == []:
				#print(itemID_all[idx], " bundle_index = 5 does not exist ")
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'two_bundle_index': [1, 5], 'diff': "bundle_index = 5 does not exist", 'only_in_one': [], 'only_in_other': [], 'bundle_price' : 0, 'bundle_price_diff' : 0})
			else:
				#print(itemID_all[idx], " diff of bundle_index = 1 and bundle_index = 5 ", comp_array(one, other))
				o = comp_array(one, other)
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'two_bundle_index': [1, 5], 'diff': o[0], 'only_in_one': o[1], 'only_in_other': o[2], 'bundle_price' : price15[idx], 'bundle_price_diff' : diff(price15[idx])})
print("Finished csv file diff_1_5!")


# for each id compare their dict_yi_index with bundle_index = 1 and bundle_index = 6
with open('output/diff_1_6.csv', 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames = fn_test)
		writer.writeheader()
		for idx in range(0, l):
			one = dict_yi_index_1[idx]
			other = dict_yi_index_6[idx]
			if one == []:
				#print(itemID_all[idx], " bundle_index = 1 does not exist ")
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'two_bundle_index': [1, 6], 'diff': "bundle_index = 1 does not exist", 'only_in_one': [], 'only_in_other': [], 'bundle_price' : 0, 'bundle_price_diff' : 0})
			elif other == []:
				#print(itemID_all[idx], " bundle_index = 6 does not exist ")
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'two_bundle_index': [1, 6], 'diff': "bundle_index = 6 does not exist", 'only_in_one': [], 'only_in_other': [], 'bundle_price' : 0, 'bundle_price_diff' : 0})
			else:
				#print(itemID_all[idx], " diff of bundle_index = 1 and bundle_index = 6 ", comp_array(one, other))
				o = comp_array(one, other)
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'two_bundle_index': [1, 6], 'diff': o[0], 'only_in_one': o[1], 'only_in_other': o[2], 'bundle_price' : price16[idx], 'bundle_price_diff' : diff(price16[idx])})
print("Finished csv file diff_1_6!")

# for each id compare their dict_yi_index with bundle_index = 1 and bundle_index = 7
with open('output/diff_1_7.csv', 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames = fn_test)
		writer.writeheader()
		for idx in range(0, l):
			one = dict_yi_index_1[idx]
			other = dict_yi_index_7[idx]
			if one == []:
				#print(itemID_all[idx], " bundle_index = 1 does not exist ")
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'two_bundle_index': [1, 7], 'diff': "bundle_index = 1 does not exist", 'only_in_one': [], 'only_in_other': [], 'bundle_price' : 0, 'bundle_price_diff' : 0})
			elif other == []:
				#print(itemID_all[idx], " bundle_index = 7 does not exist ")
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'two_bundle_index': [1, 7], 'diff': "bundle_index = 7 does not exist", 'only_in_one': [], 'only_in_other': [], 'bundle_price' : 0, 'bundle_price_diff' : 0})
			else:
				#print(itemID_all[idx], " diff of bundle_index = 1 and bundle_index = 7 ", comp_array(one, other))
 				o = comp_array(one, other)
 				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'two_bundle_index': [1, 7], 'diff': o[0], 'only_in_one': o[1], 'only_in_other': o[2], 'bundle_price' : price17[idx], 'bundle_price_diff' : diff(price17[idx])})
print("Finished csv file diff_1_7!")


# for each id compare their dict_yi_index with bundle_index = 1 and bundle_index = 8
with open('output/diff_1_8.csv', 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames = fn_test)
		writer.writeheader()
		for idx in range(0, l):
			one = dict_yi_index_1[idx]
			other = dict_yi_index_8[idx]
			if one == []:
				#print(itemID_all[idx], " bundle_index = 1 does not exist ")
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'two_bundle_index': [1, 8], 'diff': "bundle_index = 1 does not exist", 'only_in_one': [], 'only_in_other': [], 'bundle_price' : 0, 'bundle_price_diff' : 0})
			elif other == []:
				#print(itemID_all[idx], " bundle_index = 8 does not exist ")
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'two_bundle_index': [1, 8], 'diff': "bundle_index = 8 does not exist", 'only_in_one': [], 'only_in_other': [], 'bundle_price' : 0, 'bundle_price_diff' : 0})
			else:
				#print(itemID_all[idx], " diff of bundle_index = 1 and bundle_index = 8 ", comp_array(one, other))
				o = comp_array(one, other)
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'two_bundle_index': [1, 8], 'diff': o[0], 'only_in_one': o[1], 'only_in_other': o[2], 'bundle_price' : price18[idx], 'bundle_price_diff' : diff(price18[idx])})
print("Finished csv file diff_1_8!")


print("Done!")



























