import os
import uvloop
import asyncio

from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from messages import get_messages
from yt_dlp_utils import get_file


load_dotenv()
uvloop.install()
APP = Client(
    name=os.environ['APP_NAME'],
    api_id=os.environ['API_ID'],
    api_hash=os.environ['API_HASH'],
    bot_token=os.environ['BOT_TOKEN']
)
MESSAGES = get_messages()


@APP.on_message(filters.text & filters.private)
async def process_message(client, message):
    """Flow обработки входящих сообщений"""
    result_reply = MESSAGES['NonUrlMessage']

    if message.text.startswith('http'):
        find_url_message = await message.reply(MESSAGES['FindUrl'])

        url = message.text
        download_info = get_file(url=url)
        result_reply = MESSAGES['BadUrl']

        if isinstance(download_info, dict):
            download_info = get_file(url=url, download=True)
            filepath = download_info['requested_downloads'][0]['filepath']
            successful_message = await message.reply(MESSAGES['SuccessfulDownload'])
            progress_message = await message.reply(MESSAGES['Preparation'])

            try:  # avoid Flood Waits
                await message.reply_document(
                    document=filepath,
                    progress=progress,
                    progress_args=(progress_message,)
                )
            except FloodWait as err:
                await asyncio.sleep(err.value)

            os.remove(filepath)

            for bot_message in (find_url_message, successful_message, progress_message):
                await bot_message.delete()

            result_reply = MESSAGES['SuccessfulSend']

    await message.reply(result_reply)


async def progress(current, total, progress_message):
    await progress_message.edit_text(render_progressbar(total, current))


def render_progressbar(total, current, prefix='', suffix='', length=30, fill='█', zfill='░'):
    """Прогресс-бар скачивания файла"""
    current = min(total, current)
    percent = "{0:.1f}"
    percent = percent.format(100 * (current / float(total)))
    filled_length = int(length * current // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    progressbar = '{0} {1}| {2}% {3}'.format(prefix, pbar, percent, suffix)
    return progressbar


if __name__ == '__main__':

    APP.run()
