from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import config
from scrapper import *
from dbhelperrr import DBHelper

db = DBHelper()
bot = Bot(config.token)
dp = Dispatcher(bot)
la_liga =  [
            "Реал Мадрид","Барселона","Атлетико Мадрид","Севилья","Альмерия","Атлетик Бильбао","Бетис","Валенсия","Вильярреал","Жирона",
            "Кадис","Мальорка","Осасуна","Райо Вальекано","Реал Вальядолид","Реал Сосьедад","Сельта","Хетафе","Эльче","Эспаньол"
           ]

premier_league = [
                  "Манчестер Сити","Ливерпуль","Манчестер Юнайтед","Челси","Тоттенхэм","Арсенал","Астон Вилла",
                  "Борнмут","","Брайтон","Брентфорд","Вест Хэм","Вулверхэмптон","Кристал Пэлас","Лестер Сити",
                  "Лидс Юнайтед","Ноттингем Форест","Ньюкасл","Саутгемптон","Фулхэм","Эвертон"
                 ]

serie_a = [
           "Милан","Интер","Ювентус","Рома","Лацио","Наполи","Фиорентина","Аталанта","Болонья","Верона","Кремонезе",
           "Лечче","Монца","Салернитана","Сампдория","Сассуоло","Специя","Торино","Удинезе","Эмполи"
          ]

bundesliga = [
              "Бавария","Боруссия Дортмунд","Боруссия М","РБ Лейпциг","Айнтрахт Франкфурт","Аугсбург","Байер","Бохум",
              "Вердер","Вольфсбург","Герта","Кёльн","Майнц","Унион Берлин","Фрайбург","Хоффенхайм","Шальке","Штутгарт"
             ]

ligue_1 = [
           "ПСЖ","Лион","Лилль","Монако","Марсель","Анже","Аяччо","Брест","Клермон","Ланс",
           "Лорьян","Монпелье","Нант","Ницца","Осер","Реймс","Ренн","Страсбур","Труа","Тулуза"
          ]

rpl = [
       "Зенит","ЦСКА Москва","Спартак","Динамо Москва","Локомотив Москва","Ростов","Ахмат","Краснодар",
       "Крылья Советов","Оренбург","Пари Нижний Новгород","ПФК Сочи","Торпедо Москва","Урал","Факел","Химки"
      ]


@dp.message_handler(commands="start")
async def start(message: types.Message):
    League_buttons = ["La Liga", "Premier League", "Serie A", "Bundesliga", "Ligue 1", "РПЛ","В главное меню"]
    League_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    League_keyboard.add(*League_buttons)

    await message.answer("Привет, выбери лигу", reply_markup=League_keyboard)


@dp.message_handler(Text(equals="Расписание матчей"))
async def Raspisanie(message: types.Message):
    Main_menu_buttons = ["Расписание матчей","Расписание на завтра","Добавить новый(-е) клуб(-ы)","Список избранных клубов","Удалить все избранные клубы" ]
    Main_menu_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Main_menu_keyboard.add(*Main_menu_buttons)
    user_id = message.from_user.id
    clubs = db.get_items(user_id)
    i = 0
    b = 0
    datatime = []
    raspisanie_team1 = []
    raspisanie_team2 = []
    raspisanie = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    while i < 100:
        if footbal_schedule[i].text in (clubs) or footbal_schedule[i+1].text in (clubs):
            datatime.append(match_datatime[b].text)
            raspisanie_team1.append(footbal_schedule[i].text)
            raspisanie_team2.append(footbal_schedule[i+1].text)
        b += 1
        i += 2

    for i in range(0, len(datatime)):
        raspisanie[i] = datatime[i] + ' ' + raspisanie_team1[i] + ' - ' +raspisanie_team2[i]
    i = 0
    while i < len(raspisanie)-1:
        if raspisanie[i] in (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20):
            del raspisanie[i]
        else:
            i += 1
        
    del raspisanie[len(raspisanie)-1]
    if raspisanie == []:
        await message.answer("Матчей нет", reply_markup=Main_menu_keyboard)
    else:
        for i in range(0,len(raspisanie)):
            await message.answer(raspisanie[i], reply_markup=Main_menu_keyboard)


