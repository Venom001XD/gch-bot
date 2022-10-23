#ɪғ ʏᴏᴜ ғᴏᴜɴᴅ ɪɴ ᴀɴʏ ᴇʀʀᴏʀs ᴛʜᴀɴ ᴘʟᴢ ᴄᴏɴᴛᴀᴄᴛ @SIXTH_H0KAGE
#sᴜᴘᴘᴏʀᴛ :- @kakashi_bots_support
#ᴜᴘᴅᴀᴛᴇs :- @kakashi_bots_updates
#ɴᴇᴛᴡᴏʀᴋ :- @Otaku_Binge

import requests
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Himawari import pbot


@pbot.on_message(filters.command("imdb"))
async def imdb(client, message):
    if len(message.command) < 2:
        return await message.reply_text("Give me some Movie Name\n\nEx. /imdb Kgf 2")
    text = (
        message.text.split(None, 1)[1]
        if len(message.command) < 3
        else message.text.split(None, 1)[1].replace(" ", "%20")
    )
    url = requests.get(f"https://api.safone.tech/tmdb?query={text}").json()["results"][
        0
    ]
    poster = url["poster"]
    imdb_link = url["imdbLink"]
    title = url["title"]
    rating = url["rating"]
    releasedate = url["releaseDate"]
    description = url["overview"]
    popularity = url["popularity"]
    runtime = url["runtime"]
    status = url["status"]
    await client.send_photo(
        message.chat.id,
        poster,
        caption=f"""

🏷️Title = {title}

📍Rating = {rating}
🔎Release-Date = {releasedate}
♦️Popularity = {popularity}
♦️Runtime = {runtime}
♦️Status = {status}

♦️Description = {description}
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="🎟️IMDB",
                        url=imdb_link,
                    ),
                ],
            ],
        ),
    )


__help__ = """
 ⦿ /imdb <Movie name>*:* Get full info about a movie from [imdb.com](https://m.imdb.com)
"""

__mod_name__ = "𝙸ᴍᴅʙ"
