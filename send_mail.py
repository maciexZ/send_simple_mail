#!/bin/python3

"""
script for simply sending emails from set email from cli and scripts
"""

import argparse
import configparser
import os,sys
from send_simple_mail import Mail

#creating config reader for creditials from ~/.config/send_simple_mail/config
config = configparser.ConfigParser()
config.read(os.path.join(os.getenv("HOME"),".config/send_simple_mail/config"))

""" 
creating parser for arguments (-es --emailsender name of section in config file with creditials -a --address for email of recipient, 
# -s --subject for subject of mail, -t --text for email text, -f --files for attachments). 
The first three are mandatory, the rest is optional.  
"""
parser = argparse.ArgumentParser()

if __name__ == "__main__":
    # display help and version
    parser.add_argument('-v', '--version', action='version',
                        version='send_simple_mail 1.0')
    parser.add_argument("-es", "--emailsender",
                        help="name of email sender configured in config")
    parser.add_argument("-a", "--address", required=True, nargs="+",
                        help = "recipient(s) address(es)")
    parser.add_argument("-s", "--subject", required=True, help="email subject")
    parser.add_argument("-t", "--text", help= "email text")
    #for text attachment
    parser.add_argument("-f", "--files", nargs="+",help="adding textfile attachment")
    #for binary files attachment
    parser.add_argument("-fb", "--filesbinary", nargs="+",help="adding binary file attachment ")


    #parsing arguments from user
    args = parser.parse_args()
    if args.emailsender != None:
        sender = args.emailsender
    else:
        sender = "DEFAULT"
    emails = args.address
    subject = args.subject
    text = args.text

    #creating mail object with data from config file
    try:
        mailconf = config[sender]
    except KeyError as e:
        sys.exit("No such email in configfile.")
    try:
        mail = Mail(mailconf["EMAIL"], mailconf["PASS"], mailconf["SMTP"], mailconf["PORT"])
    except KeyError:
        sys.exit("Error in config file. Check whether the sections: EMAIL, PASS, SMTP and PORT are properly configured")

    for recipient in emails:
        mail.new_message(subject, recipient)
        mail.add_content(text)
        if args.files != None:
            for attachment in args.files:
                if attachment.strip()[0] != "/":
                    mail.add_atachments_plain(os.path.join(os.getcwd(), attachment))
                else:
                    mail.add_atachments_plain(attachment)
        if args.filesbinary != None:
            for attachment in args.filesbinary:
                if attachment.strip()[0] != "/":
                    mail.add_attachment_binary(os.path.join(os.getcwd(), attachment))
                else:
                    mail.add_attachment_binary(attachment)
        print(f"Sending email to: {recipient}.\nSubject: {subject}.\nBody: {text}.\nAttachments: {args.files}")
        mail.send_mail()