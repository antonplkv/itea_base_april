from tkinter import Tk, Toplevel, Button, Label, Entry, Text, END



root = Tk()

# txt = Text(height=10, width=256)


def get_name():
    label.configure(text=entry.get())
    entry.delete(2, 4)


entry = Entry(width=256, font='Arial 20')
label = Label(text='Введите свое имя и нажмите на кнопку', font='Arial 20')
button = Button(root,
                text='Нажми на меня!',
                fg='red',
                bg='white',
                width=600,
                height=10,
                command=get_name
                )

root.title('Itea-Lesson-7')
root.geometry('600x400')

label.pack()
button.pack()
entry.pack(side='bottom')
root.mainloop()