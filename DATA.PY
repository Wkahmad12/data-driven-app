from tkinter import Tk, ttk, messagebox
from tkinter import *
from PIL import Image, ImageTk
import time
import requests
import re
import json
def open_abt():
    #top level used for create a seprate window
    abt_win = Toplevel(root)
    abt_win.geometry("600x300")
    abt_win.title("About")
    abt_win.configure(bg="darkblue")

    # Add bg image to about window
    abt_image = Image.open('finance-background-lmbrnieyixwr61g9.jpg')
    abt_image = abt_image.resize((600, 300))
    abt_image = ImageTk.PhotoImage(abt_image)
    abt_label = Label(abt_win, image=abt_image)
    abt_label.place(x=0, y=0)

    
    abt_text = '''
    I created the Currency Converter (CC) program, 
    a graphical user interface for which I used Python's 
    Tkinter toolkit. Users may convert currencies using this handy tool,
      which is based on real-time exchange rates 
    from the ExchangeRate-API. The primary window 
    has a visually appealing layout with animated background graphics 
    and all the necessary functions, such as 
    quantity input fields, source and target currency selections, 
    and a "CONVERT" button to start the conversion. When the 
    button is clicked, an API call is made to retrieve 
    the most recent exchange rates, and the converted amount is 
    shown clearly along with the appropriate currency codes.
    '''

    about_label = Label(abt_win, text=abt_text, font=('Arial', 12), bg="darkblue", fg="white", justify="left")
    about_label.pack(pady=20)

    abt_win.mainloop()


root = Tk()
root.geometry("700x400")
root.title('CC')
root.resizable(width=False, height=False)

backg_image = Image.open('finance-background-lmbrnieyixwr61g9.jpg')
backg_image = backg_image.resize((700, 400))
backg_image = ImageTk.PhotoImage(backg_image)
background_label = Label(root, image=backg_image)
background_label.place(x=0, y=0)

top1 = Frame(root, width=700, height=100, bg="darkblue")
top1.grid(row=0, column=0)
frame2 = Frame(root, width=500, height=200)
frame2.grid(row=1, column=0)


#frame 2 for bg image
frame2_image = Image.open('What-is-Forex-Trading.jpg')
frame2_image = frame2_image.resize((700, 400))
frame2_image = ImageTk.PhotoImage(frame2_image)
frame2_background_label = Label(frame2, image=frame2_image)
frame2_background_label.place(x=0, y=27, relwidth=1, relheight=1)
#btn of sign in abd abou
btn = Button(frame2, text="SIGN IN", width=10, height=1, background="darkblue", fg="white", font=("Arial", 10))
btn.place(x=410, y=0)

btn = Button(frame2, text="ABOUT", width=10, height=1, background="darkblue", fg="white", font=("Arial", 10),command=open_abt)
btn.place(x=300, y=0)


#FOR TIME
time_cc = Label(frame2, text="", font=('Arial', 10), fg="black")
time_cc.place(x=0, y=0)

#funtion is used to perform some task and also updates the time
def UP_time():
    current_time = time.strftime("%H:%M:%S")
    time_cc.config(text=current_time)
    root.after(1000, UP_time)


UP_time()

time_frame = Frame(root, width=700, height=100)
time_frame.grid(row=0, column=0)

title = Label(time_frame, text="WK CURRENCY CONVERTER", height=0, pady=30, anchor=CENTER,
              font=('Italic', 12), fg="white", background="darkblue")
title.pack(side="top", fill="both", expand=True)

frame2 = Label(frame2, text="", width=30, height=5, relief=SOLID, pady=7, anchor=CENTER,
               font=('Ivy', 16, 'bold'))
frame2.place(x=50, y=50)

amount = Label(frame2, text="AMOUNT", width=8, height=5, relief=FLAT, pady=0, padx=0, anchor=NW,
               font=('arial', 10, 'bold'))
