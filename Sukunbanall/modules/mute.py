from Sukunbanall import app,BOT_ID,SUDO
from pyrogram import filters
from pyrogram.types import ChatPermissions


@app.on_message(filters.command("muteall") & filters.user(SUDO))
async def mute_all(_,msg):
    chat_id=msg.chat.id    
    bot=await app.get_chat_member(chat_id,BOT_ID)
    bot_permission=bot.privileges.can_restrict_members==True    
    if bot_permission:
        async for member in app.get_chat_members(chat_id):       
            try:
                    await app.restrict_chat_member(chat_id, member.user.id,ChatPermissions(can_send_messages=False))
                    await msg.reply_text(f"ᴍᴜᴛɪɴɢ/ᴀʙ ᴅᴇᴋʜ ʙsᴅᴋ ᴋᴀɪsᴇ ɴᴀɴɢᴀ ᴋᴀʀᴋᴇ ɢᴀɴᴅ ᴍᴀʀᴛᴀ ʜᴜ ʙᴀᴍʙᴏᴏ ʟᴀᴀʏᴀ ʜᴜ ᴍɪʀᴄʜɪ ʟᴀɢᴀ ᴋᴇ ɢʜᴜsᴀ ᴅᴜɴɢᴀ {member.user.mention} ᴡᴀʟᴏ ᴋᴇ ")
                                        
            except Exception:
                pass
    else:
        await msg.reply_text("ᴀʙᴇ ᴛᴜᴛɪʏᴇ ʙsᴅᴋ ʙᴀɴ ʀɪɢʜᴛs ᴋᴀʜᴀ ʜ ʙᴇ ʏᴀ ᴛᴏʜ ᴛᴜ sᴜᴅᴏ ᴜsᴇʀ ᴍᴇ ɴʜɪ ʜᴏɢᴀ ᴊᴏ ᴜɴɢʟɪ ᴋᴀʀ ʀʜᴀ ʜ")  
                                         
    
