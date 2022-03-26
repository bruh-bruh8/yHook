import json
import time
import requests
import pyfiglet
from os import system
ver = "[α-v1]"
system("title " + f"λHook {ver}")
banner = pyfiglet.figlet_format("yHook")
pre = "[λHook]"
print(banner)
webhook = input("Enter webhook URL: ")
print("=============================================================================================================\n")
print("[1] Webhook Spammer \n")
print("[2] Webhook Deleter\n")
print("[3] Get Info (Bad)\n")
print("[4] Coming Soon™\n")
print("=============================================================================================================\n")
selection = input("Choice: ")


def spammer(wh):
    msg = input("Spam Message: ")
    if msg == "":
        msg = "@everyone"
    while True:
        try:
            data = requests.post(webhook, json={'content': msg})
            print(f"{pre} Sent message: \"{msg}\" ")
        except:
            print(f"{pre} Bad URL!")
            time.sleep(5)
            exit(0)


def delete(wh):
    try:
        system("curl -X -S DELETE " + wh)
        print(f"{pre} Successfully deleted webhook")
        # bad way to do this but oh well!
    except:
        print(f"{pre} An error occurred when attempting to delete the webhook!")
        exit(0)


def getinfo(wh):
    try:
        x = requests.get(wh).json()
        time.sleep(3)
    except:
        print(f"{pre} An error occurred when attempting to get info on the webhook!")
        time.sleep(1.5)
        exit(0)


def cs():
    print("no")
    time.sleep(1.5)
    exit(420)


if selection == "1":
    spammer(webhook)
elif selection == "2":
    delete(webhook)
elif selection == "3":
    getinfo(webhook)
elif selection == "4":
    cs()
else:
    cs()
