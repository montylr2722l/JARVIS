from datetime import datetime

LOG_FILE = "logs/commands.log"

def log_command(command):

    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as file:
        file.write(f"[{time}] {command}\n")