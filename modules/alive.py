from telethon import events
import time

def register(client, OWNER_ID, start_time):
    @client.on(events.NewMessage(pattern=r"\.alive"))
    async def alive(event):
        if event.sender_id != OWNER_ID:
            return
        
        # Hitung uptime
        now = time.time()
        uptime = int(now - start_time)
        hours, rem = divmod(uptime, 3600)
        minutes, seconds = divmod(rem, 60)

        # Format waktu uptime
        uptime_str = f"{hours} jam {minutes} menit {seconds} detik"

        await event.respond(
            "🚨🚨 **Jayjo Cyber Userbot Aktif!** 🚨🚨\n\n"
            "🛰️ **Status** : ✅ Online\n"
            "👑 **Owner**  : Jayjo Cyber\n"
            "⚙️ **Versi**  : 1.0.0\n"
            "💾 **Library**: Telethon\n"
            "🎨 **Theme**  : Cyber Glitchy Vibes\n"
            f"⏳ **Uptime** : {uptime_str}\n\n"
            "⚡️ Powered by Jayjo Cyber Division ⚡️",
            reply_to=event.id
        )
