#!/usr/local/bin/python
#encoding:utf8
'''
Send email.
'''
import os
import re
import smtplib
import email.utils
from email.mime.text import MIMEText
from mailer import Mailer, Message

USERNAME = 'mailman@meilishuo.com'
PASSWD = '5be0d56f'
SERVER = 'mail.meilishuo.com'

def sendmail(mailto, subject, html='', text='', textfile='', htmlfile='', attachments=''):
    '''send mail'''
    if not mailto:
        print 'Error: Empty mailto address.\n'
        return

    mailto = [sb.strip() for sb in mailto.split(',')]
    if attachments:
        attachments = [att.strip() for att in attachments.split(',')]
    else:
        attachments = []

    message = Message(From=USERNAME, To=mailto, Subject=subject)
    message.Body = text
    message.Html = html
    message.charset = 'utf8'
    try:
        if htmlfile:
            message.Html += open(htmlfile, 'r').read()
        if textfile:
            message.Body += open(textfile, 'r').read()
    except IOError:
        pass

    for att in attachments:
        message.attach(att)

    sender = Mailer(SERVER)
    sender.login(USERNAME, PASSWD)
    sender.send(message)

def main():
    import argparse
    parser = argparse.ArgumentParser(description = 'Email sending tool')
    parser.add_argument('-m', '--mailto', dest='mailto', help='mailboxes delimited by comma')
    parser.add_argument('-s', '--subject', dest='subject', default='')
    parser.add_argument('-t', '--html', dest='html', default='')
    parser.add_argument('-e', '--text', dest='text', default='')
    parser.add_argument('--text-file', dest='textfile', default='')
    parser.add_argument('--html-file', dest='htmlfile', default='')
    parser.add_argument('-a', '--attachment', dest='attachments', help='paths of attachments delimited by comma')
    args = parser.parse_args()

    if not args.mailto:
        print 'Error: Empty mailto address.\n'
        parser.print_help()
        return

    sendmail(args.mailto, args.subject, args.html, args.text, args.htmlfile, args.textfile, args.attachments)

    
if __name__ == "__main__":
    main()

