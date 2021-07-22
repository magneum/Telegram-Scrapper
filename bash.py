from Liters import *
from FONK import *
from sys import platform
print(platform)
if HYPE_BOT is not None and HYPE_BOT_NAME is not None and platform.startswith("lin"):
    os.system("pip install -U -r HVapiBot.txt")
    os.system("clear")
    os.system("python -m HVapiBot")
    os.system("clear")
elif HYPE_BOT is not None and HYPE_BOT_NAME is not None and platform.startswith("win"):
    os.system("pip install -U -r HVapiBot.txt")
    os.system("cls")
    os.system("python -m HVapiBot")
    os.system("cls")
else:
    print("Please verify your credentials in configuration path")
    sys.exit()