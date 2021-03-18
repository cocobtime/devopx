

# libraries to be imported 
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 


value = []



#body, kk= trends()
#function for mail


def sendEmail(tweet,kk):
    body = '\n'.join(tweet)
    fromaddr = "cocopolice@gmail.com"
    toaddr = "jote532hamu@post.wordpress.com"

# MIMEMultipart 
    msg = MIMEMultipart() 

# senders email address 
    msg['From'] = fromaddr 

# receivers email address 
    msg['To'] = toaddr 

# the subject of mail
    msg['Subject'] = kk

# the body of the mail 


# attaching the body with the msg 
    msg.attach(MIMEText(body, 'plain')) 




# MIMEBase


# creates SMTP session 
    email = smtplib.SMTP('smtp.gmail.com', 587) 

# TLS for security 
    email.starttls() 

# authentication 
    email.login(fromaddr, "fhxz hmfa mbpl wplb") 

# Converts the Multipart msg into a string 
    message = msg.as_string() 

# sending the mail 
    email.sendmail(fromaddr, toaddr, message) 

# terminating the session 
    quit() 
