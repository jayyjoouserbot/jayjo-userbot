from telethon import events
from telethon.tl.types import UpdateUser
import json
import datetime
import os

def register(client, OWNER_ID):
    data_file = "usn_data.json"
    if not os.path.exists(data_file):
        with open(data_file, "w") as f:
            json.dump({}, f)

    @client.on(events.Raw())
    async def track_user_update(event):
        if isinstance(event, UpdateUser):
            user_id = str(event.user_id)

            try:
                user = await client.get_entity(user_id)
                username = f"@{user.username}" if user.username else "(empty)"
                name = f"{user.first_name or ''} {user.last_name or ''}".strip()

                waktu = datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")

                with open(data_file, "r") as f:
                    data = json.load(f)

                if user_id not in data:
                    data[user_id] = {
                        "names": [],
                        "usernames": []
                    }

                if name and name not in data[user_id]["names"]:
                    data[user_id]["names"].append(f"[{waktu}] {name}")

                if username and username not in data[user_id]["usernames"]:
                    data[user_id]["usernames"].append(f"[{waktu}] {username}")

                with open(data_file, "w") as f:
                    json.dump(data, f, indent=2)

            except Exception as e:
                print(f"Error tracking user: {e}")

    # Command buat cek history user
    @client.on(events.NewMessage(pattern=r"\.history(?: (.+))?"))
    async def show_history(event):
        if event.sender_id != OWNER_ID:
            return

        args = event.pattern_match.group(1)
        if not args:
            await event.reply("Format: `.history <user_id>`")
            return

        user_id = args.strip()

        with open(data_file, "r") as f:
            data = json.load(f)

        if user_id not in data:
            await event.reply("⚠️ User belum ada riwayat.")
            return

        history = data[user_id]
        names = "\n".join(f"{i+1}. {v}" for i, v in enumerate(history["names"]))
        usernames = "\n".join(f"{i+1}. {v}" for i, v in enumerate(history["usernames"]))

        result = f"📒 **History for `{user_id}`**\n\n**Names**\n{names or '-'}\n\n**Usernames**\n{usernames or '-'}"

        await event.reply(result)
