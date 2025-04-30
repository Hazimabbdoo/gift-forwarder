import os
from telethon import TelegramClient, events

# جلب البيانات من المتغيرات البيئية
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
source_channel = os.getenv("SOURCE_CHANNEL")
target_channel = os.getenv("TARGET_CHANNEL")

client = TelegramClient('gift_forwarder', api_id, api_hash, connection_retries=None, timeout=10)

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    message = event.message
    text = message.message or ""

    prizes_line = ""
    for line in text.splitlines():
        if "Prizes" in line:
            prizes_line = line
            break

    hashtag_count = prizes_line.count("#")
    print(f"Detected {hashtag_count} NFTs in message.")

    if hashtag_count >= 5:
        await event.forward_to(target_channel)
        print("Message forwarded!")

client.start()
print("Bot is running and watching for giveaways...")
client.run_until_disconnected()