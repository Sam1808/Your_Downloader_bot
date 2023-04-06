def get_messages() -> dict:
    """Словарь с заготовками сообщений пользователю"""
    messages = {
        'FindUrl': 'Найдена ссылка, пытаемся извлечь видео...',
        'NonUrlMessage': 'Не разгляжу ссылку, обычно это `http...`',
        'SuccessfulDownload': 'Успешно скачали видео... Ожидайте загрузки.',
        'BadUrl': 'Что-то не так, скачать не получается :(',
        'SuccessfulSend': 'Наслаждайтесь. Отправить отзыв автору https://t.me/anton_pozdnyakov',
        'Preparation': 'Подготовка'
    }
    return messages