@dp.message_handler(Text(equals="Расписание на завтра"))
async def Raspisanie_Tomorrow(message: types.Message):
    Main_menu_buttons = ["Расписание матчей","Расписание на завтра","Добавить новый(-е) клуб(-ы)","Список избранных клубов","Удалить все избранные клубы" ]
    Main_menu_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Main_menu_keyboard.add(*Main_menu_buttons)
    user_id = message.from_user.id
    clubs = db.get_items(user_id)
    i = 0
    b = 0
    datatime_tomorrow = []
    raspisanie_team1_tomorrow = []
    raspisanie_team2_tomorrow = []
    raspisanie_tomorrow = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    while i < 100:
        if footbal_schedule_tomorrow[i].text in (clubs) or footbal_schedule_tomorrow[i+1].text in (clubs):
            datatime_tomorrow.append(match_datatime_tomorrow[b].text)
            raspisanie_team1_tomorrow.append(footbal_schedule_tomorrow[i].text)
            raspisanie_team2_tomorrow.append(footbal_schedule_tomorrow[i+1].text)
        b += 1
        i += 2

    for i in range(0, len(datatime_tomorrow)):
        raspisanie_tomorrow[i] = datatime_tomorrow[i] + ' ' + raspisanie_team1_tomorrow[i] + ' - ' +raspisanie_team2_tomorrow[i]
    i = 0
    while i < len(raspisanie_tomorrow)-1:
        if raspisanie_tomorrow[i] in (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20):
            del raspisanie_tomorrow[i]
        else:
            i += 1
        
    del raspisanie_tomorrow[len(raspisanie_tomorrow)-1]
    if raspisanie_tomorrow == []:
        await message.answer("Матчей нет", reply_markup=Main_menu_keyboard)
    else:
        for i in range(0,len(raspisanie_tomorrow)):
            await message.answer(raspisanie_tomorrow[i], reply_markup=Main_menu_keyboard)


@dp.message_handler(Text(equals="Добавить новый(-е) клуб(-ы)"))
async def Add_Club(message: types.Message):
    League_buttons = ["La Liga", "Premier League", "Serie A", "Bundesliga", "Ligue 1", "РПЛ","В главное меню"]
    League_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    League_keyboard.add(*League_buttons)
    await message.answer("Выбери лигу", reply_markup=League_keyboard)

    
@dp.message_handler(Text(equals="Список избранных клубов"))
async def List_Clubs(message: types.Message):
    Main_menu_buttons = ["Расписание матчей","Расписание на завтра","Добавить новый(-е) клуб(-ы)","Список избранных клубов","Удалить все избранные клубы" ]
    Main_menu_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Main_menu_keyboard.add(*Main_menu_buttons)
    user_id = message.from_user.id
    clubs = db.get_items(user_id)
    if clubs == []:
        await message.answer("Список пуст", reply_markup=Main_menu_keyboard)
    else:
        await message.answer(clubs, reply_markup=Main_menu_keyboard)
    

@dp.message_handler(Text(equals="Удалить все избранные клубы"))
async def Clear_All_Clubs(message: types.Message):
    Main_menu_buttons = ["Расписание матчей","Расписание на завтра","Добавить новый(-е) клуб(-ы)","Список избранных клубов","Удалить все избранные клубы" ]
    Main_menu_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Main_menu_keyboard.add(*Main_menu_buttons)
    user_id = message.from_user.id
    db.delete_item(user_id)
    await message.answer("Список избранных клубов очищен!", reply_markup=Main_menu_keyboard)


@dp.message_handler(Text(equals="La Liga"))
async def La_Liga(message: types.Message):
    La_Liga_buttons = [
                       "Реал Мадрид","Барселона","Атлетико Мадрид","Севилья","Альмерия","Атлетик Бильбао","Бетис",
                       "Валенсия","Вильярреал","Жирона","Кадис","Мальорка","Осасуна","Райо Вальекано","Реал Вальядолид",
                       "Реал Сосьедад","Сельта","Хетафе","Эльче","Эспаньол","Назад","В главное меню"
                      ]

    La_Liga_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    La_Liga_keyboard.add(*La_Liga_buttons)

    await message.answer("Выберите клуб(-ы)", reply_markup=La_Liga_keyboard)


