import gspread
import yagmail

# Email Initialization

sender_email = "wangs2997@wrdsb.ca"
sender_password = ""
with open("password 1.txt", "r") as f:
    sender_password = f.read()
yag = yagmail.SMTP(user=sender_email, password=sender_password)

# gspread initialization for Google Sheets API
scope = ['https://www.googlapis.com/feeds',
         'https://www.googlapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file',
         'https://www.googlapis.com/auth/drive']

gc = gspread.service_account(filename="creds.json")
company_emails = gc.open("Sponsor Emails").get_worksheet_by_id(0)
guest_speakers = gc.open("Sponsor Emails").get_worksheet_by_id(1110562774)
test = gc.open("Sponsor Emails").get_worksheet_by_id(428895850)



def send_company_emails(x):
    emails_sent = len(company_emails.col_values(5))
    company_emails.update_cell(emails_sent + 1, 5, "SENT")

def send_guest_speaker_emails(x):
    # Store list with uncontacted emails
    uncontacted_indices = []

    # For all emails tht don't say yes for contacted, store the index value
    for col in enumerate(guest_speakers.col_values(3)):
        if col[1].lower() != "yes":
            uncontacted_indices.append(col[0] + 1)

    # First row doesn't count
    uncontacted_indices.remove(1)

    i = 0;
    for uncontacted in uncontacted_indices:
        info = guest_speakers.row_values(uncontacted)
        name = info[0]
        template = [
            f"Hi {name}!",
            "My name is Peter, I am a high school student and the outreach lead for Highlander Engineering this year. Currently, we are planning on hosting the Highlander Engineering Challenge, a hackathon-style event, in which over 200+ students across Waterloo will be building projects in teams and competing with other high schools. The event will be hosted from May 10 to June 30th.",
            "We were wondering if you would like to host a workshop or AMA with our students. You could talk about work you've done or a topic with respect to your profession. We believe the students will appreciate having you in our club. Click here for more information about times, dates, and other ideas.",
            "I have also attached our speaker information sheet where you can learn more about what it is like to be a guest speaker at Highlander Engineering.",
            "",
            "Looking forward to hearing from you!",
            "",
            "Kind regards,",
            "Peter"
        ]

        yag.send(to="seanwaterloo2997@gmail.com", subject="Join Us and Help Us Shape the Next Generation of Engineers", contents=template)
        
        i += 1
        if i == 5:
            break

send_guest_speaker_emails(1)
print("Success!")

# Store templates on a text file