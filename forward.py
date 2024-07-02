#test bot hahaha
from pyrogram import Client, filters
from dotenv import load_dotenv, dotenv_values
import os, environ
import asyncio
from webcode import bot_run
from aiohttp import web as webserver

config = load_dotenv("config.env")

api_id = os.getenv('API_ID', '')
api_hash = os.getenv('API_HASH', '')
bot_token = os.getenv('BOT_TOKEN', '')
PORT_CODE = os.getenv("PORT", "8080")

bot = Client(
  "dark",
  api_id=api_id,
  api_hash=api_hash,
  bot_token=bot_token,
  )
  
@bot.on_message(filters.command("start") & filters.private)
async def start_msg(client, msg):
  user_men = msg.from_user.mention
  await msg.reply_text(f"Helo {user_men}")
  
@bot.on_message(filters.channel & filters.media & filters.text & filters.photo & filters.incoming)
async def incoming(client, msg):
  await msg.forward("-1001613693052")

client = webserver.AppRunner(bot_run())
client.setup()
bind_address = "0.0.0.0"
webserver.TCPSite(client, bind_address, PORT_CODE).start()

print("Bot started!")
bot.run()
