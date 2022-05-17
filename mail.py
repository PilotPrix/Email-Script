import yagmail
import spreadsheet

# Sending Emails
sender_email = "wangs2997@wrdsb.ca"
sender_password = ""
with open("Password 1.txt", "r") as f:
    sender_password = f.read()

receiver_emails = ["wangzhan3000@rogers.com", "zhanf2495@wrdsb.ca", "shara8586@wrdsb.ca",
                    "kwaks8819@wrdsb.ca", "zhaof8586@wrdsb.ca", "wangc4574@wrdsb.ca", "chens4256@wrdsb.ca", "chaup3074@wrdsb.ca",
                    "wongt5807@wrdsb.ca", "fengv4786@wrdsb.ca", "renj5722@wrdsb.ca", "zhanc9114@wrdsb.ca",
                    "chana8034@wrdsb.ca", "kims8448@wrdsb.ca", "wangs2997@wrdsb.ca"]
yag = yagmail.SMTP(user=sender_email, password=sender_password)

print("Sending email...")

# subject = "Congradulations, you've been selected as the chosen one for the python script's victim"
subject = "Please check your spam mail for some hidden treaure!! ✨🎃😀"
contents = [
    # "bruh moment bruh moment bruh moment bruh moment bruh moment bruh moment",
    # "bruh moment bruh moment bruh moment bruh moment bruh moment bruh moment",
    # "bruh moment bruh moment bruh moment bruh moment bruh moment bruh moment",
    # "bruh moment bruh moment bruh moment bruh moment bruh moment bruh moment",
    # "bruh moment bruh moment bruh moment bruh moment bruh moment bruh moment",
    # "bruh moment bruh moment bruh moment bruh moment bruh moment bruh moment",
    # "bruh moment bruh moment bruh moment bruh moment bruh moment bruh moment",
    # "bruh moment bruh moment bruh moment bruh moment bruh moment bruh moment",
    # "bruh moment bruh moment bruh moment bruh moment bruh moment bruh moment",
    # "bruh moment bruh moment bruh moment bruh moment bruh moment bruh moment",
    # "bruh moment bruh moment bruh moment bruh moment bruh moment bruh moment",
    # "bruh moment bruh moment bruh moment bruh moment bruh moment bruh moment",
    # "bruh moment bruh moment bruh moment bruh moment bruh moment bruh moment",
    # "bruh moment bruh moment bruh moment bruh moment bruh moment bruh moment",
    # "bruh moment bruh moment bruh moment bruh moment bruh moment bruh moment",
    # "bruh moment bruh moment bruh moment bruh moment bruh moment bruh moment",
    # "bruh moment bruh moment bruh moment bruh moment bruh moment bruh moment",
    # "bruh moment bruh moment bruh moment bruh moment bruh moment bruh moment",
    # "bruh moment bruh moment bruh moment bruh moment bruh moment bruh moment",
    # "bruh moment bruh moment bruh moment bruh moment bruh moment bruh moment",
    # "bruh moment bruh moment bruh moment bruh moment bruh moment bruh moment",
    # "bruh moment bruh moment bruh moment bruh moment bruh moment bruh moment",
    # "C:\_Programming\Python\Email Script\Mi.png"
]

for receiver_email in receiver_emails:
    for i in range (0, 1):
        yag.send(to=receiver_email, subject=subject, contents=contents)
        print("Sent to", receiver_email, i)

print("Success!")