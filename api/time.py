from datetime import datetime

def handle_time():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return "Current server time is: {current_time}"