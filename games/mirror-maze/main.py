import tkinter as tk
from tkinter import messagebox
import random

class MirrorMaze:
    def __init__(self, root):
        self.root = root
        self.root.title("Mirror Maze")
        self.root.resizable(False, False)
        
        # Game constants
        self.GRID_SIZE = 15
        self.CELL_SIZE = 40
        self.canvas_width = self.GRID_SIZE * self.CELL_SIZE
        self.canvas_height = self.GRID_SIZE * self.CELL_SIZE
        
        # Colors
        self.COLOR_BG = "#2C3E50"
        self.COLOR_WALL = "#34495E"
        self.COLOR_PATH = "#ECF0F1"
        self.COLOR_PLAYER = "#3498DB"
        self.COLOR_START = "#2ECC71"
        self.COLOR_EXIT = "#E74C3C"
        
        # Game state
        self.player_pos = [1, 1]
        self.exit_pos = [self.GRID_SIZE - 2, self.GRID_SIZE - 2]
        self.moves = 0
        self.time_elapsed = 0
        self.game_active = True
        self.mirror_mode = "vertical"  # vertical, horizontal, or both
        
        # Create UI
        self.create_widgets()
        self.generate_maze()
        self.draw_maze()
        self.start_timer()
        
        # Bind keys
        self.root.bind("<Up>", lambda e: self.move("up"))
        self.root.bind("<Down>", lambda e: self.move("down"))
        self.root.bind("<Left>", lambda e: self.move("left"))
        self.root.bind("<Right>", lambda e: self.move("right"))
        self.root.bind("r", lambda e: self.restart_game())
        self.root.bind("u", lambda e: self.undo_move())
        
    def create_widgets(self):
        # Top frame for info
        info_frame = tk.Frame(self.root, bg="#34495E", padx=10, pady=10)
        info_frame.pack(fill=tk.X)
        
        # Mirror mode label
        self.mirror_label = tk.Label(
            info_frame,
            text="Mirror Mode: VERTICAL",
            font=("Arial", 12, "bold"),
            bg="#34495E",
            fg="#E74C3C"
        )
        self.mirror_label.pack(side=tk.LEFT, padx=10)
        
        # Moves counter
        self.moves_label = tk.Label(
            info_frame,
            text="Moves: 0",
            font=("Arial", 12),
            bg="#34495E",
            fg="#ECF0F1"
        )
        self.moves_label.pack(side=tk.LEFT, padx=10)
        
        # Timer
        self.timer_label = tk.Label(
            info_frame,
            text="Time: 0s",
            font=("Arial", 12),
            bg="#34495E",
            fg="#ECF0F1"
        )
        self.timer_label.pack(side=tk.LEFT, padx=10)
        
        # Canvas for maze
        self.canvas = tk.Canvas(
            self.root,
            width=self.canvas_width,
            height=self.canvas_height,
            bg=self.COLOR_BG,
            highlightthickness=0
        )
        self.canvas.pack(padx=10, pady=10)
        
        # Bottom frame for controls
        control_frame = tk.Frame(self.root, bg="#34495E", padx=10, pady=10)
        control_frame.pack(fill=tk.X)
        
        # Instructions
        instructions = tk.Label(
            control_frame,
            text="Arrow Keys: Move | R: Restart | U: Undo",
            font=("Arial", 10),
            bg="#34495E",
            fg="#ECF0F1"
        )
        instructions.pack(side=tk.LEFT, padx=10)
        
        # Buttons
        btn_frame = tk.Frame(control_frame, bg="#34495E")
        btn_frame.pack(side=tk.RIGHT)
        
        tk.Button(
            btn_frame,
            text="Restart",
            command=self.restart_game,
            bg="#E74C3C",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=15,
            pady=5
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            btn_frame,
            text="Change Mirror",
            command=self.change_mirror_mode,
            bg="#9B59B6",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=15,
            pady=5
        ).pack(side=tk.LEFT, padx=5)
        
    def generate_maze(self):
        # Initialize maze with walls
        self.maze = [[1 for _ in range(self.GRID_SIZE)] for _ in range(self.GRID_SIZE)]
        
        # Create paths using recursive backtracking
        def carve_path(x, y):
            self.maze[y][x] = 0
            
            directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]
            random.shuffle(directions)
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 < nx < self.GRID_SIZE - 1 and 0 < ny < self.GRID_SIZE - 1 and self.maze[ny][nx] == 1:
                    self.maze[y + dy // 2][x + dx // 2] = 0
                    carve_path(nx, ny)
        
        # Start carving from player position
        carve_path(1, 1)
        
        # Ensure start and end are clear
        self.maze[1][1] = 0
        self.maze[self.GRID_SIZE - 2][self.GRID_SIZE - 2] = 0
        
        # Store move history for undo
        self.move_history = []
        
    def draw_maze(self):
        self.canvas.delete("all")
        
        # Draw maze cells
        for y in range(self.GRID_SIZE):
            for x in range(self.GRID_SIZE):
                x1 = x * self.CELL_SIZE
                y1 = y * self.CELL_SIZE
                x2 = x1 + self.CELL_SIZE
                y2 = y1 + self.CELL_SIZE
                
                color = self.COLOR_WALL if self.maze[y][x] == 1 else self.COLOR_PATH
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=self.COLOR_BG)
        
        # Draw start marker
        sx = 1 * self.CELL_SIZE + self.CELL_SIZE // 2
        sy = 1 * self.CELL_SIZE + self.CELL_SIZE // 2
        self.canvas.create_oval(
            sx - 8, sy - 8, sx + 8, sy + 8,
            fill=self.COLOR_START,
            outline=""
        )
        
        # Draw exit
        ex = self.exit_pos[0] * self.CELL_SIZE
        ey = self.exit_pos[1] * self.CELL_SIZE
        self.canvas.create_rectangle(
            ex + 5, ey + 5, ex + self.CELL_SIZE - 5, ey + self.CELL_SIZE - 5,
            fill=self.COLOR_EXIT,
            outline=""
        )
        self.canvas.create_text(
            ex + self.CELL_SIZE // 2,
            ey + self.CELL_SIZE // 2,
            text="EXIT",
            font=("Arial", 10, "bold"),
            fill="white"
        )
        
        # Draw player
        px = self.player_pos[0] * self.CELL_SIZE + self.CELL_SIZE // 2
        py = self.player_pos[1] * self.CELL_SIZE + self.CELL_SIZE // 2
        self.canvas.create_oval(
            px - 12, py - 12, px + 12, py + 12,
            fill=self.COLOR_PLAYER,
            outline="white",
            width=2
        )
        
    def move(self, direction):
        if not self.game_active:
            return
        
        # Mirror the direction based on mirror mode
        mirrored_direction = self.mirror_direction(direction)
        
        # Calculate new position
        new_x, new_y = self.player_pos[0], self.player_pos[1]
        
        if mirrored_direction == "up":
            new_y -= 1
        elif mirrored_direction == "down":
            new_y += 1
        elif mirrored_direction == "left":
            new_x -= 1
        elif mirrored_direction == "right":
            new_x += 1
        
        # Check if move is valid
        if (0 <= new_x < self.GRID_SIZE and 
            0 <= new_y < self.GRID_SIZE and 
            self.maze[new_y][new_x] == 0):
            
            # Save current position for undo
            self.move_history.append(self.player_pos[:])
            
            # Update position
            self.player_pos = [new_x, new_y]
            self.moves += 1
            self.moves_label.config(text=f"Moves: {self.moves}")
            self.draw_maze()
            
            # Check for win
            if self.player_pos == self.exit_pos:
                self.win_game()
    
    def mirror_direction(self, direction):
        if self.mirror_mode == "vertical":
            # Mirror up/down
            if direction == "up":
                return "down"
            elif direction == "down":
                return "up"
            return direction
        elif self.mirror_mode == "horizontal":
            # Mirror left/right
            if direction == "left":
                return "right"
            elif direction == "right":
                return "left"
            return direction
        elif self.mirror_mode == "both":
            # Mirror both axes
            mirrors = {"up": "down", "down": "up", "left": "right", "right": "left"}
            return mirrors[direction]
        return direction
    
    def undo_move(self):
        if not self.game_active or not self.move_history:
            return
        
        self.player_pos = self.move_history.pop()
        self.moves += 1  # Undo counts as a move
        self.moves_label.config(text=f"Moves: {self.moves}")
        self.draw_maze()
    
    def change_mirror_mode(self):
        modes = ["vertical", "horizontal", "both"]
        current_idx = modes.index(self.mirror_mode)
        self.mirror_mode = modes[(current_idx + 1) % len(modes)]
        
        mode_text = self.mirror_mode.upper()
        self.mirror_label.config(text=f"Mirror Mode: {mode_text}")
    
    def start_timer(self):
        if self.game_active:
            self.time_elapsed += 1
            self.timer_label.config(text=f"Time: {self.time_elapsed}s")
            self.root.after(1000, self.start_timer)
    
    def win_game(self):
        self.game_active = False
        messagebox.showinfo(
            "Congratulations!",
            f"You solved the Mirror Maze!\n\nMoves: {self.moves}\nTime: {self.time_elapsed}s"
        )
    
    def restart_game(self):
        self.player_pos = [1, 1]
        self.moves = 0
        self.time_elapsed = 0
        self.game_active = True
        self.moves_label.config(text="Moves: 0")
        self.timer_label.config(text="Time: 0s")
        self.generate_maze()
        self.draw_maze()

def main():
    root = tk.Tk()
    game = MirrorMaze(root)
    root.mainloop()

if __name__ == "__main__":
    main()