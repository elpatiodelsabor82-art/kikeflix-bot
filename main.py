from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Configuración
API_ID = 32394929
API_HASH = "10e6543af1b09ee262f688f94f68ae71"
BOT_TOKEN = "8560755206:AAGzqanMokL-r4gDqehH2p3qWMOwCPrRVIo"
BIN_CHANNEL = -1003596503089 # Tu canal de almacenamiento

app = Client("kike_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "**¡Bienvenido a KikeFlix!**\n\nEnvíame un archivo o link de mi canal para generar tu enlace de descarga."
    )

@app.on_message(filters.private & (filters.document | filters.video))
async def gen_link(client, message):
    # Reenvía el archivo al canal de almacenamiento para asegurar el link
    forwarded = await message.forward(BIN_CHANNEL)
    file_id = forwarded.id
    
    # Genera el link (esto asumiendo que usas un sistema de visualización web después)
    share_link = f"https://t.me/share/url?url=https://t.me/c/{str(BIN_CHANNEL)[4:]}/{file_id}"
    
    await message.reply_text(
        "**✅ Archivo procesado correctamente**",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🎥 Ver / Descargar", url=share_link)]
        ])
    )

print("Bot de KikeFlix encendido...")
app.run()
