
import tkinter as tk


def search_weather():
    city = city_entry.get()

    if city == "":
        weather_label.config(text="Nejdřív zadej město!")
    else:
        weather_label.config(text=f"Hledám počasí pro: {city}")



root = tk.Tk()


root.title("Weather App")
root.geometry("600x400")
root.resizable(False, False)


title_label = tk.Label(
    root,
    text="Weather App",
    font=("Arial", 24, "bold")
)
title_label.pack(pady=20)


city_label = tk.Label(
    root,
    text="Zadej název města:",
    font=("Arial", 12)
)
city_label.pack(pady=5)


city_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=25
)
city_entry.pack(pady=10)


search_button = tk.Button(
    root,
    text="Zjistit počasí",
    font=("Arial", 12),
    command=search_weather
)
search_button.pack(pady=10)


weather_label = tk.Label(
    root,
    text="Zadej město a zjisti počasí",
    font=("Arial", 14)
)
weather_label.pack(pady=20)


root.mainloop()
