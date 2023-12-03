import tkinter as tk
from tkinter import *
from tkinter import ttk
from datetime import datetime
import requests
from PIL import ImageTk, Image
from tkinter import  messagebox

root = tk.Tk()
root.title('Currency Converter')
root.geometry('700x500')
root.resizable(False,False)

image = Image.open('bannerimg-removebg-preview.png')
zoom = 0.3

pixcel_x,pixcel_y = tuple([int(zoom * x) for x in image.size])

img = ImageTk.PhotoImage(image.resize((pixcel_x,pixcel_y)))
panel = Label(root, image = img)
panel.place(x=280,y=40)


def show_data():
    amount = E1.get()
    from_currency = c1.get()
    to_currency = c2.get()
    api_key = '607a349d72af2e3c9d08cb57f54be597'  # Replace with your own API key
    url = f'https://open.er-api.com/v6/latest/{from_currency}?apikey={api_key}'

    if amount == '':
        messagebox.showerror("Currency Converter", "Please Enter The Amount")
    elif to_currency == '':
        messagebox.showerror("Currency Converter", "Please Choose Currency")
    else:
        data = requests.get(url).json()
        currency = to_currency.strip()
        amount = int(amount)
        cc = data['rates'][currency]
        cur_conv = cc * amount
        E2.insert(0, cur_conv)
        text.insert('end',f'{amount} United States Dollar Equals to :{cur_conv} {to_currency}\n Last Time Update --- \t {datetime.now()}\n\n')


def clear():
    E1.delete(0,'end')
    E2.delete(0,'end')
    text.delete(1.0,'end')

l1 = Label(root, text="USD Currency Convertor Using Python", font=('verdana',12,'bold'))
l1.place(x=170,y=15)

amt = Label(root, text="Amount", font=('roboto',12,'bold'))
amt.place(x=40,y=55)

E1 = Entry(root, width=20,borderwidth=1,font=('roboto',12,'bold'))
E1.place(x=40,y=80)

c1 = tk.StringVar()
c2 = tk.StringVar()
currencychoose1 = ttk.Combobox(root, width=15, textvariable= c1, state='readonly', font=('verdana',12,'bold'))
currencychoose1['values'] = (
                            'USD',
                            )
currencychoose1.place(x=440, y=80)
currencychoose1.current(0)

E2 = Entry(root, width=20, borderwidth=1, font=('roboto',12,'bold'))
E2.place(x=40, y=115)

currencychoose2 = ttk.Combobox(root, width=15, textvariable=c2, state='readonly', font=('verdana',12, 'bold'))
currencychoose2['values'] = (
'ALL', 'AED', 'AFN', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTN', 'BWP', 'BYN', 'BZD', 'CAD', 'CDF', 'CHF', 'CLP', 'CNY', 'COP', 'CRC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'FOK', 'GEL', 'GBP', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KID', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRU', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLL', 'SOS', 'SPL', 'SRD', 'STN', 'SVC', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TVD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS', 'VES', 'VND', 'VUV', 'WST', 'XAF', 'XCD', 'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMW', 'ZWL'
)
currencychoose2.place(x=440, y= 115)

text = Text(root, height=15, width=56, font=('verdana', '10','bold'))
text.place(x=100, y=210)

B = Button(root, text='Search',command=show_data, font=('verdana','10','bold'), bg='red')
B.place(x=300,y=170)

clear = Button(root,text="Clear",command=clear, font=('verdana','10','bold'), bg='green')
clear.place(x=300,y=465)

root.mainloop()
