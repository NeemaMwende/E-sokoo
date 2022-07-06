import smtplib

from email.mime.text import MIMEText
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.template.loader import render_to_string

def send_welcome_email(name, receiver):
    # Creating message subject and sender
    subject = 'Welcome to E-soko NewsLetter'
    sender = 'florenceappdev@gmail.com'

    # passing in context variables
    text_content = render_to_string('email/newsemail.txt', {'name': name})
    html_content = render_to_string('email/newsemail.html', {'name': name})

    msg = EmailMultiAlternatives(subject, text_content, sender, [receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()

    
# msg = MIMEText('E-Soko NewsLetter')
# msg['Subject'] = "Welcome to  E-soko"
# msg['From']    = "florenceappdev@gmail.com"
# msg['To']      = "bar@example.com"

# s = smtplib.SMTP('smtp.mailgun.org', 587)

# s.login('postmaster@YOUR_DOMAIN_NAME', '3kh9umujora5')
# s.sendmail(msg['From'], msg['To'], msg.as_string())
# s.quit()