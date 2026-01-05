from pyrogram import Client, filters

# Datos directos para no fallar
app = Client(
    "kike_bot",
    api_id=32394929,
    api_hash="10e6543af1b09ee262f688f94f68ae71",
    bot_token="8560755206:AAGzqanMokL-r4gDqehH2p3qWMOwCPrRVIo"
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("¡POR FIN! El bot está vivo y funcionando, Edgar.")

print("Bot encendido...")
app.run()
