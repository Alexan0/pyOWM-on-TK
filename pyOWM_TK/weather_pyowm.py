from tkinter import *
from tkinter import messagebox
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
from pyowm.commons.exceptions import NotFoundError

main = Tk()
main.title('Погода')
main.config(bg='#333')
main.geometry('300x300')
main.resizable(False, False)

photo = PhotoImage(file="images.png")
main.iconphoto(False, photo)

def weather():
    config_dict = get_default_config()
    config_dict['language'] = 'ru'
    owm = OWM('c1188bdbbac1972ff8ea793e1972c4ee', config_dict)

    place = entry_city.get()

    mgr = owm.weather_manager()
    try:
        observation = mgr.weather_at_place(place)
        w = observation.weather

        t = w.temperature("celsius")
        now_temp = t["temp"]
        feels_like = t["feels_like"]
        temp_max = t["temp_max"]
        temp_min = t["temp_min"]
        
        res = (f"В городе {place} сейчас: {now_temp}°C\nОщущается как: {feels_like}°C\nМаксимальная температура: {temp_max}°C\nМинимальная: {temp_min}°C.")
        label_res = Label(main,text=res,fg='#fff',bg='#333')
        label_res.grid(row=4,column=1)
    except NotFoundError:
        messagebox.showinfo('Ошибка', f'Города - {place} не существует!\nПроверьте, возможно вы ошиблись.')


name = Label(main, text= 'Погода на сегодня',bg='#333',fg='#fff',font=('Arial', 11))
name.grid(row=0, column=1)

name_city = Label(main,text='Введите город:',bg='#333',fg='#fff',font=('Arial', 11))
name_city.grid(row=1,column=1)

entry_city = Entry(main,bg='#333',fg='#fff',font=('Arial', 11))
entry_city.grid(row=2,column=1,padx=71)

btn_check = Button(main,text='Ok',command=weather,bg='#333',fg='#fff',font=('Arial', 11))
btn_check.grid(row=3,column=1)

main.mainloop()