from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import config
from scrapperr import *


bot = Bot(config.token)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def start(message: types.Message):
    League_buttons = ["La Liga", "Premier League", "Serie A", "Bundesliga", "Ligue 1", "РПЛ","В главное меню"]
    League_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    League_keyboard.add(*League_buttons)

    await message.answer("Привет, выбери лигу", reply_markup=League_keyboard)


@dp.message_handler(Text(equals="Расписание матчей"))
async def Raspisanie(message: types.Message):
    Main_menu_buttons = ["Расписание матчей","Добавить новый(-е) клуб(-ы)","Список избранных клубов","Удалить все избранные клубы" ]
    Main_menu_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Main_menu_keyboard.add(*Main_menu_buttons)
    with open("teams.txt", encoding="utf-8") as file:
        teams = file.readlines()
    teams = [x.replace('\n','') for x in teams]
    i = 0
    b = 0
    datatime = []
    raspisanie_team1 = []
    raspisanie_team2 = []
    raspisanie = [1,2,3,4,5,6]
    while i < 100:
        if footbal_schedule[i].text in (teams) or footbal_schedule[i+1].text in (teams):
            datatime.append(match_datatime[b].text)
            raspisanie_team1.append(footbal_schedule[i].text)
            raspisanie_team2.append(footbal_schedule[i+1].text)
        b += 1
        i += 2

    for i in range(0, len(datatime)):
        raspisanie[i] = datatime[i] + ' ' + raspisanie_team1[i] + ' - ' +raspisanie_team2[i]
    i = 0
    while i < len(raspisanie)-1:
        if raspisanie[i] in (1,2,3,4,5,6):
            del raspisanie[i]
        else:
            i += 1
        
    del raspisanie[len(raspisanie)-1]
    if raspisanie == []:
        await message.answer("Список пуст", reply_markup=Main_menu_keyboard)
    else:
        for i in range(0,len(raspisanie)):
            await message.answer(raspisanie[i], reply_markup=Main_menu_keyboard)

@dp.message_handler(Text(equals="Добавить новый(-е) клуб(-ы)"))
async def Add_Club(message: types.Message):
    League_buttons = ["La Liga", "Premier League", "Serie A", "Bundesliga", "Ligue 1", "РПЛ","В главное меню"]
    League_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    League_keyboard.add(*League_buttons)
    await message.answer("Выбери лигу", reply_markup=League_keyboard)

    
@dp.message_handler(Text(equals="Список избранных клубов"))
async def List_Clubs(message: types.Message):
    Main_menu_buttons = ["Расписание матчей","Добавить новый(-е) клуб(-ы)","Список избранных клубов","Удалить все избранные клубы" ]
    Main_menu_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Main_menu_keyboard.add(*Main_menu_buttons)
    with open("teams.txt", encoding="utf-8") as file:
        teams = file.readlines()
    teams = [x.replace('\n','') for x in teams]
    await message.answer(teams, reply_markup=Main_menu_keyboard)
    

@dp.message_handler(Text(equals="Удалить все избранные клубы"))
async def Clear_All_Clubs(message: types.Message):
    Main_menu_buttons = ["Расписание матчей","Добавить новый(-е) клуб(-ы)","Список избранных клубов","Удалить все избранные клубы" ]
    Main_menu_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Main_menu_keyboard.add(*Main_menu_buttons)
    with open("teams.txt",'w', encoding="utf-8") as f:
        pass
    await message.answer("Список избранных клубов очищен!", reply_markup=Main_menu_keyboard)


@dp.message_handler(Text(equals="La Liga"))
async def La_Liga(message: types.Message):
    La_Liga_buttons = ["Реал Мадрид","Барселона","Назад","В главное меню"]
    La_Liga_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    La_Liga_keyboard.add(*La_Liga_buttons)

    await message.answer("Выберите клуб(-ы)", reply_markup=La_Liga_keyboard)


