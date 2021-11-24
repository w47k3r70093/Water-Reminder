import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(title = "DRINK WATER PLEASE!", message = "Please Drink Water", timeout = 5)
        time.sleep(60*15)
