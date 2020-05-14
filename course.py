import requests
from bs4 import BeautifulSoup


class Dollar:
    DOLLAR_RUB = 'https://www.google.com/search?rlz=1C1VLSB_enRU725RU772&sxsrf=ALeKk02twJQ4QxMOgb3MfN1h6Z1VYBTulQ%3A1585752981080&ei=lauEXsO7BIu-tQb0oJfABQ&q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=CgZwc3ktYWIQAzIKCAAQgwEQRhCCAjIFCAAQgwEyAggAMgIIADIFCAAQgwEyAggAMgIIADICCAAyAggAMgIIADoHCAAQgwEQQzoECAAQQ1CZDFjjLWD4MGgCcAB4A4AByguIAYopkgELMy00LjQuMS4wLjGYAQCgAQGqAQdnd3Mtd2l6&sclient=psy-ab&ved=0ahUKEwiD2o2ZvsfoAhULX80KHXTQBVgQ4dUDCAs&uact=5'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    def __init__(self):
        self.dollor_value = 78.5


    def get_currency_price(self):
        full_page = requests.get(self.DOLLAR_RUB, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

        return 'Курс Рубля к Доллару: {}'.format(convert[0].text.replace(',', '.'))


class Hryvnia:
    HRYVNIA_RUB = 'https://www.google.com/search?rlz=1C1VLSB_enRU725RU772&sxsrf=ALeKk00Fk4_WMw9g2y40QQF69twZtU8wEA%3A1585768681965&ei=6eiEXum3OpLA0PEPqcyR-AI&q=%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=CgZwc3ktYWIQAzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJ1D-A1jnHmCHIWgCcAB4AIABAIgBAJIBAJgBAKABAaoBB2d3cy13aXqwAQo&sclient=psy-ab&ved=0ahUKEwip0O_X-MfoAhUSIDQIHSlmBC8Q4dUDCAs&uact=5'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    def __init__(self):
        self.hryvnia_value = ' '


    def get_currency_price(self):
        full_page = requests.get(self.HRYVNIA_RUB, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

        return "Курс Рубля к Гривне: {}".format(convert[0].text.replace(',', '.'))


class Euro:
    EURO_RUB = 'https://www.google.com/search?newwindow=1&rlz=1C1VLSB_enRU725RU772&sxsrf=ALeKk03TSWxu1WWL5kOOKuhjSshdf2fqtQ%3A1586976625104&ei=cVeXXu38BcnQ6QTj1bKgBg&q=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%BA%D1%83%D1%80%D1%81+%D1%83%D0%B2%D1%80%D0%BE+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=CgZwc3ktYWIQARgAMgQIABAKMgQIABAKMgQIABAKMgQIABAKMgQIABAKMgQIABAKMgQIABAKMgQIABAKMgQIABAKMgQIABAKOgQIABBHOgYIABAHEB5KEQgXEg0xMC0xODZnMTY4ZzE2SgwIGBIIMTAtMWcxZzJQwf0MWPmEDWDEkQ1oAHACeAGAAewFiAGACpIBBzAuMy42LTGYAQCgAQGqAQdnd3Mtd2l6&sclient=psy-ab'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    def __init__(self):
        self.euro_value = ' '


    def get_currency_price(self):
        full_page = requests.get(self.EURO_RUB, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

        return "Курс Рубля к Евро: {}".format(convert[0].text.replace(',', '.'))


class Pound:
    POUND_RUB = 'https://www.google.com/search?rlz=1C1VLSB_enRU725RU772&sxsrf=ALeKk01umtxI7WfZCuQPQyMdy_8fjDelYA%3A1586890140719&ei=nAWWXvyyK8SRrgSisLugBA&q=%D0%BA%D1%83%D1%80%D1%81+%D1%84%D1%83%D0%BD%D1%82&oq=%D0%BA%D1%83%D1%80%D1%81+%D1%84%D1%83%D0%BD%D1%82&gs_lcp=CgZwc3ktYWIQAzIHCAAQRhCCAjIHCAAQFBCHAjICCAAyBwgAEBQQhwIyAggAMgIIADICCAAyAggAMgIIADICCAA6BAgAEEc6CQgAEAoQRhCCAjoECAAQCkoUCBcSEDYtMTc1ZzE4NWcxNjdnNjBKDQgYEgk2LTFnMmcxZzNQ-hxYhCpgqCxoAXACeACAAc0BiAHIBpIBBTAuNC4xmAEAoAEBqgEHZ3dzLXdpeg&sclient=psy-ab&ved=0ahUKEwj88Im5yujoAhXEiIsKHSLYDkQQ4dUDCAw&uact=5'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    def __init__(self):
        '''self.current_euro = float(self.get_currency_price())'''

    def get_currency_price(self):
        full_page = requests.get(self.POUND_RUB, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

        return "Курс Рубля к Пунду Стерлингов: {}".format(convert[0].text.replace(',', '.'))


class Yuan:
    YUAN_RUB = 'https://www.google.com/search?rlz=1C1VLSB_enRU725RU772&sxsrf=ALeKk01y9cS4_mNRB9rrJta9s12O16G6Xw%3A1586890147742&ei=owWWXvTkLIKvrgTw4qzwCA&q=%D0%BA%D1%83%D1%80%D1%81+%D1%8E%D0%B0%D0%BD%D1%8F&oq=%D0%BA%D1%83%D1%80%D1%81+%D1%8E%D0%B0%D0%BD%D1%8F&gs_lcp=CgZwc3ktYWIQAzIHCAAQRhCCAjIHCAAQFBCHAjICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAOgQIABBHOgcIIxDqAhAnOgQIIxAnOgUIABCDAToECAAQQzoHCAAQgwEQQzoJCCMQJxBGEIICOgQIABAKSikIFxIlMGcxNjJnMTU1ZzE2N2cxNjdnMTUzZzE3MGcxOTBnMTM0ZzExNUoXCBgSEzBnMmcxZzFnMWcxZzJnMWcxZzNQpakPWMP-D2CdgRBoBHABeACAAbgBiAHRDpIBBDAuMTKYAQCgAQGqAQdnd3Mtd2l6sAEK&sclient=psy-ab&ved=0ahUKEwi0wra8yujoAhWCl4sKHXAxC44Q4dUDCAw&uact=5'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    def __init__(self):
        '''self.current_euro = float(self.get_currency_price())'''

    def get_currency_price(self):
        full_page = requests.get(self.YUAN_RUB, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

        return "Курс Рубля к Юаню: {}".format(convert[0].text.replace(',', '.'))


class Bitcoin:
    BITOK_RUB = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD%D0%B0+%D0%BD%D0%B0+%D1%80%D1%83%D0%B1%D0%BB%D0%B8&rlz=1C1VLSB_enRU725RU772&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD%D0%B0+%D0%BD%D0%B0+%D1%80%D1%83%D0%B1%D0%BB%D0%B8&aqs=chrome..69i57j35i39j0l6.8181j1j7&sourceid=chrome&ie=UTF-8'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    def __init__(self):
       self.norm_bit = 6000

    def get_currency_price(self):
        full_page = requests.get(self.BITOK_RUB, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

        return "Цена Биткоина в рублях:\n{}".format(convert[0].text.replace(',', '.'))


