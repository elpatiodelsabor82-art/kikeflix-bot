import os
from pyrogram import Client, filters
from str_to_file import StreamProcess # Esta librería hace el puente

# CONFIGURACIÓN (Usa tus datos)
API_ID = "TU_API_ID" # Ahora te digo cómo sacar estos dos
API_HASH = "TU_API_HASH"
BOT_TOKEN = "8560755206:AAGzqanMokL-r4gDqehH2p3qWMOwCPrRVIo"

app = Client("KikeFlixBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.video | filters.document)
async def gen_link(client, message):
    # Esto genera el link que va directo a tu Netlify
    base_url = "https://TU-APP-DE-STREAMING.koyeb.app" 
    file_id = message.video.file_id if message.video else message.document.file_id
    direct_link = f"{base_url}/{file_id}"
    
    # Tu link de KikeFlix ya armado
    kikeflix_url = f"https://dashing-biscotti-20d2a8.netlify.app/?url={direct_link}"
    
    await message.reply_text(f"✅ **¡Listo Edgar! Aquí tienes tu película:**\n\n`{kikeflix_url}`")

app.run()
