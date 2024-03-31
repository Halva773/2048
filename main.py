import tkinter as tk
import random

class Game2048(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("2048")
        self.master.geometry("400x400") # Размер окна
        self.grid()
        self.create_widgets()
        self.master.bind("<Up>", self.move_up)
        self.master.bind("<Down>", self.move_down)
        self.master.bind("<Left>", self.move_left)
        self.master.bind("<Right>", self.move_right)

    def create_widgets(self):
        # Создание сетки 4x4
        self.cells = []
        for i in range(4):
            row = []
            for j in range(4):
                cell = tk.Label(self, text="", width=5, height=2, bg="lightgray", font=("Arial", 20, "bold"))
                cell.grid(row=i, column=j, padx=5, pady=5)
                row.append(cell)
            self.cells.append(row)
        self.add_random_value()

    def set_cell_value(self, row, col, value):
        # Установка значения и цвета клетки (строка, столбец)
        self.cells[row][col].config(text=str(value))

        # Установка цвета клетки в зависимости от значения
        colors = {
            2: "lightblue",
            4: "blue",
            8: "lightgreen",
            16: "green",
            32: "lightyellow",
            64: "yellow",
            128: "orange",
            256: "red",
            512: "lightpink",
            1024: "pink",
            2048: "purple"
        }
        cell_color = colors.get(value, "lightgray")
        self.cells[row][col].config(bg=cell_color)

    def gen_value(self):
        # Генерация нового значения для клетки (2 с вероятностью 90%, 4 с вероятностью 10%)
        return 4 if random.random() < 0.1 else 2

    def add_random_value(self):
        # Добавление нового значения на случайную пустую клетку
        empty_cells = [(i, j) for i in range(4) for j in range(4) if self.cells[i][j]['text'] == ""]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.set_cell_value(row, col, self.gen_value())

    def can_move_up(self):
        # Проверка возможности движения клеток вверх
        for j in range(4):
            for i in range(1, 4):
                if self.cells[i][j]['text'] != "" and (self.cells[i - 1][j]['text'] == "" or self.cells[i - 1][j]['text'] == self.cells[i][j]['text']):
                    return True
        return False

    def can_move_down(self):
        # Проверка возможности движения клеток вниз
        for j in range(4):
            for i in range(2, -1, -1):
                if self.cells[i][j]['text'] != "" and (self.cells[i + 1][j]['text'] == "" or self.cells[i + 1][j]['text'] == self.cells[i][j]['text']):
                    return True
        return False

    def can_move_left(self):
        # Проверка возможности движения клеток влево
        for i in range(4):
            for j in range(1, 4):
                if self.cells[i][j]['text'] != "" and (self.cells[i][j - 1]['text'] == "" or self.cells[i][j - 1]['text'] == self.cells[i][j]['text']):
                    return True
        return False

    def can_move_right(self):
        # Проверка возможности движения клеток вправо
        for i in range(4):
            for j in range(2, -1, -1):
                if self.cells[i][j]['text'] != "" and (self.cells[i][j + 1]['text'] == "" or self.cells[i][j + 1]['text'] == self.cells[i][j]['text']):
                    return True
        return False

    def move_up(self, event):
        # Движение клеток вверх
        if self.can_move_up():
            for j in range(4):
                merged = [False] * 4
                for i in range(1, 4):
                    if self.cells[i][j]['text'] != "":
                        for k in range(i, 0, -1):
                            if self.cells[k - 1][j]['text'] == "":
                                self.set_cell_value(k - 1, j, self.cells[k][j]['text'])
                                self.set_cell_value(k, j, "")
                            elif self.cells[k - 1][j]['text'] == self.cells[k][j]['text'] and not merged[k - 1]:
                                self.set_cell_value(k - 1, j, int(self.cells[k][j]['text']) * 2)
                                self.set_cell_value(k, j, "")
                                merged[k - 1] = True
                                break
                            else:
                                break
            self.after(100, self.add_random_value)

    def move_down(self, event):
        # Движение клеток вниз
        if self.can_move_down():
            for j in range(4):
                merged = [False] * 4
                for i in range(2, -1, -1):
                    if self.cells[i][j]['text'] != "":
                        for k in range(i, 3):
                            if self.cells[k + 1][j]['text'] == "":
                                self.set_cell_value(k + 1, j, self.cells[k][j]['text'])
                                self.set_cell_value(k, j, "")
                            elif self.cells[k + 1][j]['text'] == self.cells[k][j]['text'] and not merged[k + 1]:
                                self.set_cell_value(k + 1, j, int(self.cells[k][j]['text']) * 2)
                                self.set_cell_value(k, j, "")
                                merged[k + 1] = True
                                break
            self.after(100, self.add_random_value)

    def move_left(self, event):
        # Движение клеток влево
        if self.can_move_left():
            for i in range(4):
                merged = [False] * 4
                for j in range(1, 4):
                    if self.cells[i][j]['text'] != "":
                        for k in range(j, 0, -1):
                            if self.cells[i][k - 1]['text'] == "":
                                self.set_cell_value(i, k - 1, self.cells[i][k]['text'])
                                self.set_cell_value(i, k, "")
                            elif self.cells[i][k - 1]['text'] == self.cells[i][k]['text'] and not merged[k - 1]:
                                self.set_cell_value(i, k - 1, int(self.cells[i][k]['text']) * 2)
                                self.set_cell_value(i, k, "")
                                merged[k - 1] = True
                                break
            self.after(100, self.add_random_value)

    def move_right(self, event):
        # Движение клеток вправо
        if self.can_move_right():
            for i in range(4):
                merged = [False] * 4
                for j in range(2, -1, -1):
                    if self.cells[i][j]['text'] != "":
                        for k in range(j, 3):
                            if self.cells[i][k + 1]['text'] == "":
                                self.set_cell_value(i, k + 1, self.cells[i][k]['text'])
                                self.set_cell_value(i, k, "")
                            elif self.cells[i][k + 1]['text'] == self.cells[i][k]['text'] and not merged[k + 1]:
                                self.set_cell_value(i, k + 1, int(self.cells[i][k]['text']) * 2)
                                self.set_cell_value(i, k, "")
                                merged[k + 1] = True
                                break
            self.after(100, self.add_random_value)

if __name__ == "__main__":
    root = tk.Tk()
    app = Game2048(master=root)
    app.mainloop()
