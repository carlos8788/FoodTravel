from tkinter import Tk, Label, Entry, messagebox, CENTER, Button
import config as cf

class Login:
    def __init__(self):
        self.master = Tk()
        self.master.config(background=cf.PRIMARY_COLOR)
        self.master.geometry('400x600')

        self.title = Label(
            text="Login", background=cf.PRIMARY_COLOR,
            font=cf.PRIMARY_FONT,
            foreground=cf.SECONDARY_COLOR,
            justify=CENTER
        )
        self.title.place(relx=0.5, rely=0.3, anchor='center')

        self.entry = Entry(self.master)
        self.entry.insert(0, 'Ingrese su usuario acá...')
        self.entry.bind('<FocusIn>', self.on_entry_click)
        self.entry.bind('<FocusOut>', self.on_focusout)
        self.entry.config(
            font='Arial 13',
            foreground='black',
            width=40
        )
        self.entry.place(relx=0.5, rely=0.4, anchor='center')

        self.password = Entry(self.master)
        self.password.insert(0, 'Ingrese su contraseña acá...')
        self.password.bind('<FocusIn>', self.on_password_click)
        self.password.bind('<FocusOut>', self.on_focusout)
        self.password.config(
            font='Arial 13',
            foreground='black',
            width=40
        )
        self.password.place(relx=0.5, rely=0.5, anchor='center')

        self.login_button = Button(
            self.master,
            text="Iniciar sesión",
            foreground=cf.SECONDARY_COLOR,
            font=cf.SECONDARY_FONT,
            background='green',
            borderwidth=0,
            relief='ridge',
            command=self.check_login)
        self.login_button.place(relx=0.5, rely=0.6, anchor='center')

        self.master.mainloop()

    def on_entry_click(self, event):
        event.widget.delete(0, "end")
        event.widget.insert(0, '')
        event.widget.config(fg = 'black')

    def on_password_click(self, event):
        event.widget.delete(0, "end")
        event.widget.insert(0, '')
        event.widget.config(fg = 'black', show="*")

    def on_focusout(self, event):
        if event.widget.get() == '':
            if event.widget == self.entry:
                event.widget.insert(0, 'Ingrese su usuario acá...')
            else:
                event.widget.insert(0, 'Ingrese su contraseña acá...')
                event.widget.config(show="")
            event.widget.config(fg = 'grey')

    def check_login(self):
        if self.entry.get() == 'admin' and self.password.get() == '123456':
           print('Soy admin')




if __name__ == "__main__":
    Login()