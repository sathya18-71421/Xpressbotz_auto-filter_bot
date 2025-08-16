from pyrogam import Client, filters


API_ID = ""
API_HASH = ""
BOT_TOKEN = ""

XpressBotz = Client(
    name="Autofilterbot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


print("Bot was started")

XpressBotz.run()

