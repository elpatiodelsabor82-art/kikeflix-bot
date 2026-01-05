from pyrogram import Client, filters

# Tus credenciales directas
API_ID = 32394929
API_HASH = "10e6543af1b09ee262f688f94f68ae71"
BOT_TOKEN = "8560755206:AAGzqanMokL-r4gDqehH2p3qWMOwCPrRVIo"

app = Client("kike_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("¡Hola Edgar! Si lees esto, el bot de KikeFlix por fin está funcionando.")

app.run()