@dp.message_handler(Text(equals=la_liga))
async def La_Liga_Clubs(message: types.Message):
    team  = message.text
    user_id = message.from_user.id
    db.add_item(team, user_id)
    La_Liga_buttons = [
                       "Реал Мадрид","Барселона","Атлетико Мадрид","Севилья","Альмерия","Атлетик Бильбао","Бетис",
                       "Валенсия","Вильярреал","Жирона","Кадис","Мальорка","Осасуна","Райо Вальекано","Реал Вальядолид",
                       "Реал Сосьедад","Сельта","Хетафе","Эльче","Эспаньол","Назад","В главное меню"
                      ]

    La_Liga_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    La_Liga_keyboard.add(*La_Liga_buttons)

    await message.answer("Клуб добавлена", reply_markup=La_Liga_keyboard)



@dp.message_handler(Text(equals="Premier League"))
async def Premier_League(message: types.Message):
    Premier_League_buttons = [
                              "Манчестер Сити","Ливерпуль","Манчестер Юнайтед","Челси","Тоттенхэм","Арсенал","Астон Вилла","Борнмут",
                              "Брайтон","Брентфорд","Вест Хэм","Вулверхэмптон","Кристал Пэлас","Лестер Сити","Лидс Юнайтед",
                              "Ноттингем Форест","Ньюкасл","Саутгемптон","Фулхэм","Эвертон","Назад","В главное меню"
                             ]

    Premier_League_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Premier_League_keyboard.add(*Premier_League_buttons)

    await message.answer("Выберите клуб(-ы)", reply_markup=Premier_League_keyboard)


@dp.message_handler(Text(equals=premier_league))
async def Premier_League_Clubs(message: types.Message):
    team  = message.text
    user_id = message.from_user.id
    db.add_item(team, user_id)
    
    Premier_League_buttons = [
                              "Манчестер Сити","Ливерпуль","Манчестер Юнайтед","Челси","Тоттенхэм","Арсенал","Астон Вилла","Борнмут",
                              "Брайтон","Брентфорд","Вест Хэм","Вулверхэмптон","Кристал Пэлас","Лестер Сити","Лидс Юнайтед",
                              "Ноттингем Форест","Ньюкасл","Саутгемптон","Фулхэм","Эвертон","Назад","В главное меню"
                             ]
                             
    Premier_League_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Premier_League_keyboard.add(*Premier_League_buttons)

    await message.answer("Клуб добавлен", reply_markup=Premier_League_keyboard)


@dp.message_handler(Text(equals="Serie A"))
async def Serie_A(message: types.Message):
    Serie_A_buttons = [
                       "Милан","Интер","Ювентус","Рома","Лацио","Наполи","Фиорентина","Аталанта","Болонья","Верона","Кремонезе","Лечче",
                       "Монца","Салернитана","Сампдория","Сассуоло","Специя","Торино","Удинезе","Эмполи","Назад","В главное меню"
                      ]

    Serie_A_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Serie_A_keyboard.add(*Serie_A_buttons)

    await message.answer("Выберите клуб(-ы)", reply_markup=Serie_A_keyboard)


@dp.message_handler(Text(equals=serie_a))
async def Serie_A_Clubs(message: types.Message):
    team  = message.text
    user_id = message.from_user.id
    db.add_item(team, user_id)
    
    Serie_A_buttons = [
                       "Милан","Интер","Ювентус","Рома","Лацио","Наполи","Фиорентина","Аталанта","Болонья","Верона","Кремонезе","Лечче",
                       "Монца","Салернитана","Сампдория","Сассуоло","Специя","Торино","Удинезе","Эмполи","Назад","В главное меню"
                      ]
                             
    Serie_A_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Serie_A_keyboard.add(*Serie_A_buttons)

    await message.answer("Клуб добавлен", reply_markup=Serie_A_keyboard)


@dp.message_handler(Text(equals="Bundesliga"))
async def Bundesliga(message: types.Message):
    Bundesliga_buttons = [
                          "Бавария","Боруссия Дортмунд","Боруссия М","РБ Лейпциг","Айнтрахт Франкфурт","Аугсбург","Байер","Бохум","Вердер",
                          "Вольфсбург","Герта","Кёльн","Майнц","Унион Берлин","Фрайбург","Хоффенхайм","Шальке","Штутгарт","Назад","В главное меню"
                         ]

    Bundesliga_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Bundesliga_keyboard.add(*Bundesliga_buttons)

    await message.answer("Выберите клуб(-ы)", reply_markup=Bundesliga_keyboard)


