import json


KEYBOARD = {
    "one_time": False,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": json.dumps(''),
                "label": "Курсы валют"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": json.dumps(''),
                "label": "Узнать дату и время"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": json.dumps(''),
                "label": "Статистика COVID-19"
            },
            "color": "negative"
        }],
        [{
            "action": {
                "type": "text",
                "payload": json.dumps(''),
                "label": "Правила"
            },
            "color": "secondary"
        }]
    ]
    }

KEYBOARD_2 = {
    "one_time": False,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": json.dumps(''),
                "label": "Доллар"
            },
            "color": "positive"
        }],
        [{
            "action": {
                "type": "text",
                "payload": json.dumps(''),
                "label": "Евро"
            },
            "color": "positive"
        }],
        [{
            "action": {
                "type": "text",
                "payload": json.dumps(''),
                "label": "Гривна"
            },
            "color": "positive"
        }],
        [{
            "action": {
                "type": "text",
                "payload": json.dumps(''),
                "label": "Пунд Стерлингов"
            },
            "color": "positive"
        }],
        [{
            "action": {
                "type": "text",
                "payload": json.dumps(''),
                "label": "Юань"
            },
            "color": "positive"
        }],
        [{
            "action": {
                "type": "text",
                "payload": json.dumps(''),
                "label": "Биткоин"
            },
            "color": "positive"
        }],
        [{
            "action": {
                "type": "text",
                "payload": json.dumps(''),
                "label": "Назад"
            },
            "color": "negative"
        }]
    ]
    }

KEYBOARD_3 = {
    "one_time": False,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": json.dumps(''),
                "label": "По всему миру"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": json.dumps(''),
                "label": "В России"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": json.dumps(''),
                "label": "В США"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": json.dumps(''),
                "label": "Узнать про другие страны"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": json.dumps(''),
                "label": "Назад"
            },
            "color": "negative"
        }]

    ]
}