import pandas as pd
# save filepath to variable for easier access
KPI_file_path = '../input/datapath'
# read the data and store data in DataFrame titled KPI_data
KPI_data = pd.read_csv(KPI_file_path) 
# print a summary of the data 
KPI_data.describe()