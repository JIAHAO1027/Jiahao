# Author: Jiahao Huang
# Data: Feb-18-2016
# This program is for count the difference of dict_index between bundle_1 and bundle_n for n > 1
# Out put will be several diff_1_n.csv file for some n > 1

import csv
import os


# Set working directory
#os.chdir("/Users/Jiahao/Dropbox/urap_programming/Jiahao/relative_premium")
# Target file
# Put your file path here!
file_path = "../input/lst_700D_Yi_Feb222016_giftindex_price_corrected_juexiao.csv"

# This part is for count

# Compare two array and return the difference
def comp_array(one, other):
	count = 0
	for i in other:
		if i not in one:
			count += 1

	for i in one:
		if i not in other:
			count += 1

	return count

# Find the unique item id.
# Open the csv file.
with open(file_path) as csvfile:
	csv_opened = csv.DictReader(csvfile)
	itemID_all = []
	for row in csv_opened:
		if row["ItemID(LIsting_id)"] not in itemID_all:
			itemID_all += [row["ItemID(LIsting_id)"]]
print("Finished count all item id")

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
#print(len(dict_yi_index_4))
print("Finished count dict_yi_index_4")

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
#print(len(dict_yi_index_5))
print("Finished count dict_yi_index_5")



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
#print(len(dict_yi_index_6))
print("Finished count dict_yi_index_6")


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
#print(len(dict_yi_index_7))
print("Finished count dict_yi_index_7")


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
#print(len(dict_yi_index_8))
print("Finished count dict_yi_index_8")
l = len(dict_yi_index_8)


# This part is for Write file

# csv file filenames here
fn = ['Author', 'ItemID(LIsting_id)', 'diff']

# Author name
an = "Jiahao"

# for each id compare their dict_yi_index with bundle_index = 1 and bundle_index = 2
with open('../output/diff_1_2.csv', 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames = fn)
		writer.writeheader()
		for idx in range(0, l):
			one = dict_yi_index_1[idx]
			other = dict_yi_index_2[idx]
			if one == []:
				#print(itemID_all[idx], " bundle_index = 1 does not exist ")
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'diff': "bundle_index = 1 does not exist"})
			elif other == []:
				#print(itemID_all[idx], " bundle_index = 2 does not exist ")
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'diff': "bundle_index = 2 does not exist"})
			else:
				#print(itemID_all[idx], " diff of bundle_index = 1 and bundle_index = 2 ", comp_array(one, other))
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'diff': comp_array(one, other)})
print("Finished csv file diff_1_2!")


# for each id compare their dict_yi_index with bundle_index = 1 and bundle_index = 3
with open('../output/diff_1_3.csv', 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames = fn)
		writer.writeheader()
		for idx in range(0, l):
			one = dict_yi_index_1[idx]
			other = dict_yi_index_3[idx]
			if one == []:
				#print(itemID_all[idx], " bundle_index = 1 does not exist ")
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'diff': "bundle_index = 1 does not exist"})
			elif other == []:
				#print(itemID_all[idx], " bundle_index = 3 does not exist ")
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'diff': "bundle_index = 3 does not exist"})
			else:
				#print(itemID_all[idx], " diff of bundle_index = 1 and bundle_index = 3 ", comp_array(one, other))
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'diff': comp_array(one, other)})
print("Finished csv file diff_1_3!")

# for each id compare their dict_yi_index with bundle_index = 1 and bundle_index = 4
with open('../output/diff_1_4.csv', 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames = fn)
		writer.writeheader()
		for idx in range(0, l):
			one = dict_yi_index_1[idx]
			other = dict_yi_index_4[idx]
			if one == []:
				#print(itemID_all[idx], " bundle_index = 1 does not exist ")
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'diff': "bundle_index = 1 does not exist"})
			elif other == []:
				#print(itemID_all[idx], " bundle_index = 4 does not exist ")
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'diff': "bundle_index = 4 does not exist"})
			else:
				#print(itemID_all[idx], " diff of bundle_index = 1 and bundle_index = 4 ", comp_array(one, other))
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'diff': comp_array(one, other)})
print("Finished csv file diff_1_4!")


