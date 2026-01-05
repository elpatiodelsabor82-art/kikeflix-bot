from pyrogram import Client, filters
app = Client("kike", api_id=32394929, api_hash="10e6543af1b09ee262f688f94f68ae71", bot_token="8560755206:AAGzqanMokL-r4gDqehH2p3qWMOwCPrRVIo")
@app.on_message(filters.all)
async def echo(client, message):
    await message.reply_text("¡Aquí estoy! El bot está vivo.")
app.run()
