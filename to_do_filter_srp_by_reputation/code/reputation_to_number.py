import csv
import os

store_rating_enum = {#e:idx for idx, e in enumerate(pd.unique(data_merged.store_rating.ravel()))}
"0×": 0,
"1×心": 1,
"2×心":2,
"3×心":3,
"4×心":4,
"5×心":5,
"1×钻":6,
"2×钻":7,
"3×钻":8,
"4×钻":9,
"5×钻":10,
"1×蓝冠":11,
"2×蓝冠":12,
"3×蓝冠":13,
"4×蓝冠":14,
"5×蓝冠":15,
"1×金冠":16,
"2×金冠":17,
"3×金冠":18,
"4×金冠":19,
"5×金冠":20}

def remove_last(str):
	l = len(str)
	return str[:(l-1)]

file_path = "../input/700D.csv"
with open(file_path) as csvfile:
	csv_opened = csv.DictReader(csvfile)
	all_rank = []
	i = 0
	for row in csv_opened:
		key = row['store_rating']
		if key != "" and key != None:
			all_rank += [store_rating_enum[remove_last(key)]]
		else:
			all_rank += [0]
		i += 1

all_rank = ["rank"] + all_rank
print(all_rank[:10])

inp = "../input/700D.csv"
outp = "../output/700D_with_rank.csv"

with open(inp,'r') as csvinput:
    with open(outp, 'w') as csvoutput:
        writer = csv.writer(csvoutput)
        count = 0
        for row in csv.reader(csvinput):
        	if (count < 2204):
        		writer.writerow(row+[all_rank[count]])
        	count += 1












