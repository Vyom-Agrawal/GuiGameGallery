import tkinter as tk
from tkinter import messagebox
import random
import time

class DoodleBuilder:
    def __init__(self, root):
        self.root = root
        self.root.title("Doodle Builder - Replicate the Pattern!")
        self.root.geometry("900x650")
        self.root.resizable(False, False)
        self.root.configure(bg="#2c3e50")
        
        # Game variables
        self.time_limit = 15
        self.time_remaining = self.time_limit
        self.timer_running = False
        self.score = 0
        self.attempts = 0
        self.drawing = False
        self.last_x = None
        self.last_y = None
        self.has_drawn = False  # Track if player has drawn anything
        
        # Pattern definitions
        self.patterns = {
            "Circle": self.draw_circle_pattern,
            "Star": self.draw_star_pattern,
            "Spiral": self.draw_spiral_pattern,
            "Zigzag": self.draw_zigzag_pattern,
            "Smiley": self.draw_smiley_pattern,
            "Triangle": self.draw_triangle_pattern,
            "Diamond": self.draw_diamond_pattern,
            "Wave": self.draw_wave_pattern
        }
        
        self.current_pattern = None
        
        self.setup_ui()
        self.load_random_pattern()
        
    def setup_ui(self):
        # Title
        title_label = tk.Label(
            self.root,
            text="🎨 Doodle Builder 🎨",
            font=("Arial", 24, "bold"),
            bg="#2c3e50",
            fg="#ecf0f1"
        )
        title_label.pack(pady=10)
        
        # Info frame
        info_frame = tk.Frame(self.root, bg="#2c3e50")
        info_frame.pack(pady=5)
        
        self.pattern_label = tk.Label(
            info_frame,
            text="Pattern: Loading...",
            font=("Arial", 14, "bold"),
            bg="#2c3e50",
            fg="#3498db"
        )
        self.pattern_label.grid(row=0, column=0, padx=20)
        
        self.timer_label = tk.Label(
            info_frame,
            text=f"Time: {self.time_limit}s",
            font=("Arial", 14, "bold"),
            bg="#2c3e50",
            fg="#e74c3c"
        )
        self.timer_label.grid(row=0, column=1, padx=20)
        
        self.score_label = tk.Label(
            info_frame,
            text="Score: 0",
            font=("Arial", 14, "bold"),
            bg="#2c3e50",
            fg="#2ecc71"
        )
        self.score_label.grid(row=0, column=2, padx=20)
        
        # Canvas container
        canvas_frame = tk.Frame(self.root, bg="#2c3e50")
        canvas_frame.pack(pady=10)
        
        # Sample canvas
        sample_frame = tk.Frame(canvas_frame, bg="#34495e", relief=tk.RAISED, borderwidth=3)
        sample_frame.grid(row=0, column=0, padx=10)
        
        sample_title = tk.Label(
            sample_frame,
            text="📋 Pattern to Copy",
            font=("Arial", 12, "bold"),
            bg="#34495e",
            fg="#ecf0f1"
        )
        sample_title.pack(pady=5)
        
        self.sample_canvas = tk.Canvas(
            sample_frame,
            width=350,
            height=350,
            bg="white",
            highlightthickness=2,
            highlightbackground="#3498db"
        )
        self.sample_canvas.pack(padx=10, pady=10)
        
        # Drawing canvas
        drawing_frame = tk.Frame(canvas_frame, bg="#34495e", relief=tk.RAISED, borderwidth=3)
        drawing_frame.grid(row=0, column=1, padx=10)
        
        drawing_title = tk.Label(
            drawing_frame,
            text="✏️ Your Drawing",
            font=("Arial", 12, "bold"),
            bg="#34495e",
            fg="#ecf0f1"
        )
        drawing_title.pack(pady=5)
        
        self.drawing_canvas = tk.Canvas(
            drawing_frame,
            width=350,
            height=350,
            bg="white",
            highlightthickness=2,
            highlightbackground="#2ecc71"
        )
        self.drawing_canvas.pack(padx=10, pady=10)
        
        # Bind mouse events for drawing
        self.drawing_canvas.bind("<Button-1>", self.start_drawing)
        self.drawing_canvas.bind("<B1-Motion>", self.draw)
        self.drawing_canvas.bind("<ButtonRelease-1>", self.stop_drawing)
        
        # Control buttons
        button_frame = tk.Frame(self.root, bg="#2c3e50")
        button_frame.pack(pady=15)
        
        clear_btn = tk.Button(
            button_frame,
            text="🗑️ Clear",
            font=("Arial", 12, "bold"),
            bg="#e67e22",
            fg="white",
            width=15,
            height=2,
            command=self.clear_drawing,
            cursor="hand2"
        )
        clear_btn.grid(row=0, column=0, padx=10)
        
        submit_btn = tk.Button(
            button_frame,
            text="✅ Submit",
            font=("Arial", 12, "bold"),
            bg="#3498db",
            fg="white",
            width=15,
            height=2,
            command=self.submit_drawing,
            cursor="hand2"
        )
        submit_btn.grid(row=0, column=1, padx=10)
        
        next_btn = tk.Button(
            button_frame,
            text="➡️ Next Pattern",
            font=("Arial", 12, "bold"),
            bg="#9b59b6",
            fg="white",
            width=15,
            height=2,
            command=self.load_random_pattern,
            cursor="hand2"
        )
        next_btn.grid(row=0, column=2, padx=10)
        
        # Instructions
        instructions = tk.Label(
            self.root,
            text="Draw the pattern shown on the left within 5 seconds! Timer starts automatically.",
            font=("Arial", 10),
            bg="#2c3e50",
            fg="#95a5a6"
        )
        instructions.pack(pady=5)
        
    def load_random_pattern(self):
        """Load a random pattern"""
        self.stop_timer()
        self.time_remaining = self.time_limit
        self.timer_label.config(text=f"Time: {self.time_limit}s")
        
        self.current_pattern = random.choice(list(self.patterns.keys()))
        self.pattern_label.config(text=f"Pattern: {self.current_pattern}")
        
        # Clear both canvases
        self.sample_canvas.delete("all")
        self.drawing_canvas.delete("all")
        self.has_drawn = False  # Reset drawing flag for new pattern
        
        # Draw the pattern on sample canvas - force update
        self.patterns[self.current_pattern](self.sample_canvas)
        self.sample_canvas.update_idletasks()  # Force canvas to redraw
        
        # Start timer after a short delay to ensure pattern is visible
        self.root.after(100, self.start_timer)
        
    def draw_circle_pattern(self, canvas):
        """Draw a simple circle"""
        canvas.create_oval(100, 100, 250, 250, outline="#2c3e50", width=4)
        
    def draw_star_pattern(self, canvas):
        """Draw a 5-pointed star"""
        cx, cy = 175, 175
        points = []
        for i in range(10):
            angle = i * 36 - 90
            r = 80 if i % 2 == 0 else 40
            x = cx + r * __import__('math').cos(__import__('math').radians(angle))
            y = cy + r * __import__('math').sin(__import__('math').radians(angle))
            points.extend([x, y])
        canvas.create_polygon(points, outline="#2c3e50", fill="", width=4)
        
    def draw_spiral_pattern(self, canvas):
        """Draw a spiral"""
        cx, cy = 175, 175
        points = []
        for i in range(200):
            angle = i * 10
            r = i * 0.4
            x = cx + r * __import__('math').cos(__import__('math').radians(angle))
            y = cy + r * __import__('math').sin(__import__('math').radians(angle))
            points.extend([x, y])
        canvas.create_line(points, fill="#2c3e50", width=3, smooth=True)
        
    def draw_zigzag_pattern(self, canvas):
        """Draw a zigzag pattern"""
        points = []
        for i in range(8):
            x = 50 + i * 40
            y = 120 if i % 2 == 0 else 230
            points.extend([x, y])
        canvas.create_line(points, fill="#2c3e50", width=4)
        
    def draw_smiley_pattern(self, canvas):
        """Draw a smiley face"""
        # Face
        canvas.create_oval(75, 75, 275, 275, outline="#2c3e50", width=4)
        # Eyes
        canvas.create_oval(130, 130, 160, 160, fill="#2c3e50")
        canvas.create_oval(190, 130, 220, 160, fill="#2c3e50")
        # Smile
        canvas.create_arc(120, 150, 230, 240, start=0, extent=-180, outline="#2c3e50", width=4, style=tk.ARC)
        
    def draw_triangle_pattern(self, canvas):
        """Draw an equilateral triangle"""
        canvas.create_polygon(175, 80, 80, 270, 270, 270, outline="#2c3e50", fill="", width=4)
        
    def draw_diamond_pattern(self, canvas):
        """Draw a diamond/rhombus shape"""
        # Simple diamond shape - more reliable than complex heart formula
        canvas.create_polygon(175, 80, 280, 175, 175, 270, 70, 175, outline="#2c3e50", fill="", width=4)
        
    def draw_wave_pattern(self, canvas):
        """Draw a wave pattern"""
        points = []
        for i in range(0, 350, 2):
            x = i + 20
            y = 175 + 60 * __import__('math').sin(i * 0.05)
            points.extend([x, y])
        canvas.create_line(points, fill="#2c3e50", width=4, smooth=True)
        
    def start_drawing(self, event):
        """Start drawing on mouse click"""
        self.drawing = True
        self.last_x = event.x
        self.last_y = event.y
        
    def draw(self, event):
        """Draw on mouse drag"""
        if self.drawing:
            if self.last_x and self.last_y:
                self.drawing_canvas.create_line(
                    self.last_x, self.last_y, event.x, event.y,
                    fill="#2c3e50", width=3, capstyle=tk.ROUND, smooth=True
                )
                self.has_drawn = True  # Mark that player has drawn something
            self.last_x = event.x
            self.last_y = event.y
            
    def stop_drawing(self, event):
        """Stop drawing on mouse release"""
        self.drawing = False
        self.last_x = None
        self.last_y = None
        
    def clear_drawing(self):
        """Clear the drawing canvas"""
        self.drawing_canvas.delete("all")
        self.has_drawn = False  # Reset the drawing flag
        
    def start_timer(self):
        """Start the countdown timer"""
        if not self.timer_running:
            self.timer_running = True
            self.update_timer()
            
    def stop_timer(self):
        """Stop the timer"""
        self.timer_running = False
        
    def update_timer(self):
        """Update the countdown timer"""
        if self.timer_running and self.time_remaining > 0:
            self.time_remaining -= 1
            self.timer_label.config(text=f"Time: {self.time_remaining}s")
            self.root.after(1000, self.update_timer)
        elif self.time_remaining <= 0:
            self.stop_timer()
            self.time_remaining = self.time_limit
            messagebox.showinfo("Time's Up!", "Time's up! You ran out of time to complete the pattern!")
            self.root.after(200, self.load_random_pattern)  # Delay loading next pattern
            
    def submit_drawing(self):
        """Submit the drawing and calculate score"""
        if not self.timer_running and self.time_remaining == self.time_limit:
            messagebox.showwarning("Not Started", "Please wait for the timer to start!")
            return
        
        # Check if player has drawn anything
        if not self.has_drawn:
            messagebox.showwarning("No Drawing", "Please draw something before submitting!")
            return
            
        self.stop_timer()
        self.attempts += 1
        
        # Simple scoring based on time remaining
        time_taken = self.time_limit - self.time_remaining
        
        # Base score calculation - faster drawing gets more points (15 second timer)
        if self.time_remaining >= 10:
            points = 150  # Completed in 5 seconds or less
        elif self.time_remaining >= 7:
            points = 120  # Completed in 5-8 seconds
        elif self.time_remaining >= 4:
            points = 90   # Completed in 8-11 seconds
        elif self.time_remaining >= 2:
            points = 60   # Completed in 11-13 seconds
        else:
            points = 30   # Completed in 13-15 seconds
            
        self.score += points
        self.score_label.config(text=f"Score: {self.score}")
        
        result_msg = f"Great effort! 🎨\n\n"
        result_msg += f"Pattern: {self.current_pattern}\n"
        result_msg += f"Time taken: {time_taken}s\n"
        result_msg += f"Points earned: {points}\n"
        result_msg += f"Total score: {self.score}\n"
        result_msg += f"Attempts: {self.attempts}"
        
        messagebox.showinfo("Drawing Submitted!", result_msg)
        
        # Load next pattern after a short delay
        self.root.after(200, self.load_random_pattern)

def main():
    root = tk.Tk()
    app = DoodleBuilder(root)
    root.mainloop()

if __name__ == "__main__":
    main()