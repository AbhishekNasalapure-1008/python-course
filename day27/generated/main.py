import tkinter as tk

def convert_km_to_miles():
    kilometers = float(entry_km.get())
    miles = kilometers * 0.621371
    label_result.config(text=f"{kilometers} kilometers is equal to {miles:.2f} miles")

root = tk.Tk()
root.title("Kilometers to Miles Converter")

label_km = tk.Label(root, text="Enter distance in kilometers:")
label_km.pack(pady=10)

entry_km = tk.Entry(root)
entry_km.pack(pady=5)

button_convert = tk.Button(root, text="Convert", command=convert_km_to_miles)
button_convert.pack(pady=10)

label_result = tk.Label(root, text="")
label_result.pack(pady=10)

root.mainloop()