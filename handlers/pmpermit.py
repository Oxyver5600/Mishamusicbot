from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"šøš§šµš¶š šš š ššš¶š° šššš¶ššš®š»š°š² š¢š ā°ā¤š¤šš¢š¬š”šā³šš®š¬š¢šā³ššØš­š¤ā¤ā±ā°@Prince_Charles2ā±\nšøšš²šš²š¹š¼š½š²š± šš ā°ā¤š¤šš¢š¬š”šā³šš®š¬š¢šā³ššØš­š¤ā¤ā±ā°@Prince_Charles2ā±\nšøšš¼šæ šš²š¹š½ šš«šØš®š© - @Dil_dosti_duniya_dari")
  return                        
