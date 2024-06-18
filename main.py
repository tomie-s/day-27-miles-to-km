from tkinter import *


def miles_to_km():
    dist_in_km = round(float(user_input.get()) * 1.609, 2)
    answer_txt.config(text=f'{str(dist_in_km)}')


# Screen or window setup
window = Tk()
window.title('Miles to KM Converter')
window.minsize(width=200, height=200)
window.config(padx=20, pady=40)

# Entry component
user_input = Entry(width=8)
user_input.grid(column=1, row=0)

# Labels for screen
miles_txt = Label(text='Miles')
miles_txt.grid(column=2, row=0)

equals_txt = Label(text='is equals to')
equals_txt.grid(column=0, row=1)

answer_txt = Label(text='0')
answer_txt.grid(column=1, row=1)

km_txt = Label(text='Km')
km_txt.grid(column=2, row=1)

# Button component
button = Button(text='Calculate', command=miles_to_km)
button.grid(column=1, row=2)


window.mainloop()
