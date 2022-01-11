import yagmail
import os
import time
sender='rahuljha59@gmail.com'
receiver='umiuyygcb@netmail.tk'

subject="This is the subject"

contents="""
Here is the content of Email!
"""

while True:
  yag=yagmail.SMTP(user=sender,password=os.getenv('PASSWORD'))
  yag.send(to=receiver,subject=subject,contents=contents)
  print("Email Sent!")
  time.sleep(60)

