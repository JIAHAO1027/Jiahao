Python part
	First run diffDictidx.py
	input is "/input/new_lst_700D_Yi_Feb222016_giftindex_price_corrected_juexiao( 2016-03-05).csv"

	output is "/output/with1_diffDictIdx_output.csv" and "/output/step1_diffDictIdx_output.csv"
	"with1_diffDictIdx_output.csv" is bundle one compared with bundle n
	columnname = ['Author', 'ItemID(LIsting_id)', 'another_bundle_index'(n), 'diff'(dn), 'only_in_one'(Vector), 'only_in_other'(Vector), 'in_both'(Vector)]


	"step1_diffDictIdx_output.csv" is bundle n (for n from 2 ~ 7) compared with n+1
	columnname = ['Author', 'ItemID(LIsting_id)', 'two_bundle_index', 'diff'(dn), 'only_in_one'(Vector), 'only_in_other'(Vector), 'in_both'(Vector)]

	Second run make_dict_table.py
	 input: /input/dict_700d_750d_Feb082016.csv
			/input/with1_diffDictIdx_output.csv
			/input/with1_diffDictIdx_output.csv

	 output: /output/dictIdx_table.csv this output is for get_regression.Rmd
	         /output/forgraph.csv this output is for histogram of bundle 1 compared with 2~8
			 /output/for_individual_graph.csv this output is individual graph of bundle 1 compared with bundle 2~8

R part
Run get_histogram.Rmd to get the histogram of all bundle and individual bundle
Run get_regression.Rmd to get data table for regression output is : regresstion_data.csv
