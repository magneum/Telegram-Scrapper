from Liters import *
from HUB import ALL_MODULES

for module_name in ALL_MODULES:
    imported_module = importlib.import_module("HUB." + module_name)
    if not hasattr(imported_module, "__HYAPI__"):
        imported_module.__HYAPI__ = imported_module.__name__
    if imported_module.__HYAPI__.lower() not in IMPORTED:
        IMPORTED[imported_module.__HYAPI__.lower()] = imported_module

print("🎀==================================================🎀" + platform.upper() + "🎀==================================================🎀")
HYPEEED.info("—✨••÷[  HVåþïßð†⚔️  ]÷••✨—")
HYPEEED.info("⚔️ LOADED     |>    " + str(ALL_MODULES).upper())
HYPEEED.info("🎀==================================================🎀")
updater.start_polling(
timeout=15,
read_latency=4,
drop_pending_updates=True)
if platform.startswith("lin"):
    os.system("clear")
elif platform.startswith("win"):
    os.system("cls")
else:
    pass 
HYPEEED.info("⚔️ LOADED     |>    " + str(ALL_MODULES).upper())  
HYPEEED.info("")
HYPEEED.info("🎀==================================================🎀")
HYPEEED.info("—✨••÷[  HVåþïßð†⚔️  ]÷••✨— 🦞DΣV MΣПƬIӨП:\n💻 @Krakinz | @KrakinzBot ")
updater.idle()
if platform.startswith("lin"):
    os.system("clear")
elif platform.startswith("win"):
    os.system("cls")
else:
    pass 