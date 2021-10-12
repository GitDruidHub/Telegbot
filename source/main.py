import pyowm

owm = pyowm.OWM("5e195eaedcb783c7bf3a21d13e9d10f7")

place = input("В каком городе/стране?: ")
mgr = owm.weather_manager()

# Search for current weather in place and get details
observation = mgr.weather_at_place(place)
w = observation.weather

print("В городе " + place + " сейчас " + w.detailed_status)
print("Температура сейчас: " + str(w.temperature('celsius')["temp"]))