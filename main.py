from Liters import *
from HUB import ALL_MODULES

for module_name in ALL_MODULES:
    imported_module = importlib.import_module("HUB." + module_name)
    if not hasattr(imported_module, "__HYAPI__"):
        imported_module.__HYAPI__ = imported_module.__name__
    if imported_module.__HYAPI__.lower() not in IMPORTED:
        IMPORTED[imported_module.__HYAPI__.lower()] = imported_module


HYPEEED.info("🔥==================================================🔥")
HYPEEED.info("—✨••÷[  HVApiBot⚔️  ]÷••✨—")
HYPEEED.info("⚔️ LOADED" + str(ALL_MODULES).upper())
HYPEEED.info("🔥==================================================🔥")
updater.start_polling(
timeout=15,
read_latency=4,
drop_pending_updates=True)   
HYPEEED.info("")
HYPEEED.info("🔥==================================================🔥")
HYPEEED.info("—✨••÷[  HVApiBot⚔️  ]÷••✨—")
updater.idle()
updater.stop()