import gspread

scope = ['https://www.googlapis.com/feeds',
         'https://www.googlapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file',
         'https://www.googlapis.com/auth/drive']

gc = gspread.service_account(filename="creds.json")
sheet = gc.open("Sponsor Emails").sheet1

data = sheet.get_all_records()

print(data)
# print(sheet.row_values())