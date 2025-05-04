from tkinter import *
import requests

root = Tk()
Fr_lab = Label(text="Please print country (ex: in,be,ua)")
Fr_fra = Frame()
Fr_lab.pack()
Fr_fra.pack()

Sc_lab = Label(text="Please print name of city(ex: kyiv, mumbai)")
Sc_fra = Frame()
Sc_lab.pack()
Sc_fra.pack()

entry_id = Entry(master=Fr_fra)
entry_id_sec = Entry(master=Sc_fra)

entry_id.grid(row=1, column=1)
First_fr = Frame()
entry_id_sec.grid(row=1, column=1)

def send_id():
    country = entry_id.get()
    city = entry_id_sec.get()
    url = "https://foreca-weather.p.rapidapi.com/location/search/{}".format(city)

    querystring = {"lang":"en","country":"{}".format(country)}

    headers = {
	"X-RapidAPI-Key": "Your_key",
	"X-RapidAPI-Host": "foreca-weather.p.rapidapi.com"
    }

    res = requests.request("GET", url, headers=headers, params=querystring)
    json = res.json()
    translation = json["locations"]
    
    for k in translation:
        id_name = k["id"]
        name = k["name"]
        country = k["country"]
        timezone = k["timezone"]
        language = k["language"]
        adminArea = k["adminArea"]
        adminArea2 = k["adminArea2"]
        adminArea3 = k["adminArea3"]
        lon = k["lon"]
        lat = k["lat"]

    if translation == []:
        finish_data.config(text="Such country or city was not found, please try again")
    else:
        finish_data.config(text="id: {}\nname: {}\ncountry: {}\ntimezone: {}\nlanguage: {}\nadminArea: {}\nadminArea2: {}\nadminArea3: {}\nlon: {}\nlat: {}".format(id_name,name,country,timezone,language,adminArea,adminArea2,adminArea3,lon,lat))


finish_data = Label()
finish_data.pack()

def input_data():

  Last_but = Frame()
  Last_but.pack()
  button = Button(text="Show", master=Last_but,  command=send_id)
  button.pack()

  mainloop()

input_data()