@dp.message_handler(Text(equals=bundesliga))
async def Bundesliga_Clubs(message: types.Message):
    team  = message.text
    user_id = message.from_user.id
    db.add_item(team, user_id)

    Bundesliga_buttons = [
                          "Бавария","Боруссия Дортмунд","Боруссия М","РБ Лейпциг","Айнтрахт Франкфурт","Аугсбург","Байер","Бохум","Вердер",
                          "Вольфсбург","Герта","Кёльн","Майнц","Унион Берлин","Фрайбург","Хоффенхайм","Шальке","Штутгарт","Назад","В главное меню"
                         ]

    Bundesliga_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Bundesliga_keyboard.add(*Bundesliga_buttons)

    await message.answer("Выберите клуб(-ы)", reply_markup=Bundesliga_keyboard)


@dp.message_handler(Text(equals="Ligue 1"))
async def Ligue_1(message: types.Message):
    Ligue_1_buttons = [
                       "ПСЖ","Лион","Лилль","Монако","Марсель","Анже","Аяччо","Брест","Клермон","Ланс","Лорьян","Монпелье",
                       "Нант","Ницца","Осер","Реймс","Ренн","Страсбур","Труа","Тулуза","Назад","В главное меню"
                      ]

    Ligue_1_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Ligue_1_keyboard.add(*Ligue_1_buttons)

    await message.answer("Выберите клуб(-ы)", reply_markup=Ligue_1_keyboard)


@dp.message_handler(Text(equals=ligue_1))
async def Ligue_1_Clubs(message: types.Message):
    team  = message.text
    user_id = message.from_user.id
    db.add_item(team, user_id)

    Ligue_1_buttons = [
                       "ПСЖ","Лион","Лилль","Монако","Марсель","Анже","Аяччо","Брест","Клермон","Ланс","Лорьян","Монпелье",
                       "Нант","Ницца","Осер","Реймс","Ренн","Страсбур","Труа","Тулуза","Назад","В главное меню"
                      ]

    Ligue_1_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Ligue_1_keyboard.add(*Ligue_1_buttons)

    await message.answer("Выберите клуб(-ы)", reply_markup=Ligue_1_keyboard)


@dp.message_handler(Text(equals="РПЛ"))
async def RPL(message: types.Message):
    RPL_buttons = [
                   "Зенит","ЦСКА Москва","Спартак","Динамо Москва","Локомотив Москва","Ростов","Ахмат","Краснодар","Крылья Советов",
                   "Оренбург","Пари Нижний Новгород","ПФК Сочи","Торпедо Москва","Урал","Факел","Химки","Назад","В главное меню"
                  ]

    RPL_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    RPL_keyboard.add(*RPL_buttons)

    await message.answer("Выберите клуб(-ы)", reply_markup=RPL_keyboard)


@dp.message_handler(Text(equals=rpl))
async def RPL_Clubs(message: types.Message):
    team  = message.text
    user_id = message.from_user.id
    db.add_item(team, user_id)

    RPL_buttons = [
                   "Зенит","ЦСКА Москва","Спартак","Динамо Москва","Локомотив Москва","Ростов","Ахмат","Краснодар","Крылья Советов",
                   "Оренбург","Пари Нижний Новгород","ПФК Сочи","Торпедо Москва","Урал","Факел","Химки","Назад","В главное меню"
                  ]

    RPL_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    RPL_keyboard.add(*RPL_buttons)

    await message.answer("Выберите клуб(-ы)", reply_markup=RPL_keyboard)



@dp.message_handler(Text(equals="Назад"))
async def start1(message: types.Message):
    League_buttons = ["La Liga", "Premier League", "Serie A", "Bundesliga", "Ligue 1", "РПЛ","В главное меню"]
    League_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    League_keyboard.add(*League_buttons)

    await message.answer("Выберите лигу", reply_markup=League_keyboard)


@dp.message_handler(Text(equals="В главное меню"))
async def In_Main_Menu(message: types.Message):
    Main_menu_buttons = ["Расписание матчей","Расписание на завтра","Добавить новый(-е) клуб(-ы)","Список избранных клубов","Удалить все избранные клубы" ]
    Main_menu_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Main_menu_keyboard.add(*Main_menu_buttons)
    await message.answer("Вы в главном меню!", reply_markup=Main_menu_keyboard)


def main():
    executor.start_polling(dp)


if __name__ == "__main__":
    db.setup()
    main()
