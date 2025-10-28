import tkinter as tk
import colors as c
import random

#fibonacci nums for 4x4: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987
# fibonacci cache for a 4x4 board
FIB_LIST = [1, 1]
for i in range(2, 16):  # 4x4 = 16 tiles
    FIB_LIST.append(FIB_LIST[i - 1] + FIB_LIST[i - 2])
FIB_SET = set(FIB_LIST)
FIB_INDEX = {FIB_LIST[i]: i for i in range(len(FIB_LIST))}

class Game(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("2048")

        self.main_grid = tk.Frame(
            self, bg = c.GRID_COLOR, bd=3, width = 600, height = 600
        )
        self.main_grid.grid(pady=(100,0))
        self.make_GUI()
        self.start_game()

        self.master.bind("<Left>", self.left)
        self.master.bind("<Right>", self.right)
        self.master.bind("<Up>", self.up)
        self.master.bind("<Down>", self.down)

        self.mainloop()

    def make_GUI(self):
        #make grid
        self.cells = []
        for i in range(4):
            row = []
            for j in range(4):
                cell_frame = tk.Frame(
                    self.main_grid,
                    bg=c.EMPTY_CELL_COLOR,
                    width = 150,
                    height=150
                )
                cell_frame.grid(row=i, column=j, padx=5, pady=5)
                cell_number = tk.Label(self.main_grid, bg = c.EMPTY_CELL_COLOR)
                cell_number.grid(row = i, column = j)
                cell_data = {"frame": cell_frame, "number": cell_number}
                row.append(cell_data)
            self.cells.append(row)
        
        #make score header
        score_frame = tk.Frame(self)
        score_frame.place(relx=0.5, y=45, anchor="center")
        tk.Label(
            score_frame,
            text="Score",
            font=c.SCORE_LABEL_FONT
        ).grid(row=0)
        self.score_label = tk.Label(score_frame, text="0", font =c.SCORE_FONT)
        self.score_label.grid(row=1)

    def start_game(self):
        #matrix of zeros
        self.matrix = [[0]*4 for _ in range(4)]
        #fill 2 random cells with 1s
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        self.matrix[row][col] = 1
        self.cells[row][col]["frame"].configure(bg=c.CELL_COLORS[1])
        self.cells[row][col]["number"].configure(
            bg=c.CELL_COLORS[1],
            fg=c.CELL_NUMBER_COLORS[1],
            font=c.CELL_NUMBER_FONTS[1],
            text="1"
        )
        while(self.matrix[row][col]!=0):
            row = random.randint(0,3)
            col = random.randint(0,3)
        self.matrix[row][col] = 2
        self.cells[row][col]["frame"].configure(bg=c.CELL_COLORS[2])
        self.cells[row][col]["number"].configure(
            bg=c.CELL_COLORS[2],
            fg=c.CELL_NUMBER_COLORS[2],
            font=c.CELL_NUMBER_FONTS[2],
            text="2"
        )

        self.score = 0

    def stack(self):
        new_matrix = [[0]*4 for _ in range(4)]
        for i in range(4):
            fill_position = 0
            for j in range(4):
                if self.matrix[i][j] != 0:
                    new_matrix[i][fill_position] = self.matrix[i][j]
                    fill_position +=1
        self.matrix = new_matrix
    #all numbers slide left, and all zeros move to the right.

    def combine(self):
        for i in range(4):
            new_row, hold = [], -1
            for val in self.matrix[i]:
                if not val: 
                    continue
                if hold == -1:
                    hold = val
                elif abs(FIB_INDEX[hold] - FIB_INDEX[val]) == 1 and (hold + val) in FIB_SET:
                    new_row.append(hold + val)
                    self.score += hold + val
                    hold = -1
                else:
                    new_row.append(hold)
                    hold = val
            if hold != -1:
                new_row.append(hold)
            while len(new_row) < 4:
                new_row.append(0)
            self.matrix[i] = new_row
    #combines consecutive fibonacci nums

    def reverse(self):
        new_matrix = []
        for i in range(4):
            new_matrix.append([])
            for j in range(4):
                new_matrix[i].append(self.matrix[i][3-j])
        self.matrix = new_matrix

    def transpose(self):
        new_matrix = [[0]*4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                new_matrix[i][j] = self.matrix[j][i]
        self.matrix = new_matrix

    def add_new_tile(self):
        empty_cells = [(i, j) for i in range(4) for j in range(4) if self.matrix[i][j] == 0]
        if not empty_cells:
            return  # no empty cells, don't add
        row, col = random.choice(empty_cells)

        # randomly choose 1 or 2 (like start_game)
        new_value = random.choice([1, 2])
        self.matrix[row][col] = new_value

        self.cells[row][col]["frame"].configure(bg=c.CELL_COLORS[new_value])
        self.cells[row][col]["number"].configure(
            bg=c.CELL_COLORS[new_value],
            fg=c.CELL_NUMBER_COLORS[new_value],
            font=c.CELL_NUMBER_FONTS[new_value],
            text=str(new_value)
        )
    #adding new tile randomly to empty cell

    def update_GUI(self):
        for i in range(4):
            for j in range(4):
                cell_value = self.matrix[i][j]
                if cell_value == 0:
                    self.cells[i][j]["frame"].configure(bg=c.EMPTY_CELL_COLOR)
                    self.cells[i][j]["number"].configure(bg=c.EMPTY_CELL_COLOR, text="")
                else:
                    self.cells[i][j]["frame"].configure(bg=c.CELL_COLORS[cell_value])
                    self.cells[i][j]["number"].configure(
                        bg=c.CELL_COLORS[cell_value],
                        fg=c.CELL_NUMBER_COLORS[cell_value],
                        font=c.CELL_NUMBER_FONTS[cell_value],
                        text=str(cell_value)
                    )
        self.score_label.configure(text=self.score)
        self.update_idletasks()

    #Arrow Press Functions
    def left(self, event):
        self.stack()
        self.combine()
        self.stack()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()

    def right(self, event):
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()

    def up(self, event):
        self.transpose()
        self.stack()
        self.combine()
        self.stack()
        self.transpose()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()


    def down(self, event):
        self.transpose()
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.transpose()
        self.add_new_tile()
        self.update_GUI()
        self.game_over()

    #check if any moves are possible
    def horizontal_move_exists(self):
        for i in range(4):
            for j in range(3):
                a = self.matrix[i][j]
                b = self.matrix[i][j+1]
                if a in FIB_INDEX and b in FIB_INDEX and abs(FIB_INDEX[a] - FIB_INDEX[b]) == 1:
                    return True
        return False

    def vertical_move_exists(self):
        for i in range(3):
            for j in range(4):
                a = self.matrix[i][j]
                b = self.matrix[i+1][j]
                if a in FIB_INDEX and b in FIB_INDEX and abs(FIB_INDEX[a] - FIB_INDEX[b]) == 1:
                    return True
        return False

    #check is game is over and if win/lose
    def game_over(self):
        fib_win = FIB_LIST[-1]
        if any(fib_win in row for row in self.matrix):
            game_over_frame = tk.Frame(self.main_grid, borderwidth=2)
            game_over_frame.place(relx=0.5, rely=0.5, anchor = "center")
            tk.Label(
                game_over_frame,
                text="You Win!",
                bg = c.WINNER_BG,
                fg = c.GAME_OVER_FONT_COLOR,
                font = c.GAME_OVER_FONT
            ).pack()
        elif not any(0 in row for row in self.matrix) and not self.horizontal_move_exists() and not self.vertical_move_exists():
            game_over_frame = tk.Frame(self.main_grid, borderwidth=2)
            game_over_frame.place(relx=0.5, rely=0.5, anchor = "center")
            tk.Label(
                game_over_frame,
                text="Game Over!",
                bg = c.LOSER_BG,
                fg = c.GAME_OVER_FONT_COLOR,
                font = c.GAME_OVER_FONT
            ).pack()

def main():
    Game()

if __name__ == "__main__":
    main()