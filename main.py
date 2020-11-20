from tkinter import *
import requests


windows = Tk()
windows.title("CURRENCY CONVERTOR ")
windows.geometry("500x500")
windows.config(background="red")


#API
url = "https://v6.exchangerate-api.com/v6/a441075d3f7724c680627e8a/latest/USD"

req = requests.get(url)

result = req.json()

rates =result['conversion_rates'].keys()

#function
def convertor():

    amount = float(amnt_entry.get())

    new_amnt = amount * result['conversion_rates'][lst.get(ACTIVE)] #converting currency

    answer['text'] = new_amnt

#labels
l1_convertor = Label(windows, text = "Converting US Currency TO OTHERS",bg="yellow", fg = "black",font = ("bold",12))
l1_convertor.grid(row=0, column=6)

amnt = Label(text = "Amount:", bg = "green", fg = "black", font = ("bold",12))
amnt.grid(row=3, column=0)

#entry
amnt_entry = Entry(windows)
amnt_entry.grid(row=3, column=6)

#label
crrncy1 = Label(text = "To Currency:", bg = "green", fg = "black", font = ("bold",12))
crrncy1.grid(row=5, column=0)

#function
lst = Listbox(windows, width = 20)
for i in rates:
    lst.insert(END, str(i))
lst.grid(row=5 , column=6)

#button
btn = Button(windows, text = "Convertor", font=("bold",12), command = convertor)
btn.grid(row=6, column=6)

#label
answer = Label(windows, font = ('bold', 12))
answer.grid(row=8, column=6)


windows.mainloop()
