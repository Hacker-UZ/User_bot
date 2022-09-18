from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from time import sleep

api_id = 9708508
api_hash = "1e6ca420184a701db1f8a1301df99288"
app = Client("Accaunt", api_id, api_hash)


@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbp = ""  # to be printed
    typing_symbol = "🌀"

    while (tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.05)  # 50ms

            tbp = tbp + text[0]
            text = text[1:]

            msg.edit(tbp)
            sleep(0.05)

        except FloodWait as e:
            sleep(e.x)


app.run()
