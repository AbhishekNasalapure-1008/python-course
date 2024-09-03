# from tkinter import *
# import requests

# def get_quote():
#     response = requests.get('https://api.kanye.rest')
#     response.raise_for_status()
#     data = response.json()['quote']
#     canvas.itemconfig(quote_text, text=data)
#     # print(data)


# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)

# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="background.jpeg")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="", width=250, font=("Arial", 30, "bold"), fill="white")
# canvas.grid(row=0, column=0)

# kanye_img = PhotoImage(file="kanye.jpeg")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)

# window.mainloop()

from tkinter import *
from PIL import Image, ImageTk
import requests

def get_quote():
    response = requests.get('https://api.kanye.rest')
    response.raise_for_status()
    data = response.json()['quote']
    canvas.itemconfig(quote_text, text=data)
    # print(data)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = Image.open("background.jpeg")
background_img = ImageTk.PhotoImage(background_img)
canvas.create_image(150, 207, image=background_img)
canvas.image = background_img  # keep a reference to prevent garbage collection
quote_text = canvas.create_text(150, 207, text="", width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = Image.open("kanye.jpeg")
kanye_img = ImageTk.PhotoImage(kanye_img)
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.image = kanye_img  # keep a reference to prevent garbage collection
kanye_button.grid(row=1, column=0)

window.mainloop()