import csv

# file.seek(0)  #<-- set the iterator to beginning of the input file
filepath = "source/lst_700d_Jan262016_Combinelist1checked.csv"

# bundle_index = 0 & dict_index is empty
with open(filepath) as csvfile:
	reader = csv.DictReader(csvfile)
	count_0_empty = 0
	for row in reader:
		if row["bundle_index"] == "0" and row["dict_index"] == "":
			count_0_empty += 1
	print("The number of bundle_index=0 and dict_index=None is", count_0_empty)

# bundle_index = 0 & dict_index is not empty
# item id unique
with open(filepath) as csvfile1:
	reader1 = csv.DictReader(csvfile1)
	dictindex_set_zero = []
	for row1 in reader1:
			if row1["bundle_index"] == "0" and row1["dict_index"] != "":
				dictindex_set_zero += [row1["dict_index"]]
	print("dict_index of 0", dictindex_set_zero)
	print("The number of bundle_index=0 and dict_index!=none is", len(dictindex_set_zero))

with open(filepath) as csvfile2:
	reader2 = csv.DictReader(csvfile2)
	count_not0_unique = 0
	for row2 in reader2:
		if row2["bundle_index"] != "0" and row2["dict_index"] not in dictindex_set_zero:
			count_not0_unique += 1
	print("The number of bundle_index!=0 and dict_index is unique is", count_not0_unique)



with open(filepath) as csvfile3:
	reader3 = csv.DictReader(csvfile3)
	count_dict = 0
	for row3 in reader3:
		if row3["dict_index"] != "":
			count_dict += 1
	print("The number of with dict_index is", count_dict)


with open(filepath) as csvfile4:
	reader4 = csv.DictReader(csvfile4)
	count_dict = 0
	for row4 in reader4:
		if row4["dict_index"] in dictindex_set_zero and row4["bundle_index"] != "0":
			count_dict += 1
	print("The number of with dict_index!=0 but with same dict_index as 0 ones is", count_dict)


