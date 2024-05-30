from pyrogram import Client, filters

import os
import shutil

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

@Client.on_message(filters.command("delmyfolder"))
async def megadl(bot, update):
    if update.from_user.id == int(Config.OWNER_ID):
        allowed=1
    elif update.from_user.id in Config.AUTH_USERS:
        allowed=1
    else:
        allowed=0
    if allowed == 1:
        admin_downloads_directory = Config.ADMIN_LOCATION + "/" + str(update.from_user.id)
        if os.path.isdir(admin_downloads_directory):
            try:
                shutil.rmtree(admin_downloads_directory)
                await bot.send_message(
                    chat_id=update.chat.id,
                    text=f"""<b>The download directory for admins and auth users has been deleted successfully! ✅</b>\n\nNow your server will be fresh as new! 😇\n\n<b>What this command does :-</b> Since owner and auth users support multitasking their downloads folder will not get deleted automatically!. So If you want to clean up the server storage hit that command and delete your download folder afterr all of your current downloads got uploaded. If you are on heroku free dynos this doesn't really matter but if you are on a vps please remember to do it once in a while!\n\n<b>Note :- Do not send this command while links are being downloaded and uploaded!</b>""",
                    reply_to_message_id=update.id
                )
            except:
                await bot.send_message(
                    chat_id=update.chat.id,
                    text=f"""Sorry🥺 Some error occured while trying to delete your folder! 😕""",
                    reply_to_message_id=update.id
                )
        else:
            await bot.send_message(
                chat_id=update.chat.id,
                text=f"""Your download directory doesn't exist! Download some files first and after all the downloads are completed and has been uploaded to telegram send /delmyfolder in order to delete owner's and auth user's file from the server and to make the server fresh!""",
                reply_to_message_id=update.id
            )
    else:
        await bot.send_message(
            chat_id=update.chat.id,
            text=f"""This command is only for the owner and auth users of this bot!""",
            reply_to_message_id=update.id
        )
