import requests
from PIL import Image
from io import BytesIO
import tkinter as tk
from tkinter import ttk

def show_image():
    user_input = animal_var.get()

    if user_input == 'cats':
        url = f'http://shibe.online/api/cats?count=1&urls=true&httpsUrls=true'
    elif user_input == 'birds':
        url = f'http://shibe.online/api/birds?count=1&urls=true&httpsUrls=true'
    elif user_input == 'shibes':
        url = f'http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        url = data[0]
        response = requests.get(url)
        pic = Image.open(BytesIO(response.content))
        pic.show()
    else:
        print('idk')

root = tk.Tk()
root.title('Animal Image Generator')

animal_frame = ttk.LabelFrame(root, text='Select an Animal:')
animal_frame.grid(column=0, row=0, padx=10, pady=10, sticky='w')

animal_var = tk.StringVar()
animal_var.set('cats')

cat_radio = ttk.Radiobutton(animal_frame, text='Cats', variable=animal_var, value='cats')
cat_radio.grid(column=0, row=0, padx=10, pady=5, sticky='w')

bird_radio = ttk.Radiobutton(animal_frame, text='Birds', variable=animal_var, value='birds')
bird_radio.grid(column=0, row=1, padx=10, pady=5, sticky='w')

dog_radio = ttk.Radiobutton(animal_frame, text='Dogs (Shibes)', variable=animal_var, value='shibes')
dog_radio.grid(column=0, row=2, padx=10, pady=5, sticky='w')

show_button = ttk.Button(root, text='Show Image', command=show_image)
show_button.grid(column=0, row=1, padx=10, pady=10, sticky='w')

root.mainloop()