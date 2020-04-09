import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Track Covid-19").sheet1
rows = ['0','1','2','3','4','3','2','1','0','1','3','2','0','3','1','2',
'0','1','2','3','4','3','2','1','0','1','3','2','0','3','1']
# sheet.add_cols(1)
# #sheet.update_acell('I1', 'Cluster Label')
 
# cell_list_lat = sheet.range('D1:D32')
# cell_list_long = sheet.range('E1:E32')
for i in range(sheet.row_count-1):
#         cellname = 'I'+str(j+1)
    sheet.update_cell(i+2, 9, rows[i])
    
# Extract and print all of the values
list_of_hashes = sheet.get_all_records()
print(list_of_hashes)