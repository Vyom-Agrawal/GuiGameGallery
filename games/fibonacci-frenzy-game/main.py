import tkinter as tk
import random

# Fibonacci cache for a 4x4 board
FIB_LIST = [1, 1]
for i in range(2, 16):  # 4x4 = 16 tiles
    FIB_LIST.append(FIB_LIST[i - 1] + FIB_LIST[i - 2])
FIB_SET = set(FIB_LIST)
FIB_INDEX = {FIB_LIST[i]: i for i in range(len(FIB_LIST))}

#colors and fonts for design
GRID_COLOR = "#a39489"
EMPTY_CELL_COLOR = "#c2b3a9"
SCORE_LABEL_FONT = ("Verdana", 24)
SCORE_FONT = ("Helvetica", 36, "bold")
GAME_OVER_FONT = ("Helvetica", 48, "bold")
GAME_OVER_FONT_COLOR = "#ffffff"
WINNER_BG = "#ffcc00"
LOSER_BG = "#a39489"

CELL_COLORS = {
    1: "#fcefe6",
    2: "#f2e8cb",
    3: "#f5b682",
    5: "#f29446",
    8: "#ff775c",
    13: "#e64c2e",
    21: "#ede291",
    34: "#fce130",
    55: "#ffdb4a",
    89: "#f0b922",
    144: "#fad74d",
    233: "#f9a602",   
    377: "#ff8c00",   
    610: "#ff4500",   
    987: "#cc0000",   
}

CELL_NUMBER_COLORS = {
    1: "#695c57",
    2: "#695c57",
    3: "#ffffff",
    5: "#ffffff",
    8: "#ffffff",
    13: "#ffffff",
    21: "#ffffff",
    34: "#ffffff",
    55: "#ffffff",
    89: "#ffffff",
    144: "#ffffff",
    233: "#ffffff",   
    377: "#ffffff",  
    610: "#ffffff",  
    987: "#ffffff",
}

CELL_NUMBER_FONTS = {
    1: ("Helvetica", 55, "bold"),
    2: ("Helvetica", 55, "bold"),
    3: ("Helvetica", 55, "bold"),
    5: ("Helvetica", 55, "bold"),
    8: ("Helvetica", 55, "bold"),
    13: ("Helvetica", 50, "bold"),
    21: ("Helvetica", 50, "bold"),
    34: ("Helvetica", 50, "bold"),
    55: ("Helvetica", 50, "bold"),
    89: ("Helvetica", 50, "bold"),
    144: ("Helvetica", 45, "bold"),
    233: ("Helvetica", 45, "bold"),
    377: ("Helvetica", 45, "bold"),
    610: ("Helvetica", 40, "bold"),
    987: ("Helvetica", 40, "bold")
}

