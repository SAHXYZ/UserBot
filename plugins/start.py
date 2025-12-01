from pyrogram import Client, filters

# This function will be called automatically by safe_init()
def init_start(bot: Client):
    
    @bot.on_message(filters.command("start", prefixes=".") & filters.me)
    async def start_handler(_, message):
        await message.reply_text("✅ **ValerieBot is Started Successfully**\n\n— by **SAH**")
