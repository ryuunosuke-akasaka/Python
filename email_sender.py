import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Deepak Bucha'
email['to'] = 'idontgiveaflyingfk@gmail.com'
email['subject'] = 'You won nothing !'

email.set_content(html.substitute(amount='Sad'),
                  'html')  # ({'name':'Sad'})

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('buchadeepak@gmail.com', 'okdygxwtoqcnbquf')
    smtp.send_message(email)
    print("All good!")
