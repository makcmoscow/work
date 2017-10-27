import time
import smtplib
import imaplib
import email




def main():
    emails = {'testmprtv@mail.ru':'imap.mail.ru', 'testmprtv@gmail.com':'imap.gmail.com', 'testmprtv@yandex.ru':'imap.yandex.ru'}
    for mail, srv in emails.items():
        send_email(mail,'From: testmprtv@m-production.tv\nSubject: test: Results\n\nBlaBlaBla')
    time.sleep(1)
    for mail, srv in emails.items():
        recieve_email(mail, srv)

def send_email(to, message):
    pass
    # username = 'testmprtv@m-production.tv'
    # user_pass = '565ts89%w()32'
    # smtp_server = 'mail.m-pr.tv'
    # smtp_port = 25
    # mail_lib = smtplib.SMTP(smtp_server, smtp_port)
    # mail_lib.login(username, user_pass)
    # mail_lib.sendmail(username, to, message)


def recieve_email(mail, srv):
    mailbox = imaplib.IMAP4_SSL(srv)
    mailbox.login(mail, '565ts89%w()32')
    mailbox.select('INBOX')
    mailbox.search(None, 'ALL')
    print(mailbox.search(None, 'ALL'))
    status, data = mailbox.fetch(b'1', '(RFC822)')
    msg = email.message_from_bytes(data[0][1],
                                   _class=email.message.EmailMessage)
    print(msg['Subject'], msg['Date'], mail)






main()