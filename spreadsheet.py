import gspread


# gspread initialization for Google Sheets API
scope = ['https://www.googlapis.com/feeds',
         'https://www.googlapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file',
         'https://www.googlapis.com/auth/drive']

gc = gspread.service_account(filename="creds.json")
company_emails = gc.open("Sponsor Emails").get_worksheet_by_id(0)
guest_speakers = gc.open("Sponsor Emails").get_worksheet_by_id(1110562774)
test = gc.open("Sponsor Emails").get_worksheet_by_id(428895850)
