def get_messages() -> dict:
    """Словарь с заготовками сообщений пользователю"""
    messages = {
        'FindUrl': 'Найдена ссылка',
        'NonUrlMessage': 'Не разгляжу ссылку, обычно это `http...`',
        'SuccessfulDownload': 'Успешно скачали видео... Ожидайте.',
        'BadUrl': 'Что-то не так, скачать не получается :(',
        'SuccessfulSend': 'Наслаждайтесь. Отправить отзыв автору https://t.me/anton_pozdnyakov'
    }
    return messages
