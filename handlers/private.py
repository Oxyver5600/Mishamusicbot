
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**
š š§šµš¶š šš šš±šš®š»š°š² š§š²š¹š²š“šæš®šŗ š ššš¶š° šš¼š \nšŗš„šš» š¢š» š£šæš¶šš®šš² š©š£š¦ š¦š²šæšš²šæ \nš¼šš²š²š¹ šš¶š“šµ š¤šš®š¹š¶šš š ššš¶š° šš» š©š \nā­šš²šš²š¹š¼š½š²š± šš [ā¤šš«š¢š§ššāÆā³šš”šš«š„šš¬ā¤](https://t.me/Prince_Charles2)**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "šš¤ā°š¢šš»š²šæā±šš", url="https://t.me/Prince_Charles2")
                  ],[
                    InlineKeyboardButton(
                        "š®š³ā°š¦šš½š½š¼šæšā±š®š³", url="https://t.me/Prince_Charles2"
                    ),
                    InlineKeyboardButton(
                        "š„°ā°ššæš¼šš½ā±š„°", url="https://t.me/Dil_dosti_duniya_dari"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "šā°šš¼šŗšŗš®š±šā±š", url="https://telegra.ph/Commands-For---Misha-Music-Bot-09-26"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("Royal") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**ā¤š¤šš¢š¬š”šā³šš®š¬š¢šā³ššØš­š¤ā¤ š ššš¶š° šš¼š š¢š»š¹š¶š»š² š”š¼š\nš  @Prince_Charles2 <3**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "š¼š¦šš½š½š¼šæš", url="https://t.me/Dil_dosti_duniya_dari")
                ]
            ]
        )
   )
