# Импортируем библиотеку vk_api
import vk_api , os, json
from vk_api.longpoll import VkLongPoll, VkEventType
from bs4 import BeautifulSoup,element
import requests
import lxml
url1='https://stopgame.ru/news'
url2='https://pogoda.mail.ru/prognoz/moskva/'
sg = requests.get(url1)
pog=requests.get(url2)
soup1 = BeautifulSoup(sg.text , 'lxml')
soup2= BeautifulSoup(pog.text ,'lxml')
gg = soup2.find( 'div',{'class':'information__content__temperature'})
for e in gg:
    if type(e) == element.NavigableString and e.strip():
        quo=e
quotes = soup1.find_all('div',class_="caption caption-bold")
ssl=soup1.a.get('href')

# Создаём переменную для удобства в которой хранится наш токен от группы

token = "865ce5fbfa70714548a42e42291327ed1f8787152364ab9a523c48c883068f95349ab2d355d3b56f7f542"  # В ковычки вставляем аккуратно наш ранее взятый из группы токен.

# Подключаем токен и longpoll
bh = vk_api.VkApi(token=token)
give = bh.get_api()
longpoll = VkLongPoll(bh)


# Создадим функцию для ответа на сообщения в лс группы
def ms(id, text):
    bh.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0})


# Слушаем longpoll(Сообщения)
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        # Чтобы наш бот не слышал и не отвечал на самого себя
        if event.to_me:

            # Для того чтобы бот читал все с маленьких букв
            message = event.text.lower()
            # Получаем id пользователя
            id = event.user_id

            # Доисторическая логика общения на ифах
            # Перед вами структура сообщений на которые бот сможет ответить, elif можно создавать сколько угодно, if и else же могут быть только 1 в данной ситуации.
            # if - если, else - иначе(значит бот получил сообщение на которое не вызвана наша функция для ответа)

            if message == 'начать':
                ms(id, 'Привет, я бот!')
            

            elif message == 'погода' or message=='температура':

                pogoda=(f'Температура: {quo} ')
                ms(id,pogoda)

            elif message == 'новости':
                # Отправляем картинку и текст
                for n, i in enumerate(quotes, start=1):
                    itemName = i.find('a').text.strip()
                    new=(f'{n}: {itemName} ССЫЛКА:https://stopgame.ru{ssl}')
                    ms(id,new)
                    if n>3:
                        break


            else:
                ms(id, 'Я вас не понимаю! :(')
