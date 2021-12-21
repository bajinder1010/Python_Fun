import tkinter

def change_color():
    window.configure(background="white")

window = tkinter.Tk()
window.geometry("800x200")
window.title("My first python GUI")
window.configure(background="grey")
white = tkinter.Button(window, text="Click", command=change_color)
white.pack()
window.mainloop()