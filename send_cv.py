import email
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass
import os


mail_content = '''
Bonjour

Je suis à la recherche d'un emploi en tant que ingénieur systèmes et réseaux.

Veuillez trouver ci-joint mon CV contenant toutes mes informations personnelles, mon cursus scolaire et mes expériences professionnelles, et j'espère que ma candidature sera prise en considération.

ATTATFA Abdelghani.

Cordialement.'''

# The mail addresses and password
#sender_address = 'abdelghani.attatfa@gmail.com'
sender_address = os.environ["GMAIL"]
print(sender_address)
#sender_pass = 'sudo attatfa TOOR 12341991'
sender_pass = getpass.getpass()
# receiver_addresses = ['ghani894@gmail.com', 'a.attatfa@esi-sba.dz']
# Setup the MIME

# Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
session.starttls()  # enable security
session.login(sender_address, sender_pass)  # login with mail_id and password

filename = "../Abdelghani_Attatfa_CV_en.pdf"  # In same directory as script

# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string


with open("emails.txt_") as fp:
    receiver_addresses = fp.readlines()
    for receiver_address in receiver_addresses:
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        # The subject line
        message['Subject'] = 'Ingénieur systèmes et réseaux'
        # The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'plain'))
        message.attach(part)
        text = message.as_string()

        session.sendmail(sender_address, receiver_address, text)
        print("Sent to {0}".format(receiver_address))

session.quit()
print('Done')
