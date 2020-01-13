#e1.1 with picture
##################
import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

sender_email = "radvanszkyij@gmail.com"
receiver_email = "radvanszkyij@gmail.com"
password = "*******"
ImgFileName="kep.png"

img_data = open(ImgFileName, 'rb').read()
message = MIMEMultipart("alternative")
message["Subject"] = "üzenet a földnedvesség-mérőtől"
message["From"] = sender_email
message["To"] = receiver_email


# Create the plain-text and HTML version of your message
#text = """\
#Hi,
#How are you?
#Real Python has many great tutorials:
#www.realpython.com"""
html = """\
<html>
<h1 align="center">Kedves felhasználó!</h1>
<font size="4">Az Ön által gondozott növény földjének nedvesség<br>
tartalma a kritikus érték alá sülyedt.<br>
Öntözze meg a növényét!</font>
<img src="C:/Users/rijon/28767881_2038175236467148_221478428_o.png">
</html>
"""

# Turn these into plain/html MIMEText objects
#part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")
image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first

message.attach(image)
#message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
    print('Hello ! I am finished')