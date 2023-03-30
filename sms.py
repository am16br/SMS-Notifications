import smtplib

# Use sms gateway provided by mobile carrier:
# at&t:     number@mms.att.net
# t-mobile: number@tmomail.net
# verizon:  number@vtext.com
# sprint:   number@page.nextel.com

# Establish a secure session with gmail's outgoing SMTP server using your gmail account
server = smtplib.SMTP( "smtp.gmail.com", 587 )

server.starttls()

server.login( 'email@gmail.com', 'password' )
sender = 'email@gmail.com'
to = '1231231234@vtext.com'
subject='Notification'
body='Event happened'
message = ("From: %s\r\n" % sender
             + "To: %s\r\n" % to
             + "Subject: %s\r\n" % subject
             + "\r\n"
             + body)

server.sendmail(sender, to, "hi")

# Send text message through SMS gateway of destination number
