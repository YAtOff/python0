import json
import tkinter as tk
from tkinter import ttk


def load_rates():
    with open("currency.json") as file:
        return json.load(file)["rates"]


rates = load_rates()
currencies = list(rates.keys())


def convert_currency(amount, from_currency, to_currency):
    return amount * rates[to_currency] / rates[from_currency]


window = tk.Tk()
window.geometry("350x200")


def clalulate_currency():
    ammount = int(ammount_entry.get())
    from_currency = from_combo.get()
    to_currency = to_combo.get()
    result = convert_currency(ammount, from_currency, to_currency)
    result_label.configure(text=str(result))


tk.Label(window, text="From:").grid(column=0, row=0)
from_combo = ttk.Combobox(window)
from_combo["values"] = currencies
from_combo.current(currencies.index("BGN"))
from_combo.grid(column=1, row=0)

tk.Label(window, text="To:").grid(column=0, row=1)
to_combo = ttk.Combobox(window)
to_combo["values"] = currencies
to_combo.current(currencies.index("USD"))
to_combo.grid(column=1, row=1)

tk.Label(window, text="Ammount:").grid(column=0, row=2)
ammount_entry = tk.Entry(window, width=10)
ammount_entry.grid(column=1, row=2)

tk.Button(window, text="Calculate", command=clalulate_currency).grid(column=0, row=3)

result_label = tk.Label(window, text="")
result_label.grid(column=3, row=0, columnspan=4)

window.mainloop()
