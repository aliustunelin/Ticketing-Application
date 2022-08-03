import logging
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from datetime import datetime

class logger:
    def mailLogger(self, message, statusCode, module):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("this-is-costumer-web-site.com", 465, context=context) as s:
            # s = smtplib.SMTP(host='smtp.google.com',port=465)
            print('going down')
            # s.starttls()
            s.login('logger@ali.com', 'aQd1w#31')
            print('we are in')
            msg = MIMEMultipart()
            msg['From']='logger@ali.com'
            msg['To']='development@ali.com'
            msg['X-Priority']='1'
            msg['Subject']="Application Error on Costumer Server: "+str(statusCode)
            
            logTime = datetime.now()
            msg.attach(MIMEText('Time:'+str(logTime)+'\nStatus Code:'+str(statusCode)+'\nApplication:'+module+'\nError:'+str(message), 'plain'))
            print('sending now')
            s.send_message(msg)
            print('gone....')
            del msg
        # mail_handler = SMTPHandler(
        #     mailhost='server.ali.com',
        #     fromaddr='logger@ali.com',
        #     toaddrs=['development@ali.com', 'aliustunelin@gmail.com'],
        #     subject='Application Error on Costumer Server',
        #     credentials=('logger@ali.com','aQd1w#31')
        # )
        # logTime = datetime.now
        # levelname = statusCode        
        # mail_handler.setLevel(logging.ERROR)
        # mail_handler.setFormatter(logging.Formatter(
        #     '[%(logTime)s] %(levelname)s in %(module)s: %(message)s'
        # ))
        # if not app.debug:
        #     app.logger.addHandler(mail_handler)
        #     app.logger.removeHandler(default_handler)   