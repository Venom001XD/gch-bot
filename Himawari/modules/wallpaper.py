"""
MIT License

Copyright (c) 2022 Arsh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import requests as r

from random import randint
from telegram import Update, ChatAction
from telegram.ext import CallbackContext, run_async

from Himawari import SUPPORT_CHAT, WALL_API, dispatcher
from Himawari.modules.disable import DisableAbleCommandHandler
from Himawari.modules.helper_funcs.alternate import send_action


@send_action(ChatAction.UPLOAD_PHOTO)
def wall(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    msg = update.effective_message
    args = context.args
    msg_id = update.effective_message.message_id
    bot = context.bot
    query = " ".join(args)
    if not query:
        msg.reply_text("Please enter a query!")
        return
    caption = query
    term = query.replace(" ", "%20")
    json_rep = r.get(
        f"https://wall.alphacoders.com/api2.0/get.php?auth=2455acab48f3a935a8e703e54e26d121&method=search&term={term}"
    ).json()
    if not json_rep.get("success"):
        msg.reply_text(f"An error occurred! Report this @{SUPPORT_CHAT}")
    else:
        wallpapers = json_rep.get("wallpapers")
        if not wallpapers:
            msg.reply_text("No results found! Refine your search.")
            return
        index = randint(0, len(wallpapers) - 1)  # Choose random index
        wallpaper = wallpapers[index]
        wallpaper = wallpaper.get("url_image")
        wallpaper = wallpaper.replace("\\", "")
        bot.send_photo(
            chat_id,
            photo=wallpaper,
            caption="Preview",
            reply_to_message_id=msg_id,
            timeout=60,
        )
        bot.send_document(
            chat_id,
            document=wallpaper,
            filename="wallpaper",
            caption=caption,
            reply_to_message_id=msg_id,
            timeout=60,
        )


WALLPAPER_HANDLER = DisableAbleCommandHandler("wall", wall, run_async=True)
dispatcher.add_handler(WALLPAPER_HANDLER)
