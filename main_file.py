#!/usr/bin/python3
# -*- coding: utf-8 -*-

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import config
import json
import keyboards
import datetime
from course import Dollar, Hryvnia, Euro, Pound, Yuan, Bitcoin
from covid import Covid19
import sys


month = {'1': 'января', '2': 'февраля', '3': 'марта', '4': 'апреля', '5': 'мая', '6': "июня", '7': 'июля',
         '8': 'августа', '9': 'сентября', '10': "октября", "11": "ноября", "12": "декабря"}
waiting = ['Минуточку...', 'Сейчас узнаю', 'Подождите немного..', 'Открываю третий глаз..',
           'Сейчас спрошу у других волков']

vk_session = vk_api.VkApi(token=config.TOKEN)
longpoll = VkBotLongPoll(vk_session, config.ID)
kol = 0



def main():
    global kol
    for event in longpoll.listen():
        if (event.type == VkBotEventType.GROUP_JOIN or event.type == VkBotEventType.MESSAGE_NEW) and kol == 0:
            kol = 1
            begining(event)
        if event.type == VkBotEventType.GROUP_LEAVE:
            kol = 0

        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.obj.message['text'] == 'Узнать дату и время':
                time_date(event)
            elif event.obj.message['text'] == 'Правила':
                rules(event)
            elif event.obj.message['text'] == 'Курсы валют':
                currency(event)
            elif event.obj.message['text'] == 'Доллар':
                dollar(event)
            elif event.obj.message['text'] == 'Гривна':
                hryvnia(event)
            elif event.obj.message['text'] == 'Евро':
                euro(event)
            elif event.obj.message['text'] == 'Пунд Стерлингов':
                pound(event)
            elif event.obj.message['text'] == 'Юань':
                yuan(event)
            elif event.obj.message['text'] == 'Биткоин':
                bitcoin(event)
            elif event.obj.message['text'] == 'Статистика COVID-19':
                covid19(event)
            elif event.obj.message['text'] == 'По всему миру':
                covid_in_the_world(event)
            elif event.obj.message['text'] == 'В России':
                covid_in_russia(event)
            elif event.obj.message['text'] == 'В США':
                covid_in_usa(event)
            elif event.obj.message['text'][0] == '?':
                covid_in_different_country(event, event.obj.message['text'])

            elif event.obj.message['text'] == 'Узнать про другие страны':
                more_countries(event)

            elif event.obj.message['text'] == 'Назад':
                vk = vk_session.get_api()
                keyboard = json.dumps(keyboards.KEYBOARD).encode('utf-8')
                keyboard = str(keyboard.decode('utf-8'))
                vk.messages.send(user_id=event.obj.message['from_id'], random_id=random.randint(0, 2 ** 64),
                                 message='ОК',
                                 keyboard=keyboard)
            else:
                error(event)


def covid_in_different_country(event, kod):
    covid19 = Covid19()
    vk = vk_session.get_api()
    vk.messages.send(user_id=event.obj.message['from_id'], message=random.choice(waiting),
                     random_id=random.randint(0, 2 ** 64))
    try:
        value = covid19.covid_in_different_country(kod)
        vk.messages.send(user_id=event.obj.message['from_id'], message=value,
                         random_id=random.randint(0, 2 ** 64))
    except Exception as ex:
        value = "Врачи пока не могут дать статистику"
        vk.messages.send(user_id=event.obj.message['from_id'], message=value,
                         random_id=random.randint(0, 2 ** 64))
    return


def covid_in_the_world(event):
    covid19 = Covid19()
    vk = vk_session.get_api()
    vk.messages.send(user_id=event.obj.message['from_id'], message=random.choice(waiting),
                     random_id=random.randint(0, 2 ** 64))
    try:
        value = covid19.check_in_the_world()
        vk.messages.send(user_id=event.obj.message['from_id'], message=value,
                         random_id=random.randint(0, 2 ** 64))
    except Exception as ex:
        value = "Врачи пока не могут дать статистику"
        vk.messages.send(user_id=event.obj.message['from_id'], message=value,
                         random_id=random.randint(0, 2 ** 64))
    return


def covid_in_russia(event):
    covid19 = Covid19()
    vk = vk_session.get_api()
    vk.messages.send(user_id=event.obj.message['from_id'], message=random.choice(waiting),
                     random_id=random.randint(0, 2 ** 64))
    try:
        value = covid19.check_in_the_russia()
        vk.messages.send(user_id=event.obj.message['from_id'], message=value,
                         random_id=random.randint(0, 2 ** 64))
    except Exception:
        value = "Врачи пока не могут дать статистику"
        vk.messages.send(user_id=event.obj.message['from_id'], message=value,
                         random_id=random.randint(0, 2 ** 64))
    return


def covid_in_usa(event):
    covid19 = Covid19()
    vk = vk_session.get_api()
    vk.messages.send(user_id=event.obj.message['from_id'], message=random.choice(waiting),
                     random_id=random.randint(0, 2 ** 64))
    try:
        value = covid19.check_in_the_usa()
        vk.messages.send(user_id=event.obj.message['from_id'], message=value,
                         random_id=random.randint(0, 2 ** 64))
    except Exception:
        value = "Врачи пока не могут дать статистику"
        vk.messages.send(user_id=event.obj.message['from_id'], message=value,
                         random_id=random.randint(0, 2 ** 64))
    return


