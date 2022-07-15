import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "seanwaterloo2997@gmail.com"
with open("Authentication/password 2.txt", "r") as f:
    password = f.read()
toaddr = "wangs2997@wrdsb.ca"

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "SUBJECT OF THE EMAIL"

body = "Hi NAME!\nMy name is Peter, I am a high school student and the outreach lead for Highlander Engineering this year. Currently, we are planning on hosting the Highlander Engineering Challenge, a hackathon-style event, in which over 200+ students across Waterloo will be building projects in teams and competing with other high schools. The event will be hosted from May 4 to June 30th."

msg.attach(MIMEText(body, 'plain'))

filename = "Mi.png"
attachment = open("Mi.png", "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, password)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

print("Success!")