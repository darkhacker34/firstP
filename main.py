
from pyrogram import Client, filters

AI="1917094"
AH="43dbeb43f27f99752b44db7493bf38ad"
BT="6941473830:AAFlRLUUhjPIfrYWOeBjVrxMbygS0VX4N7w"

NIK = Client (
  name="dark",
  api_id=AI,
  api_hash=AH,
  bot_token=BT,
  
)

print("Bot started!")

NIK.run()
