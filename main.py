import yagmail
import spreadsheet

# Email Initialization
sender_email = "wangs2997@wrdsb.ca"
sender_password = ""
with open("Authentication/password 1.txt", "r") as f:
    sender_password = f.read()
yag = yagmail.SMTP(user=sender_email, password=sender_password, port=465)


def send_company_emails(x):
    emails_sent = len(spreadsheet.company_emails.col_values(5))
    spreadsheet.company_emails.update_cell(emails_sent + 1, 5, "SENT")

def send_guest_speaker_emails(x):
    # Store list with uncontacted emails
    uncontacted_indices = []

    # For all emails tht don't say yes for contacted, store the index value
    for col in enumerate(spreadsheet.guest_speakers.col_values(3)):
        if col[1].lower() != "yes":
            uncontacted_indices.append(col[0] + 1)

    # First row doesn't count as it's the header
    uncontacted_indices.remove(1)

    # Contact all uncontacted people
    i = 0;
    for uncontacted in uncontacted_indices:
        info = spreadsheet.guest_speakers.row_values(uncontacted)
        print(info)
        name = info[0]

        yag.send(to="seanwaterloo2997@gmail.com", subject="Join Us and Help Us Shape the Next Generation of Engineers",
                contents="Email template.html")
        
        # Contact x many people on the list
        i += 1
        if i >= x:
            break

if __name__ == "__main__":
    send_guest_speaker_emails(1)
    print("Success!")