@dp.message_handler(Text(equals="Реал Мадрид"))
async def La_Liga_Command(message: types.Message):
    team1  = message.text
    with open("teams.txt", "a", encoding="utf-8") as file:
        print(team1, file=file)
    Navigation_buttons = ["Добавить ещё клуб из La Liga","Назад","В главное меню"]
    Navigation_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Navigation_keyboard.add(*Navigation_buttons)

    await message.answer("Выберите что делать дальше", reply_markup=Navigation_keyboard)

@dp.message_handler(Text(equals="Барселона"))
async def La_Liga_Command1(message: types.Message):
    team2  = message.text
    with open("teams.txt", "a", encoding="utf-8") as file:
        print(team2, file=file)
    Navigation_buttons = ["Добавить ещё клуб из La Liga","Назад","В главное меню"]
    Navigation_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Navigation_keyboard.add(*Navigation_buttons)

    await message.answer("Выберите что делать дальше", reply_markup=Navigation_keyboard)


@dp.message_handler(Text(equals="Добавить ещё клуб из La Liga"))
async def Add_La_Liga_Clubs_More(message: types.Message):
    La_Liga_buttons = ["Реал Мадрид","Барселона","Назад","В главное меню"]
    La_Liga_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    La_Liga_keyboard.add(*La_Liga_buttons)

    await message.answer("Выберите клуб(-ы)", reply_markup=La_Liga_keyboard)


@dp.message_handler(Text(equals="Premier League"))
async def Premier_League(message: types.Message):
    Premier_League_buttons = ["Манчестер Сити","Челси","Ливерпуль","Манчестер Юнайтед","Тотенхэм","Назад","В главное меню"]
    Premier_League_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Premier_League_keyboard.add(*Premier_League_buttons)

    await message.answer("Выберите клуб(-ы)", reply_markup=Premier_League_keyboard)


@dp.message_handler(Text(equals="Ливерпуль"))
async def Premier_League_Command(message: types.Message):
    team3  = message.text
    with open("teams.txt", "a", encoding="utf-8") as file:
        print(team3, file=file)
    Premier_League_Command_buttons = ["Добавить ещё клуб из Premier League","Назад","В главное меню"]
    Premier_League_Command_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Premier_League_Command_keyboard.add(*Premier_League_Command_buttons)

    await message.answer("Выберите что делать дальше", reply_markup=Premier_League_Command_keyboard)


@dp.message_handler(Text(equals="Челси"))
async def Premier_League_Command1(message: types.Message):
    team4  = message.text
    with open("teams.txt", "a", encoding="utf-8") as file:
        print(team4, file=file)
    Premier_League_Command_buttons = ["Добавить ещё клуб из Premier League","Назад","В главное меню"]
    Premier_League_Command_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Premier_League_Command_keyboard.add(*Premier_League_Command_buttons)

    await message.answer("Выберите что делать дальше", reply_markup=Premier_League_Command_keyboard)


@dp.message_handler(Text(equals="Добавить ещё клуб из Premier League"))
async def Premier_League1(message: types.Message):
    Premier_League_buttons = ["Манчестер Сити","Челси","Ливерпуль","Манчестер Юнайтед","Тотенхэм","Назад","В главное меню"]
    Premier_League_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Premier_League_keyboard.add(*Premier_League_buttons)

    await message.answer("Выберите клуб(-ы)", reply_markup=Premier_League_keyboard)


@dp.message_handler(Text(equals="Назад"))
async def start1(message: types.Message):
    League_buttons = ["La Liga", "Premier League", "Serie A", "Bundesliga", "Ligue 1", "РПЛ","В главное меню"]
    League_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    League_keyboard.add(*League_buttons)

    await message.answer("Выберите лигу", reply_markup=League_keyboard)


@dp.message_handler(Text(equals="В главное меню"))
async def In_Main_Menu(message: types.Message):
    Main_menu_buttons = ["Расписание матчей","Добавить новый(-е) клуб(-ы)","Список избранных клубов","Удалить все избранные клубы" ]
    Main_menu_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Main_menu_keyboard.add(*Main_menu_buttons)
    await message.answer("Вы в главном меню!", reply_markup=Main_menu_keyboard)


def main():
    executor.start_polling(dp)


if __name__ == "__main__":
    main()