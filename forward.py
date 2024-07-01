#test bot hahaha
from pyrogram import Client, filters
from dotenv import load_dotenv, dotenv_values
import os
import asyncio

config = load_dotenv("config.env")

api_id = os.getenv('API_ID', '')
api_hash = os.getenv('API_HASH', '')
bot_token = os.getenv('BOT_TOKEN', '')

bot = Client(
  "dark",
  api_id=api_id,
  api_hash=api_hash,
  bot_token=bot_token,
  )
  
@bot.on_message(filters.command("start"))
async def start_msg(client, msg):
  user_men = msg.from_user.mention
  ST = await msg.reply_text(f"Helo {user_men}")
  await asyncio.sleep(2)
  await ST.delete()

print("Bot started!")
bot.run()