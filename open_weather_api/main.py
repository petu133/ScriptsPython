from dotenv import load_dotenv  #for python-dotenv method
load_dotenv()                   #for python-dotenv method
import tkinter as tk 
import requests
import time
import os

api_key = os.environ.get('APIKEY')

def getWeather():
    city = entryField.get()
    url_call = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    json_data = requests.get(url_call).json()
    

display = tk.Tk()
display.title("Open Weather")
display.size("600x500")

type_font = ("Arial", 20, "bold")
type_font2 = ("Calibri", 30, "roman")
# label_font_two = ("Calibri", 25, "italic")

entryField = tk.Entry(display, font = type_font)
entryField.pack(pady=25)
entryField.focus()

first_label = tk.Label(display, font = type_font)
first_label.pack()
second_label = tk.Label(display, font = type_font2)
second_label.pack()

display.mainloop()