def more_countries(event):
    vk = vk_session.get_api()
    vk.messages.send(user_id=event.obj.message['from_id'], message=random.choice(waiting),
                     random_id=random.randint(0, 2 ** 64))
    vk.messages.send(user_id=event.obj.message['from_id'],
                     message=config.COVID_MORE_COUNTRIES,
                     random_id=random.randint(0, 2 ** 64))
    return


def dollar(event):
    vk = vk_session.get_api()
    vk.messages.send(user_id=event.obj.message['from_id'], message=random.choice(waiting),
                     random_id=random.randint(0, 2 ** 64))
    value = Dollar().get_currency_price()
    vk.messages.send(user_id=event.obj.message['from_id'], message=value,
                     random_id=random.randint(0, 2 ** 64))
    return


def hryvnia(event):
    vk = vk_session.get_api()
    vk.messages.send(user_id=event.obj.message['from_id'], message=random.choice(waiting),
                     random_id=random.randint(0, 2 ** 64))
    value = Hryvnia().get_currency_price()
    vk.messages.send(user_id=event.obj.message['from_id'], message=value,
                     random_id=random.randint(0, 2 ** 64))
    return


def euro(event):
    vk = vk_session.get_api()
    vk.messages.send(user_id=event.obj.message['from_id'], message=random.choice(waiting),
                     random_id=random.randint(0, 2 ** 64))
    value = Euro().get_currency_price()
    vk.messages.send(user_id=event.obj.message['from_id'], message=value,
                     random_id=random.randint(0, 2 ** 64))
    return


def pound(event):
    vk = vk_session.get_api()
    vk.messages.send(user_id=event.obj.message['from_id'], message=random.choice(waiting),
                     random_id=random.randint(0, 2 ** 64))
    value = Pound().get_currency_price()
    vk.messages.send(user_id=event.obj.message['from_id'], message=value,
                     random_id=random.randint(0, 2 ** 64))
    return


def yuan(event):
    vk = vk_session.get_api()
    vk.messages.send(user_id=event.obj.message['from_id'], message=random.choice(waiting),
                     random_id=random.randint(0, 2 ** 64))
    value = Yuan().get_currency_price()
    vk.messages.send(user_id=event.obj.message['from_id'], message=value,
                     random_id=random.randint(0, 2 ** 64))
    return


def bitcoin(event):
    vk = vk_session.get_api()
    vk.messages.send(user_id=event.obj.message['from_id'], message=random.choice(waiting),
                     random_id=random.randint(0, 2 ** 64))
    value = Bitcoin().get_currency_price()
    vk.messages.send(user_id=event.obj.message['from_id'], message=value,
                     random_id=random.randint(0, 2 ** 64))
    return


def currency(event):
    vk = vk_session.get_api()
    keyboard = json.dumps(keyboards.KEYBOARD_2).encode('utf-8')
    keyboard = str(keyboard.decode('utf-8'))
    vk.messages.send(user_id=event.obj.message['from_id'], message='Выбери валюту',
                     random_id=random.randint(0, 2 ** 64), keyboard=keyboard)
    return


def covid19(event):
    vk = vk_session.get_api()
    keyboard = json.dumps(keyboards.KEYBOARD_3).encode('utf-8')
    keyboard = str(keyboard.decode('utf-8'))
    vk.messages.send(user_id=event.obj.message['from_id'], message='Выбери опцию',
                     random_id=random.randint(0, 2 ** 64), keyboard=keyboard)
    return


def time_date(event):
    now = datetime.datetime.now()
    message = "Сегодня {} {} {}, а спутник передаёт точное время {}:{}".format(now.day, month[str(now.month)],
                                                                               now.year, now.hour, now.minute)
    vk = vk_session.get_api()
    vk.messages.send(user_id=event.obj.message['from_id'], message=message, random_id=random.randint(0, 2 ** 64))
    return


def error(event):
    vk = vk_session.get_api()
    value = "Не знаю, что ответить.."
    vk.messages.send(user_id=event.obj.message['from_id'], message=value,
                     random_id=random.randint(0, 2 ** 64))
    return


def rules(event):
    vk = vk_session.get_api()
    keyboard = json.dumps(keyboards.KEYBOARD).encode('utf-8')
    keyboard = str(keyboard.decode('utf-8'))
    vk.messages.send(user_id=event.obj.message['from_id'],
                     message=config.RULES,
                     random_id=random.randint(0, 2 ** 64))
    return


def begining(event):
    keyboard = json.dumps(keyboards.KEYBOARD).encode('utf-8')
    keyboard = str(keyboard.decode('utf-8'))
    vk = vk_session.get_api()
    if event.type == VkBotEventType.GROUP_JOIN:
        name = vk.users.get(user_id=event.obj.user_id)[0]['first_name']
        vk.messages.send(user_id=event.obj.user_id,
                         message="Добро пожаловать, {}!\nЯ - Волчара, бот, который не выступает в цирке.1".format(name),
                         random_id=random.randint(0, 2 ** 64), keyboard=keyboard)
    if event.type == VkBotEventType.MESSAGE_NEW:
        name = vk.users.get(user_id=event.obj.message['from_id'])[0]['first_name']
        vk.messages.send(user_id=event.obj.message['from_id'],
                         message="Добро пожаловать, {}!\nЯ - Волчара, бот, который не выступает в цирке.".format(name),
                         random_id=random.randint(0, 2 ** 64), keyboard=keyboard)
    return

main()
