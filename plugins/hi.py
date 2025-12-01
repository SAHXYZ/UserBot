from pyrogram import Client, filters

hi_art = (
    "🌺✨           ✨🌺    🌺✨\n"
    "🌺✨           ✨🌺    🌺✨\n"
    "🌺✨✨✨✨✨🌺    🌺✨\n"
    "🌺✨           ✨🌺    🌺✨\n"
    "🌺✨           ✨🌺    🌺✨"
)

def init_hi(bot: Client):

    @bot.on_message(filters.command("hi", prefixes=[".", "/"]) & filters.me)
    async def hi_handler(_, message):
        await message.reply_text(f"**{hi_art}**")
