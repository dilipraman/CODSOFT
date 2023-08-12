from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox 
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=tk.Tk()
root.title("WEATHER FINDER")
root.geometry("900x500+300+200")
root.iconbitmap("C:/Users/91949/Desktop/weather/image/weather.ico")
root.resizable(False,False)

def getWeather():
     city=textsite.get()
     
     geolocator=Nominatim(user_agent="geoapiExercises")
     location=geolocator.geocode(city)
     obj=TimezoneFinder()
     result= obj.timezone_at(lng=location.longitude,lat=location.latitude)

     home=pytz.timezone(result)
     local_time=datetime.now(home)
     current_time=local_time.strftime("%I:%M %p")
     clock.config(text=current_time)
     name.config(text="WEATHER")
     #weather
     api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=cffbf9bb228d00ff5c37465e6969f1fb"

     json_data=requests.get(api).json()
     condition = json_data['weather'][0]['main']
     description=json_data['weather'][0]['description']
     temp=int(json_data['main']['temp']-273.15)
     pressure=json_data['main']['pressure']
     humidity=json_data['main']['humidity']
     wind=json_data['wind']['speed']

     t.config(text=(temp,"°"))
     c.config(text=(condition,"feel"))
     
     w.config(text=wind)
     h.config(text=humidity)
     d.config(text=description)
     p.config(text=pressure)
    


#Searching block
search_image=PhotoImage(name="image_1",file="C:/Users/91949/Desktop/weather/image/searchbar.png")
imagelable=Label(root,image=search_image)
imagelable.place(x=20,y=20)

textsite=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textsite.place(x=50,y=40)
textsite.focus()

search_icon=PhotoImage(name="image_2",file="C:/Users/91949/Desktop/weather/image/searchicon.png")
image_icon_bt=Button(root,image=search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
image_icon_bt.place(x=400,y=34)

#logo
logo_img=PhotoImage(name="image_3",file="C:/Users/91949/Desktop/weather/image/IMGlogo.png")
logo=Label(image=logo_img)
logo.place(x=150,y=100)


#bottonblock

frameimg=PhotoImage(name="image_4",file="C:/Users/91949/Desktop/weather/image/framebar.png")
frame=Label(image=frameimg)
frame.pack(padx=5,pady=5,side=BOTTOM)

#timezone
name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)


#label

label1=Label(root,text="WIND",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)
label2=Label(root,text="HUMIDITY",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label2.place(x=250,y=400)
label3=Label(root,text="DESCRIPTION",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label3.place(x=430,y=400)
label4=Label(root,text="PRESSURE",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label4.place(x=650,y=400)


t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",70,"bold"))
c.place(x=400,y=250)

w=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)
h=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=280,y=430)
d=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=450,y=430)
p=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=670,y=430)



root.mainloop()
