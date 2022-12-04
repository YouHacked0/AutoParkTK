import collections
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import logging as log
# Если хотим ВКЛЮЧИТЬ логи - оставляем всё так.
# Если хотим ВЫКЛЮЧИТЬ логи - добавляем "#" в начале следующей строки.
log.getLogger().setLevel(log.DEBUG)



class DefaultAutopark:
    def __init__(self):
        self.park = {}

    def AddCar(self, brand, model, color, year, price, booked=False):
        i = 0
        if self.park != {}:
            [i] = collections.deque(self.park, maxlen=1)
        self.park.update({i + 1: [brand, model, color, int(year), int(price), bool(booked)]})
        return i + 1

    def ChangeCar(self, car_id, type_edit, value):
        if type_edit == "brand":
            self.park[car_id][0] = value
        elif type_edit == "model":
            self.park[car_id][1] = value
        elif type_edit == "color":
            self.park[car_id][2] = value
        elif type_edit == "year":
            self.park[car_id][3] = int(value)
        elif type_edit == "price":
            self.park[car_id][4] = int(value)
        elif type_edit == "booked":
            self.park[car_id][5] = bool(value)

    def ViewCars(self):
        return self.park

    def DeleteCar(self, car_id):
        del self.park[car_id]

    def ViewBrandCar(self, brand):
        nums = []
        for i, z in self.park.items():
            if z[0] == brand:
                nums.append(self.park[i])
        return nums


class EconomAutopark(DefaultAutopark):
    def __init__(self):
        DefaultAutopark.__init__(self)


class ComfortAutopark(DefaultAutopark):
    def __init__(self):
        DefaultAutopark.__init__(self)


class BusinessAutopark(DefaultAutopark):
    def __init__(self):
        DefaultAutopark.__init__(self)


# TKINTER

autoparks = {}


def new_tk():
    def do():
        if type.get() == "Econom":
            if autoparks == {}:
                i = 0
            else:
                [i] = collections.deque(autoparks, maxlen=1)
                i = i + 1
            messagebox.showinfo("AutoParkTK", f"Your identificator is: {i}")
            log.debug("A new autopark has been registered")
            print(autoparks)
            autoparks[i] = EconomAutopark()

        elif type.get() == "Comfort":
            if autoparks == {}:
                i = 0
            else:
                [i] = collections.deque(autoparks, maxlen=1)
                i = i + 1
            messagebox.showinfo("AutoParkTK", f"Your identificator is: {i}")
            log.debug("A new autopark has been registered")
            print(autoparks)
            autoparks[i] = ComfortAutopark()

        elif type.get() == "Business":
            if autoparks == {}:
                i = 0
            else:
                [i] = collections.deque(autoparks, maxlen=1)
                i = i + 1
            messagebox.showinfo("AutoParkTK", f"Your identificator is: {i}")
            log.debug("A new autopark has been registered")
            print(autoparks)
            autoparks[i] = BusinessAutopark()

        new.destroy()

    new = Toplevel(root)

    text = Label(new, text="Класс автопарка:")
    text.pack()

    type = Combobox(new)
    type['values'] = ("Econom", "Comfort", "Business")
    type.current(1)
    type.pack()

    save = Button(new, command=do, text="Подтвердить")
    save.pack()


def add_tk():
    def do():
        autoparks[int(id.get())].AddCar(brand.get(), model.get(), color.get(), year.get(), price.get())
        log.debug("A new car has been registered")

    add = Toplevel(root)

    Label(add, text="Идентификатор парка").pack()
    id = Entry(add, width=5)
    id.pack()

    Label(add, text="Бренд").pack()
    brand = Entry(add, width=5)
    brand.pack()

    Label(add, text="Модель").pack()
    model = Entry(add, width=5)
    model.pack()

    Label(add, text="Цвет").pack()
    color = Entry(add, width=5)
    color.pack()

    Label(add, text="Год выпуска").pack()
    year = Entry(add, width=4)
    year.pack()

    Label(add, text="Стоимость").pack()
    price = Entry(add, width=5)
    price.pack()

    Button(add, text="Подтвердить", command=do).pack()


def viw_tk():
    view = Toplevel(root)

    listt = ""
    for z, x in autoparks.items():
        listt += f"Автопарк {z}: {x.ViewCars()}\n"
    print(listt)
    lbl = Label(view, text=listt)
    lbl.pack()


def del_tk():
    def do():
        autoparks[int(parkid.get())].DeleteCar(int(carid.get()))
        log.debug(f"Car n{carid.get()} has been deleted.")
    dell = Toplevel(root)

    Label(dell, text="ID автопарка").pack()
    parkid = Entry(dell)
    parkid.pack()

    Label(dell, text="ID машины").pack()
    carid = Entry(dell)
    carid.pack()

    Button(dell, text="Подтвердить", command=do).pack()


def edt_tk():
    def do():
        autoparks[int(park.get())].ChangeCar(int(id.get()), what_edit.get(), value.get())
        log.debug(f"Car n{id.get()} has been edited.")
    edt = Toplevel(root)

    Label(edt, text="Идентификатор парка").pack()
    park = Entry(edt, width=5)
    park.pack()


    Label(edt, text="Идентификатор машины").pack()
    id = Entry(edt, width=5)
    id.pack()


    Label(edt, text="Что изменяем? (на английском)").pack()
    what_edit = Entry(edt, width=5)
    what_edit.pack()


    Label(edt, text="Значение").pack()
    value = Entry(edt, width=5)
    value.pack()


    Button(edt, text="Подтвердить", command=do).pack()


def tkinter():
    global root
    root = Tk()
    root.title("Auto-parks")

    Button(root, text="New Autopark", command=new_tk).pack()
    Button(root, text="Add Car", command=add_tk).pack()
    Button(root, text="View Autoparks + Cars", command=viw_tk).pack()
    Button(root, text="Delete Car", command=del_tk).pack()
    Button(root, text="Edit Car", command=edt_tk).pack()

    root.mainloop()


if __name__ == '__main__':
    tkinter()





