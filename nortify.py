import time
from plyer import notification


def send_notification(title, message, wait_time=7):
    notification.notify(
        title=title,
        message=message,
        app_name="TODO",
        app_icon="icon.ico",
        timeout=2
    )
    time.sleep(wait_time)
