# File: UserBot/main.py

from pyrogram import Client
import importlib
import traceback
from config import API_ID, API_HASH, STRING_SESSION
from database.mongo import client  # ensure MongoDB loads first

bot = Client(
    name="UserBot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION,
    workers=1
)



def safe_init(module_name: str):
    try:
        mod = importlib.import_module(f"plugins.{module_name}")
        init_fn = getattr(mod, f"init_{module_name}", None)

        if callable(init_fn):
            init_fn(bot)
            print(f"[loaded] plugins.{module_name}")
        else:
            print(f"[skipped] plugins.{module_name}")

    except Exception as e:
        print(f"[ERROR] {module_name}: {e}")
        traceback.print_exc()


required_modules = [
   "hi",
  "start"
]

optional_modules = []


if __name__ == "__main__":
    print("Initializing UserBot...")

    for module in required_modules:
        safe_init(module)

    for module in optional_modules:
        safe_init(module)

    print("✔ Valeire UserBot is running Successfully!")
    bot.run()