# for each id compare their dict_yi_index with bundle_index = 1 and bundle_index = 5
with open('../output/diff_1_5.csv', 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames = fn)
		writer.writeheader()
		for idx in range(0, l):
			one = dict_yi_index_1[idx]
			other = dict_yi_index_5[idx]
			if one == []:
				#print(itemID_all[idx], " bundle_index = 1 does not exist ")
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'diff': "bundle_index = 1 does not exist"})
			elif other == []:
				#print(itemID_all[idx], " bundle_index = 5 does not exist ")
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'diff': "bundle_index = 5 does not exist"})
			else:
				#print(itemID_all[idx], " diff of bundle_index = 1 and bundle_index = 5 ", comp_array(one, other))
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'diff': comp_array(one, other)})
print("Finished csv file diff_1_5!")


# for each id compare their dict_yi_index with bundle_index = 1 and bundle_index = 6
with open('../output/diff_1_6.csv', 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames = fn)
		writer.writeheader()
		for idx in range(0, l):
			one = dict_yi_index_1[idx]
			other = dict_yi_index_6[idx]
			if one == []:
				#print(itemID_all[idx], " bundle_index = 1 does not exist ")
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'diff': "bundle_index = 1 does not exist"})
			elif other == []:
				#print(itemID_all[idx], " bundle_index = 6 does not exist ")
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'diff': "bundle_index = 6 does not exist"})
			else:
				#print(itemID_all[idx], " diff of bundle_index = 1 and bundle_index = 6 ", comp_array(one, other))
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'diff': comp_array(one, other)})
print("Finished csv file diff_1_6!")

# for each id compare their dict_yi_index with bundle_index = 1 and bundle_index = 7
with open('../output/diff_1_7.csv', 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames = fn)
		writer.writeheader()
		for idx in range(0, l):
			one = dict_yi_index_1[idx]
			other = dict_yi_index_7[idx]
			if one == []:
				#print(itemID_all[idx], " bundle_index = 1 does not exist ")
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'diff': "bundle_index = 1 does not exist"})
			elif other == []:
				#print(itemID_all[idx], " bundle_index = 7 does not exist ")
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'diff': "bundle_index = 7 does not exist"})
			else:
				#print(itemID_all[idx], " diff of bundle_index = 1 and bundle_index = 7 ", comp_array(one, other))
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'diff': comp_array(one, other)})
print("Finished csv file diff_1_7!")

# for each id compare their dict_yi_index with bundle_index = 1 and bundle_index = 8
with open('../output/diff_1_8.csv', 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames = fn)
		writer.writeheader()
		for idx in range(0, l):
			one = dict_yi_index_1[idx]
			other = dict_yi_index_8[idx]
			if one == []:
				#print(itemID_all[idx], " bundle_index = 1 does not exist ")
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'diff': "bundle_index = 1 does not exist"})
			elif other == []:
				#print(itemID_all[idx], " bundle_index = 8 does not exist ")
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'diff': "bundle_index = 8 does not exist"})
			else:
				#print(itemID_all[idx], " diff of bundle_index = 1 and bundle_index = 8 ", comp_array(one, other))
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'diff': comp_array(one, other)})
print("Finished csv file diff_1_8!")



# for each id compare their dict_yi_index with bundle_index = 1 and bundle_index = 8
with open('../output/diff_1_8.csv', 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames = fn)
		writer.writeheader()
		for idx in range(0, l):
			one = dict_yi_index_1[idx]
			other = dict_yi_index_8[idx]
			if one == []:
				#print(itemID_all[idx], " bundle_index = 1 does not exist ")
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'diff': "bundle_index = 1 does not exist"})
			elif other == []:
				#print(itemID_all[idx], " bundle_index = 8 does not exist ")
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'diff': "bundle_index = 8 does not exist"})
			else:
				#print(itemID_all[idx], " diff of bundle_index = 1 and bundle_index = 8 ", comp_array(one, other))
				writer.writerow({'Author': an, 'ItemID(LIsting_id)': itemID_all[idx], 'diff': comp_array(one, other)})

print("Finished csv file diff_1_8!")

print("Done!")



























