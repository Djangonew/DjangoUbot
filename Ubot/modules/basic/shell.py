"""
Credit:
Code By:
- Kynan (https://github.com/naya1504)
- Amang (https://github.com/amanqs)
"""

from subprocess import Popen, PIPE, TimeoutExpired
import os
from time import perf_counter

from pyrogram import Client, filters
from pyrogram.types import Message

from . import *


@Client.on_message(filters.command(["sh"], cmds) & filters.me)
async def shell(_, message: Message):
    if message.from_user.id not in ADMINS:
        return await message.edit("**Lu bukan ADMINS**")
  
    if len(message.command) < 2:
        return await message.edit("<b>Specify the command in message text</b>")
    cmd_text = message.text.split(maxsplit=1)[1]
    cmd_obj = Popen(
        cmd_text,
        shell=True,
        stdout=PIPE,
        stderr=PIPE,
        text=True,
    )

    char = "#" if os.getuid() == 0 else "$"
    text = f"<b>{char}</b> <code>{cmd_text}</code>\n\n"

    await message.edit(text + "<b>Running...</b>")
    try:
        start_time = perf_counter()
        stdout, stderr = cmd_obj.communicate(timeout=1800)
    except TimeoutExpired:
        text += "<b>Timeout expired (60 seconds)</b>"
    else:
        stop_time = perf_counter()
        if stdout:
            text += f"<b>Output:</b>\n<code>{stdout}</code>\n\n"
        if stderr:
            text += f"<b>Error:</b>\n<code>{stderr}</code>\n\n"
        text += f"<b>Completed in {round(stop_time - start_time, 5)} seconds with code {cmd_obj.returncode}</b>"
    await message.edit(text)
    cmd_obj.kill()
