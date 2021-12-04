import pyowm
from telegram.ext import Updater


def calculate_weather(update, context):
    owm = pyowm.OWM("5e195eaedcb783c7bf3a21d13e9d10f7")
    place = input("В каком городе/стране?: ")
    mgr = owm.weather_manager()
    # Search for current weather in place and get details
    observation = mgr.weather_at_place(place)
    w = observation.weather

    weather = {}

    update.message.reply_text("В городе " + place + " сейчас " + w.detailed_status)
    update.message.reply_text("Температура сейчас: " + str(w.temperature('celsius')["temp"]))

    if w.temperature('celsius')["temp"] < 10:
        update.message.reply_text("Оденься потеплее")
    elif w.temperature('celsius')["temp"] < 20:
        update.message.reply_text("Ходи в чем угодно")

    return weather()



    user_weather = calculate_weather()
    update.message.reply_text(f"{user_weather()}")