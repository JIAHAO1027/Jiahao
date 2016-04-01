import csv
import os

file_path = "../input/lst_700D_Yi_Feb222016_giftindex_price_corrected_juexiao_0306.csv"

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

	in_both = only_in_one + only_in_other

	return (count, only_in_one, only_in_other, in_both)


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


fn = ['Author', 'ItemID(LIsting_id)', 'another_bundle_index', 'diff', 'only_in_one', 'only_in_other', 'in_both']
an = "Jiahao"

def get_top2(x):
	result = []
	for i in x:
		result += [i[:2]]
	return result

with open('../output/with1_diffDictIdx_output.csv', 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames = fn)
		writer.writeheader()
		for i in range(2,9):
			for idx in range(0, l):
				one = dict_yi_index_1[idx]
				other_array = [dict_yi_index_2[idx], dict_yi_index_3[idx], dict_yi_index_4[idx],
				dict_yi_index_5[idx], dict_yi_index_6[idx], dict_yi_index_7[idx], dict_yi_index_8[idx]]
				other = other_array[i - 2]
				if one == []:
					#print(itemID_all[idx], " bundle_index = 1 does not exist ")
					writer.writerow({'Author': an, 'ItemID(LIsting_id)': str(itemID_all[idx]), 'another_bundle_index': i, 'diff': "", 'only_in_one': [], 'only_in_other': [], 'in_both': []})
				elif other == []:
					#print(itemID_all[idx], " bundle_index = 2 does not exist ")
					writer.writerow({'Author': an, 'ItemID(LIsting_id)': str(itemID_all[idx]), 'another_bundle_index': i, 'diff': "", 'only_in_one': [], 'only_in_other': [], 'in_both': []})
				else:
					#print(itemID_all[idx], " diff of bundle_index = 1 and bundle_index = 2 ", comp_array(one, other))
					o = comp_array(one, other)
					writer.writerow({'Author': an, 'ItemID(LIsting_id)': str(itemID_all[idx]), 
						'another_bundle_index': i, 'diff': o[0], 'only_in_one': o[1], 
						'only_in_other': o[2], 'in_both': get_top2(o[3])})


fn = ['Author', 'ItemID(LIsting_id)', 'two_bundle_index', 'diff', 'only_in_one', 'only_in_other', 'in_both']

with open('../output/step1_diffDictIdx_output.csv', 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames = fn)
		writer.writeheader()
		for i in range(0,6):
			for idx in range(0, l):

				one_array = [dict_yi_index_2[idx], dict_yi_index_3[idx], dict_yi_index_4[idx],
				dict_yi_index_5[idx], dict_yi_index_6[idx], dict_yi_index_7[idx], dict_yi_index_8[idx]]

				other_array = [dict_yi_index_2[idx], dict_yi_index_3[idx], dict_yi_index_4[idx],
				dict_yi_index_5[idx], dict_yi_index_6[idx], dict_yi_index_7[idx], dict_yi_index_8[idx]]

				one = one_array[i]
				other = other_array[i + 1]
				if one == []:
					#print(itemID_all[idx], " bundle_index = 1 does not exist ")
					writer.writerow({'Author': an, 'ItemID(LIsting_id)': str(itemID_all[idx]), 'two_bundle_index': [], 'diff': "", 'only_in_one': [], 'only_in_other': [], 'in_both': []})
				elif other == []:
					#print(itemID_all[idx], " bundle_index = 2 does not exist ")
					writer.writerow({'Author': an, 'ItemID(LIsting_id)': str(itemID_all[idx]), 'two_bundle_index': [], 'diff': "", 'only_in_one': [], 'only_in_other': [], 'in_both': []})
				else:
					#print(itemID_all[idx], " diff of bundle_index = 1 and bundle_index = 2 ", comp_array(one, other))
					o = comp_array(one, other)
					writer.writerow({'Author': an, 'ItemID(LIsting_id)': str(itemID_all[idx]), 
						'two_bundle_index': [i + 2, i + 3], 'diff': o[0], 'only_in_one': o[1], 
						'only_in_other': o[2], 'in_both': get_top2(o[3])})









