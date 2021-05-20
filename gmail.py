import smtplib
import time
import imaplib
import email
import pprint
import html2text
import email.utils




ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "mail.aishwaryashukla" + ORG_EMAIL
FROM_PWD    = "kcqqrerumbpuzlma"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993


# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------

def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('Inbox')

        type, data = mail.search(None, "from accounts.google.com")
        print(type)
        mail_ids = data[0]
        # print(mail_ids)
        # pprint.pprint(data)

        id_list = mail_ids.split()   
        first_email_id = int(id_list[0])
        # print(id_list)
        latest_email_id = int(id_list[-1])
        for num in data[0].split():
            try :

                typ, data = mail.fetch(num, '(RFC822)' )




                for response_part in data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_string(response_part[1].decode('utf-8'))
                        email_subject = msg['subject']
                        email_from = msg['from']
                        print ('From : ' + email_from )
                        print ('Subject : ' + msg['To'] )
                        print ('From : ' + email_from )
                        print(msg.get('date')+ '\n'+ '\n')
                        # print(type(msg))
                        # pprint.pprint(msg.keys())
                        # for k in msg.keys():
                        #     print("{} := {}".format(k, msg[k]))
                        
                        for part in msg.walk():
                            print(part.get_content_type())
                            # print(part.get_payload())
                                # each part is a either non-multipart, or another multipart message
                            # that contains further parts... Message is organized like a tree
                            if part.get_content_type() == 'text/html':
                                print(html2text.html2text(part.get_payload())) # prints the raw text
                        # pprint.pprint(msg.get_payload(decode=True).decode('utf-8'))
                        # pprint.pprint(msg.get_payload(decode=True))
                        # input("test")

                # pprint.pprint(data[0][1])
        #         raw_email = data[0][1]
                
        # # converts byte literal to string removing b''
        #         raw_email_string = raw_email.decode('utf-8')
        #         # pprint.pprint(raw_email_string)
        #         email_message = email.message_from_string(raw_email_string)
        #         pprint.pprint(email_message)
            except Exception as e:
                print(e)
    




    except Exception as e:
        print("err2")

read_email_from_gmail()