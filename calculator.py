
from tkinter import *
from datetime import *
import random
import math
from tkinter import font


class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title('Advanced Calculator')
        self.dimesions()
        self.data()
        self.widgets()
        self.button_layout()
        self.clock_n_color()
        self.calculate_rad()

    def dimesions(self):
        self.master.update()
        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()

        self.window_width = int(self.screen_width * 0.75)
        self.window_height = int(self.screen_height * 0.85)

        x = (self.screen_width - self.window_width) // 2
        y = (self.screen_height - self.window_height) // 2

        self.master.geometry(
            f'{self.window_width}x{self.window_height}+{x}+{y}')

    def data(self):
        self.HEIGHT, self.WIDTH = 2, 4
        self.OBJ = []
        self.row, self.col = 3, 0
        self.label_var = StringVar()
        self.BACKGROUND = '#000'
        self.FOREGROUND = '#fff'
        self.BUTTON_DATA = {
            "basic": [
                "√", "π", "^", "!",
                "(", ")", "%", "/",
                "7", "8", "9", "*",
                "4", "5", "6", "-",
                "1", "2", "3", "+",
                "0", ".", "←", "=", "AC"
            ],
            "advance": ["RAD", "sin", "cos", "tan", "INV", "In", "e", "log"]
        }
        self.COLORS = [
            "sky blue", "orange", "green", "blue", "red",
            "violet", "grey", "maroon", "white smoke", "magenta",
            "yellow", "cyan", 'Turquoise', 'purple', 'Crimson',
            'pink', 'indigo', 'gold', 'olive', 'silver', 'navy',
            'teal', 'lime', 'white', 'skyblue', "#d97b60",
            "#febbd9", "#b02466", "#d6430b", "#7c430b"
        ]
        self.EQUATION = ""
        self.ADVANCED_MODE = False
        self.FONT = {
            'palatino': ('palatino', 12, 'italic')
        }

    def widgets(self):
        # HEADER -> LABEL WIDGET
        self.dancing_script_font = font.Font(family='Dancing Script', size=15)
        self.date_font = font.Font(family="courier new", size=14)

        self.title_label = Label(self.master, text="RAYN CODES CALCULATOR",
                                 font=self.dancing_script_font, bg=self.BACKGROUND)
        self.title_label.grid(column=0, row=0, columnspan=4)

        self.dt_label = Label(self.master, text="",
                              font=self.date_font, bg=self.BACKGROUND)
        self.dt_label.grid(column=0, row=1, columnspan=4)

        self.res_label = Label(self.master, textvariable=self.label_var,
                               font=self.FONT['palatino'], bg=self.BACKGROUND)
        self.res_label.grid(column=0, row=2, columnspan=4)

        # BUTTONS

        for char in self.BUTTON_DATA["basic"]:
            btn = Button(
                self.master, text=char, font=self.FONT['palatino'],
                relief="flat", bd=10, highlightthickness=0, highlightbackground=self.BACKGROUND,
                command=lambda c=char: self.button_click(c), width=self.WIDTH,
                activebackground=self.BACKGROUND, fg=self.FOREGROUND, height=self.HEIGHT, bg=self.BACKGROUND
            )
            btn.grid(column=self.col, row=self.row, sticky="news")
            self.OBJ.append(btn)
            self.col += 1
            if self.col > 3:
                self.col = 0
                self.row += 1

        self.advance_btn = Button(
            self.master, text="↑", font=self.FONT['palatino'], width=self.WIDTH, height=self.HEIGHT, bg=self.BACKGROUND,
            highlightthickness=0, highlightbackground=self.BACKGROUND, activebackground=self.BACKGROUND, relief="flat",
            command=self.toggle_advance_mode
        )
        self.advance_btn.grid(row=9, column=1)

        self.exit_btn = Button(
            self.master, text="OFF", font=self.FONT['palatino'], width=self.WIDTH, height=self.HEIGHT, bg=self.BACKGROUND,
            highlightthickness=0, highlightbackground=self.BACKGROUND, relief="flat",
            activebackground=self.BACKGROUND, command=self.master.destroy
        )
        self.exit_btn.grid(row=9, column=2)

        self.history = Text(self.master, font=self.FONT['palatino'], width=self.WIDTH, height=self.HEIGHT, bg="black", fg=self.FOREGROUND,
                            highlightthickness=0, highlightbackground=self.BACKGROUND, relief="flat")
        self.history.grid(row=9, column=3)

        self.history.tag_configure("right", justify="right")

    def button_layout(self):
        for i in range(7):
            self.master.grid_rowconfigure(i, weight=1)

        for i in range(5):
            self.master.grid_columnconfigure(i, weight=1)

    def change_color(self):
        random_color = random.choice(self.COLORS)
        self.dt_label.config(fg=random_color)
        self.master.config(bg=self.BACKGROUND)
        self.advance_btn.config(fg=random_color)
        self.exit_btn.config(fg=random_color)
        self.res_label.config(fg=random_color)
        self.title_label.config(fg=random_color)
        for b in self.OBJ:
            b.config(fg=random_color)
        self.master.after(1000, self.change_color)

    def update_clock(self):
        current = datetime.now()
        timedate = current.strftime("%a %d-%b-%Y\n %H:%M:%S %p")
        self.dt_label.config(text=timedate)
        self.master.after(1000, self.update_clock)

    def button_click(self, char):
        if char == "=":
            try:
                result = eval(self.EQUATION)
                self.label_var.set(result)
                self.history.insert(END, self.EQUATION +
                                    " = " + str(result) + "\n")
                self.EQUATION = str(result)
            except ZeroDivisionError:
                self.label_var.set("Error: Division by Zero")
            except SyntaxError:
                self.label_var.set("Error: Invalid Input")

        elif char == "√":
            try:
                res = float(self.EQUATION)
                value = str(math.sqrt(res))
                self.label_var.set(value)
                self.EQUATION = value
            except:
                self.label_var.set("Invalid Input")

        elif char == "π":
            res = float(self.EQUATION)
            value = str(math.pi)
            self.EQUATION = value
            self.label_var.set(value)
            self.EQUATION = ""
        elif char == "AC":
            self.EQUATION = ""
            self.label_var.set("")
            self.history.delete(1.0, END)
        elif char == "←":
            self.EQUATION = self.EQUATION[:-1]
            self.label_var.set(self.EQUATION)
        else:
            self.EQUATION += str(char)
            self.label_var.set(self.EQUATION)

    def toggle_advance_mode(self):
        self.ADVANCED_MODE = not self.ADVANCED_MODE
        self.update_button_labels()

    def update_button_labels(self):
        # button_labels = advance if advance_mode else basic
        if self.ADVANCED_MODE:
            for i, label in enumerate(self.BUTTON_DATA["advance"]):
                self.OBJ[i].config(text=label)
        else:
            for i, label in enumerate(self.BUTTON_DATA["basic"]):
                self.OBJ[i].config(text=label)

    def calculate_rad(self):
        try:
            if self.EQUATION == "RAD":
                radians = float(self.EQUATION)
                value = str(math.radians(radians))
                self.label_var.set(value)
                self.EQUATION = ""
                self.update_button_labels()

            elif self.EQUATION == "sin":
                Sin = float(self.EQUATION)
                value = str(math.sin(Sin))
                self.label_var.set(value)
                self.EQUATION = ""
                self.update_button_labels()

            elif self.EQUATION == "cos":
                Cos = float(self.EQUATION)
                value = str(math.cos(Cos))
                self.label_var.set(value)
                self.EQUATION = ""
                self.update_button_labels()
        except ValueError:
            self.label_var.set("Invalid Input")

    def clock_n_color(self):
        self.master.after(1000, self.update_clock)
        self.master.after(1000, self.change_color)


if __name__ == '__main__':
    window = Tk()
    calculator = Calculator(window)
    window.mainloop()
