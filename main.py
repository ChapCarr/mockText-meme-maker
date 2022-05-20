import tkinter as tk
from PIL import ImageTk,Image

def makeMock():
    og = user_input.get()
    new_word = " "
    index = 0
    for i in og:
        if (index % 2) == 0:
            downers = og[index].lower()
            new_word = new_word + downers
        else:
            uppers = og[index].upper()
            new_word = new_word + uppers
        index = index + 1
    if len(new_word)< 12:
        myimg_label.config(text=new_word)
    elif 24 > len(new_word) >= 12:
        first_half = new_word[:len(new_word) // 2]
        second_half = new_word[len(new_word) // 2:]
        format_word = first_half + "\n" + second_half
        myimg_label.config(text=format_word)
    elif 48 > len(new_word) >= 24:
        myimg_label.config(font=("arial", "48"))
        first_half = new_word[:len(new_word) // 2]
        second_half = new_word[len(new_word) // 2:]
        format_word = first_half + "\n" + second_half
        myimg_label.config(text=format_word)


root = tk.Tk()
root.geometry("500x550")
root.title("Mockery")
root.iconbitmap("")
# Title for gui
title = tk.Label(root, text="Enter your text below:")
title.pack()

# Entry Widget for user input
user_input = tk.Entry(root)
user_input.pack()

# Submit button
button = tk.Button(root,text="Submit" ,command=makeMock)
button.pack()

#img import and pack
img = ImageTk.PhotoImage(Image.open("/Users/chapcarr/Desktop/Code/mockText/Mocking-Spongebob.jpg"))
myimg_label = tk.Label(root, image=img, compound="center")
myimg_label.configure(font=("Arial", "64"), fg="black")
myimg_label.pack()

root.mainloop()


