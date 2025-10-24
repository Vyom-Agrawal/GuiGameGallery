import tkinter as tk
from tkinter import messagebox
import random
import time

class PatternLockGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Pattern Lock Memory Game")
        self.root.geometry("550x780")
        self.root.resizable(False, False)
        self.root.configure(bg="#1a1a2e")
        
        # Game state
        self.grid_size = 3
        self.dot_positions = {}
        self.current_pattern = []
        self.user_pattern = []
        self.level = 1
        self.is_showing = False
        self.is_playing = False
        self.dragging = False
        
        # Visual settings
        self.dot_radius = 20
        self.canvas_size = 450
        self.spacing = self.canvas_size // (self.grid_size + 1)
        
        # Colors
        self.bg_color = "#16213e"
        self.dot_color = "#0f3460"
        self.dot_active_color = "#00d4ff"
        self.line_color = "#00d4ff"
        self.error_color = "#ff4757"
        self.success_color = "#2ed573"
        
        self.setup_ui()
        self.create_grid()
        
    def setup_ui(self):
        # Title
        title_label = tk.Label(
            self.root,
            text="PATTERN LOCK",
            font=("Arial", 28, "bold"),
            bg="#1a1a2e",
            fg="#00d4ff"
        )
        title_label.pack(pady=20)
        
        # Score frame
        score_frame = tk.Frame(self.root, bg="#1a1a2e")
        score_frame.pack(pady=10)
        
        self.level_label = tk.Label(
            score_frame,
            text=f"Level: {self.level}",
            font=("Arial", 16, "bold"),
            bg="#1a1a2e",
            fg="#ffffff"
        )
        self.level_label.pack(side=tk.LEFT, padx=20)
        
        self.pattern_length_label = tk.Label(
            score_frame,
            text=f"Pattern Length: {self.level + 2}",
            font=("Arial", 16, "bold"),
            bg="#1a1a2e",
            fg="#ffffff"
        )
        self.pattern_length_label.pack(side=tk.LEFT, padx=20)
        
        # Canvas
        self.canvas = tk.Canvas(
            self.root,
            width=self.canvas_size,
            height=self.canvas_size,
            bg=self.bg_color,
            highlightthickness=0
        )
        self.canvas.pack(pady=20)
        
        # Status label
        self.status_label = tk.Label(
            self.root,
            text="Click 'Start Game' to begin!",
            font=("Arial", 14),
            bg="#1a1a2e",
            fg="#ffffff",
            wraplength=500
        )
        self.status_label.pack(pady=10)
        
        # Buttons
        button_frame = tk.Frame(self.root, bg="#1a1a2e")
        button_frame.pack(pady=10)
        
        self.start_button = tk.Button(
            button_frame,
            text="Start Game",
            font=("Arial", 14, "bold"),
            bg="#00d4ff",
            fg="#1a1a2e",
            command=self.start_game,
            padx=20,
            pady=10,
            relief=tk.FLAT,
            cursor="hand2"
        )
        self.start_button.pack(side=tk.LEFT, padx=10)
        
        self.restart_button = tk.Button(
            button_frame,
            text="Restart",
            font=("Arial", 14, "bold"),
            bg="#ff4757",
            fg="#ffffff",
            command=self.reset_game,
            padx=20,
            pady=10,
            relief=tk.FLAT,
            cursor="hand2",
            state=tk.DISABLED
        )
        self.restart_button.pack(side=tk.LEFT, padx=10)
        
        # Bind mouse events
        self.canvas.bind("<Button-1>", self.on_mouse_down)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)
        
    def create_grid(self):
        """Create the 3x3 grid of dots"""
        self.canvas.delete("all")
        self.dot_positions = {}
        
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                x = (col + 1) * self.spacing
                y = (row + 1) * self.spacing
                
                # Draw outer circle
                self.canvas.create_oval(
                    x - self.dot_radius - 5,
                    y - self.dot_radius - 5,
                    x + self.dot_radius + 5,
                    y + self.dot_radius + 5,
                    fill=self.bg_color,
                    outline=self.dot_color,
                    width=3,
                    tags=f"dot_{row}_{col}_outer"
                )
                
                # Draw inner circle
                dot = self.canvas.create_oval(
                    x - self.dot_radius,
                    y - self.dot_radius,
                    x + self.dot_radius,
                    y + self.dot_radius,
                    fill=self.dot_color,
                    outline="",
                    tags=f"dot_{row}_{col}"
                )
                
                self.dot_positions[(row, col)] = (x, y, dot)
    
    def get_dots_on_line(self, pos1, pos2):
        """Get all dots that lie on the line between pos1 and pos2"""
        r1, c1 = pos1
        r2, c2 = pos2
        
        dots_on_line = []
        
        # Calculate the direction
        dr = r2 - r1
        dc = c2 - c1
        
        # Find the GCD to get the step size
        from math import gcd
        steps = gcd(abs(dr), abs(dc))
        
        if steps > 1:
            # There are dots in between
            step_r = dr // steps
            step_c = dc // steps
            
            # Check each intermediate position
            for i in range(1, steps):
                mid_r = r1 + step_r * i
                mid_c = c1 + step_c * i
                if 0 <= mid_r < self.grid_size and 0 <= mid_c < self.grid_size:
                    dots_on_line.append((mid_r, mid_c))
        
        return dots_on_line
    
    def is_valid_move(self, pattern, next_pos):
        """Check if adding next_pos to pattern is valid (doesn't skip over unvisited dots)"""
        if not pattern:
            return True
        
        last_pos = pattern[-1]
        dots_on_line = self.get_dots_on_line(last_pos, next_pos)
        
        # All dots on the line must already be in the pattern
        for dot in dots_on_line:
            if dot not in pattern:
                return False
        
        return True
    
    def generate_pattern(self):
        """Generate a random valid pattern that doesn't cross unvisited dots"""
        length = self.level + 2
        max_attempts = 100
        
        for attempt in range(max_attempts):
            pattern = []
            available = [(r, c) for r in range(self.grid_size) for c in range(self.grid_size)]
            
            # Start with random position
            current = random.choice(available)
            pattern.append(current)
            available.remove(current)
            
            # Try to build a valid pattern
            while len(pattern) < length and available:
                # Get valid next moves (don't skip over unvisited dots)
                valid_moves = [pos for pos in available if self.is_valid_move(pattern, pos)]
                
                if not valid_moves:
                    # No valid moves, restart pattern generation
                    break
                
                # Choose a random valid move
                next_pos = random.choice(valid_moves)
                pattern.append(next_pos)
                available.remove(next_pos)
            
            # If we got a pattern of the desired length, return it
            if len(pattern) == length:
                return pattern
        
        # Fallback: if we couldn't generate a pattern, return a simple adjacent pattern
        pattern = [(0, 0)]
        available = [(r, c) for r in range(self.grid_size) for c in range(self.grid_size) if (r, c) != (0, 0)]
        
        while len(pattern) < length and available:
            # Find adjacent positions
            last = pattern[-1]
            adjacent = [
                (last[0] + dr, last[1] + dc)
                for dr in [-1, 0, 1]
                for dc in [-1, 0, 1]
                if (dr != 0 or dc != 0) and 
                   0 <= last[0] + dr < self.grid_size and 
                   0 <= last[1] + dc < self.grid_size and
                   (last[0] + dr, last[1] + dc) in available
            ]
            
            if adjacent:
                next_pos = random.choice(adjacent)
                pattern.append(next_pos)
                available.remove(next_pos)
            else:
                break
        
        return pattern
    
    def show_pattern(self):
        """Animate the pattern for the player to memorize"""
        self.is_showing = True
        self.status_label.config(text="Watch carefully and memorize the pattern!")
        self.start_button.config(state=tk.DISABLED)
        
        def animate_step(index):
            if index >= len(self.current_pattern):
                # Pattern shown, now let user try
                self.root.after(500, self.start_user_input)
                return
            
            pos = self.current_pattern[index]
            x, y, dot = self.dot_positions[pos]
            
            # Highlight dot
            self.canvas.itemconfig(dot, fill=self.dot_active_color)
            self.canvas.itemconfig(f"dot_{pos[0]}_{pos[1]}_outer", outline=self.dot_active_color, width=4)
            
            # Draw line from previous dot if exists
            if index > 0:
                prev_pos = self.current_pattern[index - 1]
                prev_x, prev_y, _ = self.dot_positions[prev_pos]
                self.canvas.create_line(
                    prev_x, prev_y, x, y,
                    fill=self.line_color,
                    width=8,
                    tags="pattern_line",
                    capstyle=tk.ROUND
                )
            
            # Continue animation
            self.root.after(600, lambda: animate_step(index + 1))
        
        animate_step(0)
    
    def start_user_input(self):
        """Clear the pattern and let user try to replicate"""
        self.is_showing = False
        self.is_playing = True
        self.user_pattern = []
        
        # Clear visual pattern
        self.canvas.delete("pattern_line")
        for pos in self.current_pattern:
            _, _, dot = self.dot_positions[pos]
            self.canvas.itemconfig(dot, fill=self.dot_color)
            self.canvas.itemconfig(f"dot_{pos[0]}_{pos[1]}_outer", outline=self.dot_color, width=3)
        
        self.status_label.config(text="Now draw the pattern you saw!")
    
    def get_dot_at_position(self, x, y):
        """Find which dot is at the given canvas coordinates"""
        for pos, (dot_x, dot_y, _) in self.dot_positions.items():
            distance = ((x - dot_x) ** 2 + (y - dot_y) ** 2) ** 0.5
            if distance <= self.dot_radius + 10:
                return pos
        return None
    
    def on_mouse_down(self, event):
        """Handle mouse click on canvas"""
        if not self.is_playing:
            return
        
        dot_pos = self.get_dot_at_position(event.x, event.y)
        if dot_pos and dot_pos not in self.user_pattern:
            self.dragging = True
            # Auto-add any dots that are crossed over
            if self.user_pattern:
                dots_on_line = self.get_dots_on_line(self.user_pattern[-1], dot_pos)
                for intermediate_dot in dots_on_line:
                    if intermediate_dot not in self.user_pattern:
                        self.add_dot_to_pattern(intermediate_dot)
            
            self.add_dot_to_pattern(dot_pos)
    
    def on_mouse_drag(self, event):
        """Handle mouse drag on canvas"""
        if not self.is_playing or not self.dragging:
            return
        
        dot_pos = self.get_dot_at_position(event.x, event.y)
        if dot_pos and dot_pos not in self.user_pattern:
            # Auto-add any dots that are crossed over
            if self.user_pattern:
                dots_on_line = self.get_dots_on_line(self.user_pattern[-1], dot_pos)
                for intermediate_dot in dots_on_line:
                    if intermediate_dot not in self.user_pattern:
                        self.add_dot_to_pattern(intermediate_dot)
            
            self.add_dot_to_pattern(dot_pos)
    
    def on_mouse_up(self, event):
        """Handle mouse release"""
        if not self.is_playing:
            return
        
        self.dragging = False
        if len(self.user_pattern) > 0:
            self.check_pattern()
    
    def add_dot_to_pattern(self, pos):
        """Add a dot to the user's pattern"""
        self.user_pattern.append(pos)
        x, y, dot = self.dot_positions[pos]
        
        # Highlight the dot
        self.canvas.itemconfig(dot, fill=self.dot_active_color)
        self.canvas.itemconfig(f"dot_{pos[0]}_{pos[1]}_outer", outline=self.dot_active_color, width=4)
        
        # Draw line from previous dot
        if len(self.user_pattern) > 1:
            prev_pos = self.user_pattern[-2]
            prev_x, prev_y, _ = self.dot_positions[prev_pos]
            self.canvas.create_line(
                prev_x, prev_y, x, y,
                fill=self.line_color,
                width=8,
                tags="user_line",
                capstyle=tk.ROUND
            )
    
    def check_pattern(self):
        """Check if user pattern matches the shown pattern"""
        self.is_playing = False
        
        if self.user_pattern == self.current_pattern:
            # Success!
            self.show_success()
            self.level += 1
            self.level_label.config(text=f"Level: {self.level}")
            self.pattern_length_label.config(text=f"Pattern Length: {self.level + 2}")
            self.root.after(1500, self.start_round)
        else:
            # Failure
            self.show_failure()
    
    def show_success(self):
        """Show success animation"""
        self.status_label.config(text="✓ Correct! Get ready for the next level...", fg=self.success_color)
        
        for pos in self.user_pattern:
            _, _, dot = self.dot_positions[pos]
            self.canvas.itemconfig(dot, fill=self.success_color)
            self.canvas.itemconfig(f"dot_{pos[0]}_{pos[1]}_outer", outline=self.success_color)
        
        self.canvas.itemconfig("user_line", fill=self.success_color)
    
    def show_failure(self):
        """Show failure animation and end game"""
        self.status_label.config(text=f"✗ Wrong pattern! Game Over - You reached Level {self.level}!", fg=self.error_color)
        
        for pos in self.user_pattern:
            _, _, dot = self.dot_positions[pos]
            self.canvas.itemconfig(dot, fill=self.error_color)
            self.canvas.itemconfig(f"dot_{pos[0]}_{pos[1]}_outer", outline=self.error_color)
        
        self.canvas.itemconfig("user_line", fill=self.error_color)
        
        self.start_button.config(state=tk.NORMAL, text="Play Again")
        self.restart_button.config(state=tk.NORMAL)
    
    def start_round(self):
        """Start a new round"""
        self.create_grid()
        self.current_pattern = self.generate_pattern()
        self.user_pattern = []
        self.status_label.config(text="Get ready...", fg="#ffffff")
        self.root.after(1000, self.show_pattern)
    
    def start_game(self):
        """Start the game"""
        self.level = 1
        self.level_label.config(text=f"Level: {self.level}")
        self.pattern_length_label.config(text=f"Pattern Length: {self.level + 2}")
        self.restart_button.config(state=tk.NORMAL)
        self.start_round()
    
    def reset_game(self):
        """Reset the game to initial state"""
        self.level = 1
        self.level_label.config(text=f"Level: {self.level}")
        self.pattern_length_label.config(text=f"Pattern Length: {self.level + 2}")
        self.status_label.config(text="Click 'Start Game' to begin!", fg="#ffffff")
        self.start_button.config(state=tk.NORMAL, text="Start Game")
        self.restart_button.config(state=tk.DISABLED)
        self.create_grid()
        self.is_playing = False
        self.is_showing = False

if __name__ == "__main__":
    root = tk.Tk()
    game = PatternLockGame(root)
    root.mainloop()