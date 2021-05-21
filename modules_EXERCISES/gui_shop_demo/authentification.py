import json

from tkinter import Button, Entry, Label
from modules_EXERCISES.gui_shop_demo.canvas import tk
from modules_EXERCISES.gui_shop_demo.helpers import clean_screen
from modules_EXERCISES.gui_shop_demo.products import render_products


def login(username, password):
    with open("db/users_credentials.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            user, pass_ = line[:-1].split(", ")
            if user == username and pass_ == password:
                with open("db/current_user.txt", "w") as current_user_file:
                    current_user_file.write(user)
                render_products()
                return

        render_login(errors=True)


def register(**user):
    user.update({"products": []})
    with open("db/users.txt", "a") as file:
        file.write(json.dumps(user))
        file.write("\n")

    with open("db/users_credentials.txt", "a") as file:
        file.write(f"{user.get('username')}, {user.get('password')}")
        file.write("\n")

    render_login()

def render_login(errors=None):
    clean_screen()
    Label(text= "Enter your username").grid(row=0,column=1)
    username = Entry(tk)
    username.grid(row=0, column=0)
    Label(text="Enter your password").grid(row=1, column=1)
    password = Entry(tk, show="*")
    password.grid(row=1, column=0)
    Button(tk, text="Enter", bg="purple", fg="white",\
           command= lambda: login(username.get(), password.get())).grid(row=2, column=0)
    if errors:
        Label(text="Invalid username or password").grid(row=3, column=0)


def render_register():
    clean_screen()
    username = Entry(tk)
    username.grid(row=0, column=0)
    password = Entry(tk, show="*")
    password.grid(row=1, column=0)
    first_name = Entry(tk)
    first_name.grid(row=2, column=0)
    last_name = Entry(tk)
    last_name.grid(row=3, column=0)
    Button(tk, text="Register", bg="purple", fg="white", command= lambda:\
        register(username=username.get(), \
                 password=password.get(), \
                 first_name=first_name.get(), \
                 last_name=last_name.get())).grid(row=4, column=0)


def render_main_enter_screen():
    Button(tk, text="Login", bg="green", fg= "white", command=render_login).grid(row=0, column=0)
    Button(tk, text="Register", bg="yellow", fg="black", command=render_register).grid(row=0, column=1)

