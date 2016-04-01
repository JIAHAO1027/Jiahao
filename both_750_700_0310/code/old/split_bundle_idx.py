import csv
import os
import ast

file_path = "../output/dictIdx_table_pr_fk_20160314.csv"

fn = "ItemID", "first_bundle_index", "second_bundle_index", 
"camera_name", "deltaN", "dic_index", "dictIdx_top2", "first", "price","fake_brand_id"
with open('../output/dictIdx_table_new.csv', 'w') as csvfile:
	writer = csv.DictWriter(csvfile, fieldnames = fn)
	writer.writeheader()
	with open(file_path) as iput:
		csv_opened = csv.DictReader(iput)
		for row in csv_opened:
			writer.writerow({'ItemID': row["ItemID"] ,'first_bundle_index': ast.literal_eval(row["two_bundle_index"])[0], 
				'second_bundle_index': ast.literal_eval(row["two_bundle_index"])[1], "camera_name": row["camera_model"], 
				'deltaN': row['deltaN'], 'dic_index': row['dic_index'], 
				'dictIdx_top2': row['dictIdx_top2'], 'first': row['first'], "price": row['price'], 'fake_brand_id': row['fake_brand_id']})


