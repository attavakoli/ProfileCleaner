#Coder: @Salazar
#chnl : https://t.me/PiniGerTeam & https://t.me/GIOUTiN
from pyrogram import Client
import os
import sys
###########################
api_id = 739690  #api_id ک برای دیل نشدن اکانتتون باید جایگذاری کنید
api_hash = "427ff8e03bccfd1182961765d9c1bc6b" #api_hash ک برای دیل نشدن اکانتتون باید جایگذاری کنید
sudo = 744309935 #ایدی عددی سازنده ربات
app = Client("clean",api_id, api_hash)
@app.on_message()
def cmd(c,message):
    if message.from_user.id == sudo:
        try:
            if message.text == 'pict':
                my = app.get_me()
                count = app.get_profile_photos_count(my.id)
                message.reply_text("تعداد پروفایل های اکانت : [ {} ]".format(count))
        except Exception as e:
            print(e)


        if message.text == 'reload':
            message.reply_text("~ Done!")
            python = sys.executable
            os.execl(python, python, *sys.argv)

        try:
            if message.text == 'delpic':
                my = app.get_me()
                photos = app.get_profile_photos(my.id)
                app.delete_profile_photos([p.file_id for p in photos[0:]])
                message.reply_text("پروفایل های اکانت با موفقیت پاکسازی شد!")
        except Exception as e:
            print(e)


app.run()