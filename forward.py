from dotenv import load_dotenv, dotenv_values 
from pyrogram import Client, filters
import os
import asyncio

load_dotenv('config.env', override=True)

api_id = os.environ.get('API_HASH', '')
api_hash = os.environ.get('API_ID', '')
bot_token = os.environ.get('BOT_TOKEN', '')

NIK = Client (
  name="dark",
  api_id=api_id,
  api_hash=api_hash,
  bot_token=bot_token,
  
)
@NIK.on_message(filters.command("start"))
async def start_msg(client, msg):
  user_men = msg.from_user.mention
  await msg.reply_text(f"Helo {user_men}")
  await asyncio.sleep(2)
  await msg.delete()

print("Bot started!")

NIK.run()
