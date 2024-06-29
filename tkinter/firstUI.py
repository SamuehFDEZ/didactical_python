# python nased gui framework that is built in a standar library and is
# readily available
# this is like javafx, to build desktop apps
import tkinter as tk

main_window = tk.Tk()
main_window.title('My first GUI')
main_window.geometry('500x500')
# minimum size
main_window.minsize(200, 100)
# maximum size
main_window.maxsize(1000, 700)
# label
label = tk.Label(main_window, text='My first GUI', bg='red', fg='black',
                 padx=100, pady=100)
label.pack(side=tk.LEFT)
label.grid(row=1, column=0, columnspan=2)

#img
img = tk.PhotoImage(file="yourimage.png")
label1 = tk.Label(image=img)
label1.pack(side=tk.RIGHT)
label1.grid(row=1, column=0, columnspan=2)





main_window.mainloop()