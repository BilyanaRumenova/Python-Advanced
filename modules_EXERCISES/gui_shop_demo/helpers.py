from modules_EXERCISES.gui_shop_demo.canvas import tk


def clean_screen():
    for el in tk.grid_slaves():
        el.destroy()