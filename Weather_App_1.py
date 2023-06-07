from tkinter import *
from tkinter import ttk
from tkinter import ttk,messagebox
import requests
def data_get():
    city=city_name.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=cfce15fa2ff77d1d425b5f13024e3b94").json()
    wc1_label.config(text=data['weather'][0]['main'])
    wd1_label.config(text=data['weather'][0]['description'])
    wt1_label.config(text=str(round(data['main']['temp']-273.15,2)))
    pre1_label.config(text=data['main']['pressure'])
win=Tk()
win.title("Weather App")
win.config(bg='skyblue')
win.geometry('1000x1140')
name_label=Label(win,text="Weather App",font=("Arial",30,"bold"))
name_label.place(x=50,y=50,height=100,width=900)
city_name=StringVar()
list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com=ttk.Combobox(win,text="Weather App",values=list_name,font=("Arial",20,"bold"),textvariable=city_name)
com.place(x=50,y=240,height=100,width=900)
wc_label=Label(win,text="Weather Climate",font=("Arial",20))
wc_label.place(x=50,y=520,height=50,width=250)
wc1_label=Label(win,text="",font=("Arial",20))
wc1_label.place(x=500,y=520,height=50,width=250)
wd_label=Label(win,text="Weather Description",font=("Arial",18))
wd_label.place(x=50,y=580,height=50,width=250)
wd1_label=Label(win,text="",font=("Arial",18))
wd1_label.place(x=500,y=580,height=50,width=250)
wt_label=Label(win,text="Temprature",font=("Arial",20))
wt_label.place(x=50,y=640,height=50,width=250)
wt1_label=Label(win,text="",font=("Arial",20))
wt1_label.place(x=500,y=640,height=50,width=250)
pre_label=Label(win,text="Pressure",font=("Arial",20))
pre_label.place(x=50,y=700,height=50,width=250)
pre1_label=Label(win,text="",font=("Arial",20))
pre1_label.place(x=500,y=700,height=50,width=250)
done_button=Button(win,text="Done",font=("Arial",30,"bold"),command=data_get)
done_button.place(y=380,height=100,width=200,x=400)
image_icon=PhotoImage(file="D:\Web-Development\Microsoft GitHub CoPilot Weather App\App_Icon.png")
win.iconphoto(False,image_icon)

#copyright
copyright=Label(win,text="©Abhishek_Swaroop",font=("Helvetica",10),fg="white",bg="#203243")
copyright.place(x=450,y=770)
'''
#copyright_symbol = u"\u00A9"
copyright_symbol = u"\N{COPYRIGHT SIGN}"
#registered_symbol = u"\u00AE"
registered_symbol = u"\N{REGISTERED SIGN}"
msg = u"Copyright: %sAbhishek_Swaroop, Registered: %s" % (copyright_symbol,registered_symbol)
messagebox.showinfo("Info", msg)
'''
win.mainloop()