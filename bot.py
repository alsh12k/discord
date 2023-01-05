from pyrogram import Client, filters

api_id = 1036626
api_hash = "2f24c61c519fd5cd1da65f87ffa94de6"
bot_token = "5302017916:AAFumbh6bpnqdKg7h-Osgci2wDJ9kD1umuc"

bot = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)
@bot.on_message(filters.command('start'))
def send(bot, msg):
  bot.send_message(msg.chat.id, "Message sent with")
  
bot.run()
