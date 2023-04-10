import os
import yt_dlp
from yt_dlp import DownloadError


def get_file(
        url: str,
        options: dict = None,
        download: bool = False
):
    """Скачиваем видео по ссылке"""
    if not options:  # Возможно форматы прийдется вынести в переменную
        options = {
            'format': 'b',
            'format-sort': 'filesize~50M',
            'outtmpl': '%(title)s.%(ext)s',
            'trim_file_name': 49,
            'geo_bypass': True,
            'cookiefile': 'cookies.txt'
        }

    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            download_info = ydl.extract_info(url=url, download=download)
            return download_info
    except DownloadError as err:
        return err
