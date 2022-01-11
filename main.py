import yagmail
import os
import time
from datetime import datetime as dt

sender='rahuljha59@gmail.com'
receiver='umiuyygcb@netmail.tk'

subject="This is the subject"

contents="""
Here is the content of Email!
"""

while True:
    now=dt.now()
    if now.hour==15 and now.minute==27:

      yag=yagmail.SMTP(user=sender,password=os.getenv('PASSWORD'))
      yag.send(to=receiver,subject=subject,contents=contents)
      print("Email Sent!")
      time.sleep(60)