class Game(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("Fibonacci Frenzy - Click to Merge!")
        self.master.geometry("1100x850")  # Set window size

        self.main_grid = tk.Frame(
            self, bg =  GRID_COLOR, bd=3, width = 700, height = 700
        )
        self.main_grid.grid(pady=(200,0), padx=(20,0))
        
        # Initialize selection state and difficulty first
        self.selected_tiles = []  # List to store (row, col) of selected tiles
        self.selection_count = 0  # Track how many tiles are selected (0, 1, or 2)
        self.difficulty = "medium"  # easy, medium, hard, super_hard
        self.target_fib = self.get_target_fib()
        
        self.make_GUI()
        self.start_game()

        self.mainloop()

    def make_GUI(self):
        #make grid
        self.cells = []
        for i in range(4):
            row = []
            for j in range(4):
                cell_frame = tk.Frame(
                    self.main_grid,
                    bg=EMPTY_CELL_COLOR,
                    width = 170,
                    height=170
                )
                cell_frame.grid(row=i, column=j, padx=5, pady=5)
                cell_number = tk.Label(self.main_grid, bg = EMPTY_CELL_COLOR)
                cell_number.grid(row = i, column = j)
                
                # Bind click events to both frame and number label
                cell_frame.bind("<Button-1>", lambda e, r=i, c=j: self.on_cell_click(r, c))
                cell_number.bind("<Button-1>", lambda e, r=i, c=j: self.on_cell_click(r, c))
                
                cell_data = {"frame": cell_frame, "number": cell_number}
                row.append(cell_data)
            self.cells.append(row)
        
        #make fibonacci sequence display at top
        fib_frame = tk.Frame(self)
        fib_frame.place(relx=0.5, y=50, anchor="center")
        tk.Label(
            fib_frame,
            text="Fibonacci Sequence:",
            font=("Arial", 16, "bold"),
            fg= CELL_NUMBER_COLORS[1]
        ).pack()
        tk.Label(
            fib_frame,
            text="1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987",
            font=("Arial", 15, "bold"),
            fg= CELL_NUMBER_COLORS[1]
        ).pack()
        
        #make score and difficulty buttons on the same line
        control_frame = tk.Frame(self)
        control_frame.place(relx=0.5, y=130, anchor="center")
        
        # Score on the left
        score_frame = tk.Frame(control_frame)
        score_frame.pack(side="left", padx=20)
        tk.Label(
            score_frame,
            text="Score",
            font=("Arial", 14, "bold"),
            fg= CELL_NUMBER_COLORS[1]
        ).pack()
        self.score_label = tk.Label(score_frame, text="0", font=("Arial", 20, "bold"), fg= CELL_NUMBER_COLORS[1])
        self.score_label.pack()
        
        # Difficulty buttons in the center
        diff_frame = tk.Frame(control_frame)
        diff_frame.pack(side="left", padx=20)
        
        tk.Label(
            diff_frame,
            text="Mode:",
            font=("Arial", 14, "bold"),
            fg= CELL_NUMBER_COLORS[1]
        ).pack()
        
        # Create difficulty buttons in a row
        difficulties = [("easy", 34), ("medium", 89), ("hard", 233), ("super_hard", 987)]
        self.diff_buttons = {}
        
        button_frame = tk.Frame(diff_frame)
        button_frame.pack(pady=5)
        
        for diff, target in difficulties:
            btn = tk.Button(
                button_frame,
                text=f"{diff.replace('_', ' ').title()}\n{target}",
                command=lambda d=diff: self.change_difficulty(d),
                font=("Arial", 10, "bold"),
                bg= CELL_COLORS[1] if diff == self.difficulty else  EMPTY_CELL_COLOR,
                fg= CELL_NUMBER_COLORS[1],
                width=8,
                height=2,
                relief="raised",
                bd=2
            )
            btn.pack(side="left", padx=3)
            self.diff_buttons[diff] = btn
        
        # Restart button on the right
        restart_frame = tk.Frame(control_frame)
        restart_frame.pack(side="left", padx=20)
        
        restart_btn = tk.Button(
            restart_frame,
            text="Restart",
            command=self.restart_game,
            font=("Arial", 14, "bold"),
            bg= CELL_COLORS[2],
            fg= CELL_NUMBER_COLORS[2],
            relief="raised",
            bd=3,
            width=8,
            height=2
        )
        restart_btn.pack()

    def start_game(self):
        # Initialize matrix with zeros
        self.matrix = [[0]*4 for _ in range(4)]
        
        # Fill grid with 15 starting tiles (leaving 1 empty)
        starting_tiles = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 5, 5, 8, 8, 13]
        
        # Get all positions and shuffle
        positions = [(i, j) for i in range(4) for j in range(4)]
        random.shuffle(positions)
        
        # Place the starting tiles
        for idx, value in enumerate(starting_tiles):
            row, col = positions[idx]
            self.matrix[row][col] = value
            self.cells[row][col]["frame"].configure(bg= CELL_COLORS[value])
            self.cells[row][col]["number"].configure(
                bg= CELL_COLORS[value],
                fg= CELL_NUMBER_COLORS[value],
                font= CELL_NUMBER_FONTS[value],
                text=str(value)
            )

        self.score = 0
        self.selection_count = 0
        self.selected_tiles = []
        self.target_fib = self.get_target_fib()
        self.update_GUI()

    def update_GUI(self):
        for i in range(4):
            for j in range(4):
                cell_value = self.matrix[i][j]
                if cell_value == 0:
                    self.cells[i][j]["frame"].configure(bg= EMPTY_CELL_COLOR)
                    self.cells[i][j]["number"].configure(bg= EMPTY_CELL_COLOR, text="")
                else:
                    self.cells[i][j]["frame"].configure(bg= CELL_COLORS[cell_value])
                    self.cells[i][j]["number"].configure(
                        bg= CELL_COLORS[cell_value],
                        fg= CELL_NUMBER_COLORS[cell_value],
                        font= CELL_NUMBER_FONTS[cell_value],
                        text=str(cell_value)
                    )
        self.score_label.configure(text=self.score)
        self.update_idletasks()

    # Click-based tile selection functions
    def on_cell_click(self, row, col):
        """Handle cell click for tile selection and merging"""
        # Don't allow selection of empty cells
        if self.matrix[row][col] == 0:
            return
            
        # If this cell is already selected, deselect it
        if (row, col) in self.selected_tiles:
            self.deselect_tile(row, col)
            return
            
        # If we already have 2 tiles selected, clear selection first
        if self.selection_count >= 2:
            self.clear_selection()
            
        # Select this tile
        self.select_tile(row, col)
        
        # If we now have 2 tiles selected, try to merge them
        if self.selection_count == 2:
            self.attempt_merge()
    
    def select_tile(self, row, col):
        """Select a tile and add visual highlighting"""
        self.selected_tiles.append((row, col))
        self.selection_count += 1
        
        # Add visual highlighting (thicker border)
        self.cells[row][col]["frame"].configure(relief="raised", bd=5)
        
    def deselect_tile(self, row, col):
        """Deselect a tile and remove highlighting"""
        if (row, col) in self.selected_tiles:
            self.selected_tiles.remove((row, col))
            self.selection_count -= 1
            
            # Remove visual highlighting
            self.cells[row][col]["frame"].configure(relief="flat", bd=0)
            
    def clear_selection(self):
        """Clear all tile selections"""
        for row, col in self.selected_tiles:
            self.cells[row][col]["frame"].configure(relief="flat", bd=0)
        self.selected_tiles = []
        self.selection_count = 0
        
    def attempt_merge(self):
        """Try to merge the two selected tiles"""
        if len(self.selected_tiles) != 2:
            return
            
        (r1, c1), (r2, c2) = self.selected_tiles
        val1, val2 = self.matrix[r1][c1], self.matrix[r2][c2]
        
        # Check if the two values are consecutive Fibonacci numbers
        if self.can_merge(val1, val2):
            # Merge successful: place result in second clicked cell, zero the first
            merged_value = val1 + val2
            self.matrix[r2][c2] = merged_value
            self.matrix[r1][c1] = 0
            
            # Update score
            self.score += merged_value
            
            # Clear selection
            self.clear_selection()
            
            # Update display (NO new tiles added!)
            self.update_GUI()
            
            # Check game over
            self.game_over()
        else:
            # Merge failed: just clear selection (NO new tiles added!)
            self.clear_selection()
            
    def can_merge(self, val1, val2):
        """Check if two values can be merged (consecutive Fibonacci numbers)"""
        if val1 not in FIB_INDEX or val2 not in FIB_INDEX:
            return False
        # Special-case: allow 1 + 1 -> 2
        if val1 == 1 and val2 == 1:
            return True
        
        # Check if they are consecutive in the Fibonacci sequence
        return abs(FIB_INDEX[val1] - FIB_INDEX[val2]) == 1
    
    def get_target_fib(self):
        """Get target Fibonacci number based on difficulty"""
        targets = {
            "easy": 34,
            "medium": 89,
            "hard": 233,
            "super_hard": 987
        }
        return targets.get(self.difficulty, 89)
    
    def change_difficulty(self, difficulty):
        """Change difficulty and update target"""
        self.difficulty = difficulty
        self.target_fib = self.get_target_fib()
        
        # Update button colors
        for diff, btn in self.diff_buttons.items():
            if diff == difficulty:
                btn.configure(bg= CELL_COLORS[1])
            else:
                btn.configure(bg= EMPTY_CELL_COLOR)
    
    def restart_game(self):
        """Restart the game"""
        for widget in self.main_grid.winfo_children():
            if isinstance(widget, tk.Frame) and len(widget.winfo_children()) == 1:
                label = widget.winfo_children()[0]
                if isinstance(label, tk.Label) and label.cget("text") in ("You Win!", "Game Over!"):
                    widget.destroy()
        self.start_game()
        self.clear_selection()

    def any_move_exists(self):
        """Check if any two tiles can be merged anywhere on the board"""
        # Get all non-zero tiles
        tiles = []
        for i in range(4):
            for j in range(4):
                if self.matrix[i][j] != 0:
                    tiles.append(self.matrix[i][j])
        
        # Need at least 2 tiles to have a move
        if len(tiles) < 2:
            return False
        
        # Check all possible pairs
        for i in range(len(tiles)):
            for j in range(i + 1, len(tiles)):
                if self.can_merge(tiles[i], tiles[j]):
                    return True
        return False

    def game_over(self):
        """Check if game is over and if win/lose"""
        if any(self.target_fib in row for row in self.matrix):
            game_over_frame = tk.Frame(self.main_grid, borderwidth=2)
            game_over_frame.place(relx=0.5, rely=0.5, anchor = "center")
            tk.Label(
                game_over_frame,
                text="You Win!",
                bg =  WINNER_BG,
                fg =  GAME_OVER_FONT_COLOR,
                font =  GAME_OVER_FONT
            ).pack()
        elif not self.any_move_exists():
            game_over_frame = tk.Frame(self.main_grid, borderwidth=2)
            game_over_frame.place(relx=0.5, rely=0.5, anchor = "center")
            tk.Label(
                game_over_frame,
                text="Game Over!",
                bg =  LOSER_BG,
                fg =  GAME_OVER_FONT_COLOR,
                font =  GAME_OVER_FONT
            ).pack()

def main():
    Game()

if __name__ == "__main__":
    main()
