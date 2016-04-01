import os
os.system("python gen_700_750.py")
os.system("python table_700_750.py")
os.system("ipython price_fake_id.py")
os.system("Rscript convert_jiahao_result_to_good_format.R")