amount.place(x=0, y=10)
#entry of amount
entry1 = Entry(frame2, width=12, justify=CENTER, relief=SOLID)
entry1.place(x=10, y=55)
#from text 
from_text = Label(frame2, text="FROM", width=8, height=1, relief=FLAT, pady=0, padx=0, anchor=NE,
                  font=('Ivy', 10, 'bold'))
from_text.place(x=120, y=10)
#drop menu of from
combo_from1 = ttk.Combobox(frame2, width=8, justify=CENTER, font=("arial 10 bold"))
currencies = [
    "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF",
    "BMD", "BND", "BOB", "BRL", "BSD", "BTN", "BWP", "BYN", "BZD", "CAD", "CDF", "CHF", "CLP", "CNY", "COP", "CRC", 
    "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "FOK", "GBP", "GEL",
    "GGP", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "IMP", "INR", 
    "IQD", "IRR", "ISK", "JEP", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KID", "KIN", "KRW", "KWD", "KYD", "KZT", 
    "LAK", "LBP", "LKR", "LRD", "LSL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRU", "MUR", "MVR", 
    "MWK", "MXN", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", 
    "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLL", "SOS", 
    "SRD", "SSP", "STN", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TVD", "TWD", "TZS", "UAH", 
    "UGX", "USD", "UYU", "UZS", "VES", "VND", "VUV", "WST", "XAF", "XCD", "XDR", "XOF", "XPF", "YER", "ZAR", "ZMW", 
    "ZWL"
]


combo_from1['value'] = (currencies)
combo_from1.place(x=150, y=55)

to_text = Label(frame2, text="TO", width=8, height=1, relief=FLAT, pady=0, padx=0, anchor=NE,
                font=('Ivy', 10, 'bold'))
to_text.place(x=250, y=10)
#dropdown menu
combo_from = ttk.Combobox(frame2, width=8, justify=CENTER, font=("arial 10 bold"))
combo_from['value'] = (currencies)  
combo_from.place(x=300, y=55)
#convert btn
btn = Button(frame2, text="COVERT", width=10, height=1, background="darkblue", fg="white", font=("arial", 10))
btn.place(x=150, y=100)

rslt_frame = Frame(root, width=500, height=50, bg="white")
rslt_frame.grid(row=2, column=0)

rslt_label = Label(rslt_frame, text="Result:", font=('arial', 12, 'bold'), bg="white")
rslt_label.place(x=10, y=10)
rslt_label = Label(rslt_frame, text="", font=('arial', 12, 'bold'),bg=("white"))
rslt_label.place(x=100, y=10)

convertion = {}

def currency_convertor():

    # get input from user
    try:
        amount = entry1.get()
        from_text = combo_from1.get()
        to_text = combo_from.get()

        # NUMERIC PART
        amount = float(re.sub(r'[^\d.]', '', amount))
      # api url provided by tutor
        url = f"https://api.exchangerate-api.com/v4/latest/{from_text}"
        response = requests.get(url)
        data = response.json()

        print("API Response:", data)  # Debugging line

        # IF RATE KEY DATA EXIST
        if 'rates' in data:
            exchange_rate = data['rates'].get(to_text, 0)
            # Calculation of converted amount
            converted_amount = amount * exchange_rate
            # for result update 
            result_text = f"{amount} {from_text} = {converted_amount:.2f} {to_text}"
            rslt_label.config(text=result_text)

             # to store detail in dictionry
            convertion["timestamp"] = time.strftime("%Y-%m-%d %H:%M:%S")
            convertion["from"] = from_text
            convertion["to"] = to_text
            convertion["amount"] = amount
            convertion["Amount_converted"] = converted_amount

            #add conversation detail to json file
            with open("RESULT_DETAIL.json", "a") as json_file:
                json.dump(convertion, json_file, indent=2)

        else:
            rslt_label.config(text="Invalid API")
    except ValueError:
        rslt_label.config(text="please enter valid number.")
# to call currency  convertor to do its function
btn.config(command=currency_convertor)

if __name__ == "__main__":
    root.mainloop()