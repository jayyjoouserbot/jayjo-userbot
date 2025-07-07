from telethon import TelegramClient, events
from dotenv import load_dotenv
from modules import alive
from modules import usn_tracker
import os
import time
start_time = time.time()

# Load .env
load_dotenv(dotenv_path="config.env")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
OWNER_ID = int(os.getenv("OWNER_ID"))

# Inisialisasi client
client = TelegramClient("JAYJO_USERBOT", API_ID, API_HASH)

# Import module dan daftarin client
from modules import alive
alive.register(client, OWNER_ID, start_time)
usn_tracker.register(client, OWNER_ID)

# Run
with client:
    print("Jayjo Cyber Userbot Aktif")
    client.run_until_disconnected()
