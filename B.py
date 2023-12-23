import telebot
import requests
from telebot import types
from random import randint
main_url = 'https://newsapi.org/v2/everything?q=tesla&from=2023-11-23&sortBy=publishedAt&apiKey=85a8fa826a63403bab28c51a2e679579'

def news():
    global main_url
    main_url = requests.get(main_url).json()
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Вернуться в меню', callback_data='menu')
    markup.row(btn1)
    try:
        article = main_url['articles']
        news_title = []
        news_url = []
        news_time = []
        counter = 0
        for art in article:
            news_title.append(art['title'])
            news_url.append(art['url'])
            news_time.append(art['publishedAt'])
            counter += 1
            if counter >= 5:
                break
        info = news_title[randint(0, counter-1)]
        res = f'{info}\n{news_url[news_title.index(info)]}\n{news_time[news_title.index(info)]}'
        return res
    except KeyError:
        return main_url['message']
