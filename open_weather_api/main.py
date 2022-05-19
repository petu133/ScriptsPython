from dotenv import load_dotenv  #for python-dotenv method
load_dotenv()                   #for python-dotenv method
import tkinter as tk 
import requests
import time
import os

api_key = os.environ.get('APIKEY')

def getWeather(display): #This function needs to inherit the tkinder portrait to show the information
    city = entryField.get()
    url_call = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    json_data = requests.get(url_call).json()
    condition = json_data['weather'][0]['main']
    temperature = int(json_data['main']['temp'] - 273)
    pressure = json_data['main']['pressure']
    wind = json_data['wind']['speed']
    min_t = int(json_data['main']['temp_min'] - 273)
    max_t = int(json_data['main']['temp_max'] - 273)
    country = json_data['sys']['country']
    latitude = json_data['coord']['lat']
    longitude = json_data['coord']['lon']
    info_principal = f"Current Condition: {condition} \n Current Temperature: {temperature}° Celsius"
    info_secondary = f"Latitude: {latitude} \nLongitude: {longitude} \nCountry: {country} \nPressure: {pressure}\"hPa\" \nWind: {wind} \"meters per second\" \nMinimum Temperature: {min_t}°C \nMaximum Temperature: {max_t}°C \n"
    first_label.config(text = info_principal)
    second_label.config(text = info_secondary)

#creating widget
display = tk.Tk()
display.title("Open Weather")
display.geometry("1000x600")

font_principal = ("arial", 40, "bold")
font_secundary = ("calibri", 20, "italic")
entryField = tk.Entry(display, justify='center', font = font_principal)
entryField.pack(fill= None, side='bottom')
entryField.focus() #determines that this field is going to receive the imput from the user 
entryField.bind('<Return>', getWeather)
first_label = tk.Label(display, font = font_principal)
first_label.pack()
second_label = tk.Label(display, font = font_secundary)
second_label.pack()
display.mainloop() #set endpoint for the widget

