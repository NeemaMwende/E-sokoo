from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(name,receiver):
    # Creating message subject and sender
    subject = 'Welcome to the E-soko NewsLetter'
    sender = 'postmaster@sandbox7895da5ac08144e89546d986e38d677e.mailgun.org'

    #passing in the context vairables
    text_content = render_to_string('email/newsemail.txt',{"name": name})
    html_content = render_to_string('email/newsemail.html',{"name": name})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()


# def send_welcome_email(name,receiver):
#     # Creating message subject and sender
#     subject = 'E-SOKO'
#     sender = 'esokoapp2222@gmail.com'

#     #passing in the context vairables
#     text_content = render_to_string('email/registeremail.txt',{"name": name})
#     html_content = render_to_string('email/registeremail.html',{"name": name})

#     msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
#     msg.attach_alternative(html_content,'text/html')
#     msg.send()