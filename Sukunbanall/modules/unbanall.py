from Sukunbanall import app,BOT_ID,SUDO
from pyrogram import filters,enums


@app.on_message(filters.command("unbanall") & filters.user(SUDO))
async def unban_all(_,msg):
    chat_id=msg.chat.id   
    x = 0
    bot=await app.get_chat_member(chat_id,BOT_ID)
    bot_permission=bot.privileges.can_restrict_members==True 
    if bot_permission:
        banned_users = []
        async for m in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.BANNED):
            banned_users.append(m.user.id)       
            try:
                    await app.unban_chat_member(chat_id,banned_users[x])
                    await msg.reply_text(f"ᴜɴʙᴀɴɪɴɢ/ʀᴜᴋ ʙsᴅᴋ ɪɴᴋᴇ ɢᴀɴᴅ {m.user.mention} ᴡᴀʟᴏ ᴋᴇ ")
                    x += 1
                                        
            except Exception:
                pass
    else:
        await msg.reply_text("ᴀʙᴇ ᴛᴜᴛɪʏᴇ ʙsᴅᴋ ʙᴀɴ ʀɪɢʜᴛs ᴋᴀʜᴀ ʜ ʙᴇ ʏᴀ ᴛᴏʜ ᴛᴜ sᴜᴅᴏ ᴜsᴇʀ ᴍᴇ ɴʜɪ ʜᴏɢᴀ ᴊᴏ ᴜɴɢʟɪ ᴋᴀʀ ʀʜᴀ ʜ")
