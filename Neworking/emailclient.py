import smtplib

from email.mime.text import MIMEText

# build email body

body = "This is python bootcamp... today is Monday 25th October"

msg = MIMEText(body)

msg["From"]  = "chetubapodara@gmail.com"

msg["To"]  = " chjkbap@yahoo.com"

msg["Subject"]  = " Your Email Message for Python"

server = smtplib.SMTP("smtp.gmail.com", 587)

server.starttls()

server.login("chetubapodara@gmail.com", "jyzmpncpcwbsedbq")

server.send_message(msg)

print("Mail sent")
server.quit()


