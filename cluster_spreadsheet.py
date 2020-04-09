import gspread
from oauth2client.service_account import ServiceAccountCredentials
from df2gspread import df2gspread as d2g
import pandas as pd


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)



# initialize list of lists 
data = [["1", "28.5742976 77","77.1667573","305","305"],
["2","28.574297678","77.1667573","55","345"]]
  
# Create the pandas DataFrame 
df = pd.DataFrame(data, columns = ['cluster_name', 'cluster_center_lat',
'cluster_center_lang','cluster_infected_cases','cluster_suspected_cases']) 
  
# print dataframe. 
print(df) 

d2g.upload(df, '1jRfthUvnAiP4d9OzF6B7ZKyOLgg2cGNXygvy7dLS6Ow', wks_name='Cluster_Covid_19', credentials=creds, row_names=True)
# Find a workbook by name and open the first sheet
# Make sure you use the right name here.

 #sheet1 = client.open("Track Covid-19").sheet1

# sheet2 = client.open("Track Covid-19").get_worksheet(1)
# lat_list = sheet1.col_values(4)
# long_list = sheet1.col_values(5)
# i=0
# for lat in lat_list:
#     sheet2.update_cell(i+1, 4, lat)
#     i=i+1

# j=0
# for long in long_list:
#     sheet2.update_cell(j+1, 5, long)
#     j=j+1


# # Extract and print all of the values
# list_of_hashes = sheet2.get_all_records()
# print(sheet1.row_count)