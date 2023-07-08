# Automatic Keylogger Upon Machine Startup
#### It is just for educational purposes only. If you understand how this kind of attack works, you can better protect yourself from it! YOU ARE RESPONSIBLE FOR YOUR ACTIONS!

# 1: logger_0.3.pyw
Summary: Capturing keystrokes and sending them to the email!

## Importing the Libraries
This script works first by importing the necessary libraries like "smtplib" for sending emails, "threading" for running the keylogger, "time" for the time interval of sending the logs, "email.mime.text" for creating email messages, and "pynput.keyboard" for capturing keystrokes.

## Setting the Email for Sending the Logs
In this part, we will set up the username and the password of the SMTP server that we are using! I would recommend to use MAILTRAP, because it is easy and free to use! 
![image](https://github.com/hassnshahir/keylogger/assets/133601250/ac0a2ef0-7d01-4830-b6b7-6004c2588123)

## "KeyLogger" Class
The defined "KeyLogger" class uses time interval, and email address as parameters to use during initialization! The "appendlog" captures the keystrokes. The "save_data" converts a key to a string, it handles special keys separately. The "send_mail" carries the logs via email. I have used MAILTRAP as an SMTP provider, but you can replace it with your own SMTP provider. The "report" works by the time interval which is fixed by the "SEND_REPORT_EVERY" variable. The "run" sets up a keyboard listener. Finally the "start" is used for starting the keylogger in a separate thread. 



