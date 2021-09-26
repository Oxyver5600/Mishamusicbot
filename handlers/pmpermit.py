from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"🌸𝗧𝗵𝗶𝘀 𝗜𝘀 𝗠𝘂𝘀𝗶𝗰 𝗔𝘀𝘀𝗶𝘀𝘁𝗮𝗻𝗰𝗲 𝗢𝗙 ❰❤🎤𝐌𝐢𝐬𝐡𝐚➳𝐌𝐮𝐬𝐢𝐜➳𝐁𝐨𝐭🎤❤❱❰@Prince_Charles2❱\n🌸𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗱 𝗕𝘆 ❰❤🎤𝐌𝐢𝐬𝐡𝐚➳𝐌𝐮𝐬𝐢𝐜➳𝐁𝐨𝐭🎤❤❱❰@Prince_Charles2❱\n🌸𝗙𝗼𝗿 𝗛𝗲𝗹𝗽 𝐆𝐫𝐨𝐮𝐩 - @Dil_dosti_duniya_dari")
  return                        
