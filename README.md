# Automatic Keylogger Upon Machine Startup
#### It is just for educational purposes only. It is only to understand how this kind of attack works, so you can better protect yourself from it! YOU ARE RESPONSIBLE FOR YOUR ACTIONS!


# 1: logger_0.3.pyw
Summary: Capturing keystrokes and sending them to the email!


* ### Importing the Libraries: 
  This script works first by importing the necessary libraries like 'smtplib' for sending emails, "threading" for running the keylogger, "time" for the time interval of sending the logs, "email.mime.text" for creating email messages, and "pynput.keyboard" for capturing keystrokes.


* ### Setting the Email for Sending the Logs:
  In this part, we will set up the username and password of the SMTP server that we are using! I would recommend using MAILTRAP because it is easy and free to use! 

![image](https://github.com/hassnshahir/keylogger/assets/133601250/ac0a2ef0-7d01-4830-b6b7-6004c2588123)


* ### "KeyLogger" Class:
  The defined "KeyLogger" class uses time interval, and email address as parameters to use during initialization! The "appendlog" captures the keystrokes. The "save_data" converts a key to a string, it handles special keys    separately. The "send_mail" carries the logs via email. I have used MAILTRAP as an SMTP provider, but you can replace it with your own SMTP provider. The "report" works by the time interval which is fixed by the             "SEND_REPORT_EVERY" variable. The "run" sets up a keyboard listener. Finally the "start" is used for starting the keylogger in a separate thread. 

## This will work properly but to make it run itself after every restart of the machine, another script should be created! [startup_keylogger_0.3.pyw]
First of all, if we only want to use this script in a machine without installing any dependencies. it is important to convert it to an executable file! So we will make the keylogger_0.3.pyw to a .exe file by the command "pyinstaller --onefile keylogger_0.3.pyw" Make sure to open the terminal in the same folder as the keylogger_0.3.pyw is located. Then we will create a script that runs the .exe file by startup. 


# 2: logger_0.3_startup.pyw
Summary: Adding the keylogger_0.3.exe to the Startup

### To run this code, you need to ensure that:
* You run this code with administrative privileges.
* You have the logger_0.3.exe file in the same directory as this script.

# 3: Final File
I would recommend converting both files to a .exe file. Whenever you want to run the it.
  1: Run the keylogger_0.3.exe 
  2: Run the startup_keylogger_0.3.exe 
BUT MAKE SURE THAT THEY ARE BOTH IN THE SAME FOLDER!

## In a world that is changing really quickly, the only strategy that is guaranteed to fail is not taking any risks!

