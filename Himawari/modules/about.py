#ɪғ ʏᴏᴜ ғᴏᴜɴᴅ ɪɴ ᴀɴʏ ᴇʀʀᴏʀs ᴛʜᴀɴ ᴘʟᴢ ᴄᴏɴᴛᴀᴄᴛ @SIXTH_H0KAGE
#sᴜᴘᴘᴏʀᴛ :- @kakashi_bots_support
#ᴜᴘᴅᴀᴛᴇs :- @kakashi_bots_updates
#ɴᴇᴛᴡᴏʀᴋ :- @Otaku_Binge

from Himawari import dispatcher
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ParseMode

from telegram.ext import (
    CallbackContext,
    CommandHandler,
)

PHOTO = "https://telegra.ph/file/04c735f9bfac9aba70edd.jpg"

about_name = "makima info"

if about_name == "makima info":
    def ABOUT(update: Update, context: CallbackContext):

        TEXT = f"""
⦿ ʜᴀʏɪ ʜᴀʏɪ !!,
ɪ'ᴍ *ᴘᴏᴡᴇʀ* ᴀɴ ᴀɴɪᴍᴇ ᴄʜᴀʀᴀᴄᴛᴇʀ ғʀᴏᴍ ᴄʜᴀɪɴsᴀᴡ ᴍᴀɴ.
ᴍᴀᴅᴇ ᴡɪᴛʜ ᴛʜᴇ ᴜɴɪᴛʏ ᴏғ ᴍᴀɴʏ [ɴᴇᴛᴡᴏʀᴋs](https://t.me/PowerSupportGroup).

⦿ ʜᴍᴍ ɪɴᴛᴇʀᴇsᴛᴇᴅ ɪɴ ᴍʏ ʀᴇᴘᴏ? sᴏʀʀʏ sᴇᴍᴘᴀɪ ʙᴜᴛ ᴍʏ ʀᴇᴘᴏ ɪs ᴘʀɪᴠᴀᴛᴇ sᴏ ʏᴏᴜ ᴄᴀɴ'ᴛ ᴅᴇᴘʟᴏʏ ᴍᴇ ᴀɴᴅ ᴍᴀᴋᴇ ᴍᴇ ʏᴏᴜʀs.

⦿ ʙᴜᴛ ʜᴇʏ ɪ ʜᴀᴠᴇ ᴀ ɢᴏᴏᴅ ɴᴇᴡs ғᴏʀ ʏᴏᴜ.ʏᴏᴜ ᴄᴀɴ ɢᴇᴛ ᴍʏ ʀᴇᴘᴏ.
ᴀsᴋ ᴀᴛ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ.
"""

        update.effective_message.reply_photo(
            PHOTO, caption= TEXT,
            parse_mode=ParseMode.MARKDOWN,

                reply_markup=InlineKeyboardMarkup(
                [                    
                    [
                    InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url="https://t.me/PowerSupportGroup"),
                    InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇs", url="https://t.me/PowerBotUpdates")
                    ],
                ]
            ),
            disable_web_page_preview=True              
        )
  

    ABOUT_handler = CommandHandler(("about","repo"), ABOUT)
    dispatcher.add_handler(ABOUT_handler)

    __help__ = """
    ──「POWER INFO & HISTORY」──                         
    
    ❂ /about / /repo: Get information about DABI or if interested in repo!!"""
    
    __mod_name__ = "𝙰ʙᴏᴜᴛ"
