from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_ID = 32394929
API_HASH = "10e6543af1b09ee262f688f94f68ae71"
BOT_TOKEN = "8560755206:AAGzqanMokL-r4gDqehH2p3qWMOwCPrRVIo"
BIN_CHANNEL = -1003596503089 

app = Client("kike_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("**¡KikeFlix Activo!** 🍿\n\nEnvíame un video o archivo para generar su link de descarga.")

@app.on_message(filters.private & (filters.document | filters.video))
async def gen_link(client, message):
    forwarded = await message.forward(BIN_CHANNEL)
    file_id = forwarded.id
    # Link directo al mensaje en el canal
    share_link = f"https://t.me/c/3596503089/{file_id}"
    
    await message.reply_text(
        "**✅ Link generado:**",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🎥 Ver Película", url=share_link)]])
    )

app.run()
