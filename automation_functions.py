import os
import webbrowser
import psutil

def open_chrome():
    webbrowser.open("https://www.google.com")

def open_calculator():
    os.system("calc" if os.name == "nt" else "gnome-calculator")

def get_cpu_usage():
    return f"Current CPU Usage: {psutil.cpu_percent()}%"

def get_ram_usage():
    return f"Current RAM Usage: {psutil.virtual_memory().percent}%"
