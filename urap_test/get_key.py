import jieba
import csv
import os

jieba.add_word('闪迪')
jieba.add_word('sd卡')
jieba.add_word('SD卡')
jieba.add_word('高速卡')
jieba.add_word('微单反')
jieba.add_word('卡套')


file_path = "input/dic/CC01.csv"

with open(file_path) as csvfile:
	csv_opened = csv.DictReader(csvfile)
	total_key = []
	for row in csv_opened:
		st = row["item_title"]
		seg_list = jieba.cut(st, cut_all=True)
		s = " ".join(seg_list)
		total_key += [s.split()]



with open("input/dic/CC01.csv",'r') as csvinput:
    with open("output/CC01_with_key.csv", 'w', encoding='utf-8-sig' ) as csvoutput:

        writer = csv.writer(csvoutput)
        count = -1

        for row in csv.reader(csvinput):
        	if count < 0:
        		writer.writerow(row+['Keys'])
        	else:
        		writer.writerow(row+[total_key[count]])
        	count += 1




