from tkinter import Tk, Entry, StringVar, Frame, Button

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            value = eval(screen.get())
            screen_value.set(value)
        except Exception:
            screen_value.set("Error")
    elif text == "C":
        screen_value.set("")
    else:
        screen_value.set(screen_value.get() + text)

# Create the main window
cal = Tk()
cal.geometry("400x560")
cal.title("Super Calculator")

# Screen
screen_value = StringVar()
screen_value.set("")
screen = Entry(cal, font="lucida 45 bold", bg="lightblue", textvariable=screen_value)
screen.pack(pady=10, fill="x", padx=10)

# Button Frame
button_frame = Frame(cal)
button_frame.pack()

# Buttons
button_texts = [
    ("C", 1, 0), ("*", 1, 1), ("=", 1, 2), ("/", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("+", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("0", 4, 3)
]

for (text, row, col) in button_texts:
    button = Button(button_frame, text=text, font="lucida 25 bold", padx=20, pady=20, bg="grey")
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind('<Button-1>', click)

# Start the Tkinter event loop
cal.mainloop()
