# Telegram-бот для комплиментов фотографиям

Этот скрипт Python представляет собой простого Telegram-бота, который реагирует на отправленные пользователем фотографии и отправляет в ответ комплимент, выбранный случайным образом.

## Описание

Бот использует библиотеку `pyTelegramBotAPI` (telebot) для взаимодействия с Telegram API. При получении фотографии бот выбирает случайный комплимент из списка и отправляет его пользователю.

## Функциональность

*   Обрабатывает команду `/start`: отправляет приветственное сообщение с просьбой прислать фотографию.
*   Обрабатывает фотографии: отправляет случайный комплимент в ответ на присланную фотографию.

## Установка

1.  **Установите Python:**  Если у вас еще не установлен Python, скачайте и установите его с официального сайта: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2.  **Установите библиотеку `pyTelegramBotAPI` (telebot):**

    ```bash
    pip install pyTelegramBotAPI
    ```

3.  **Получите токен API у BotFather:**

    *   В Telegram найдите бота @BotFather.
    *   Начните с ним разговор и введите команду `/newbot`.
    *   Следуйте инструкциям BotFather, чтобы создать нового бота.
    *   BotFather предоставит вам токен API для вашего бота.  Сохраните этот токен.

## Использование

1.  **Клонируйте репозиторий (если он есть) или создайте новый файл `main.py`:**

    ```bash
    # Если есть репозиторий (например, на GitHub)
    git clone <URL_репозитория>
    cd <название_директории>

    # Если нет репозитория, создайте файл main.py
    touch main.py
    ```

2.  **Скопируйте код скрипта в файл `main.py`:**

    ```python
    import telebot
    import random
    import time

    bot = telebot.TeleBot('Ваш API') #Вставьте сюда ваш API ключ полученный в @BotFather 

    # Команда /start

    @bot.message_handler(commands=['start'])
    def main(message):
        bot.send_message(message.chat.id, 'Привет, скинь мне любую фотку')

    # Фото и компилмент в зависимости от рандома

    @bot.message_handler(content_types=['photo'])
    def user_photo(message):
        randomm = random.randint(1,3)
        time.sleep(1)
        if randomm == 1:
            bot.send_message(message.chat.id, 'Какое красивое фото😍')
        elif randomm == 2:
            bot.send_message(message.chat.id, 'Это очень красиво..')
        elif randomm == 3:
            bot.send_message(message.chat.id, 'Запредельная красота')
        else:
            bot.send_message(message.chat.id, 'Помоему это не фото')

    bot.infinity_polling()
    ```

3.  **Замените `'Ваш API'` на токен API, полученный от BotFather.**

4.  **Запустите скрипт:**

    ```bash
    python main.py
    ```

5.  **Найдите своего бота в Telegram и начните с ним разговор.**

## Зависимости

*   `pyTelegramBotAPI` (telebot)

## Авторы

*   [Ваше имя]

## Лицензия

Этот проект распространяется под лицензией MIT. Подробнее см. в файле LICENSE.
