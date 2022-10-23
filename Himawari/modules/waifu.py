#ɪғ ʏᴏᴜ ғᴏᴜɴᴅ ɪɴ ᴀɴʏ ᴇʀʀᴏʀs ᴛʜᴀɴ ᴘʟᴢ ᴄᴏɴᴛᴀᴄᴛ @SIXTH_H0KAGE
#sᴜᴘᴘᴏʀᴛ :- @kakashi_bots_support
#ᴜᴘᴅᴀᴛᴇs :- @kakashi_bots_updates
#ɴᴇᴛᴡᴏʀᴋ :- @Otaku_Binge

import requests
from telegram import ParseMode

from Himawari.events import register as bot


@bot(pattern="[/!]waifu")
async def ok(event):
    url = "https://api.waifu.pics/sfw/waifu"
    r = requests.get(url)
    e = r.json()
    await event.reply(
        "**A waifu appeared!** \nAdd them to your harem by sending /protecc character name",
        parse_mode=ParseMode.MARKDOWN,
        file=e["url"])


@bot(pattern="[/!]wprotecc")
async def ok(event):
    await event.reply(
        "OwO you protecc'd A Waifu This waifu has been added to your harem.")


@bot(pattern="[/!]wharem")
async def ok(event):
    await event.reply("You haven't protecc'd any waifu yet...")
