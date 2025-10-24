import tkinter as tk
from tkinter import messagebox
import random
import time

class ColourMatchGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Colour Match Reaction")
        self.root.geometry("620x720")
        self.root.resizable(False, False)
        self.root.configure(bg="#2c3e50")
        
        # Color definitions
        self.colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange"]
        self.color_codes = {
            "Red": "#e74c3c",
            "Blue": "#3498db",
            "Green": "#2ecc71",
            "Yellow": "#f1c40f",
            "Purple": "#9b59b6",
            "Orange": "#e67e22"
        }
        
        # Game state
        self.total_rounds = 10
        self.current_round = 0
        self.correct_answers = 0
        self.incorrect_answers = 0
        self.reaction_times = []
        
        # Round tracking
        self.start_time = None  # Timestamp when round starts
        self.current_correct_color = None  # Font color (correct answer)
        self.game_active = False
        
        self.setup_ui()
        
    def setup_ui(self):
        # Title
        title_label = tk.Label(
            self.root,
            text="Colour Match Reaction",
            font=("Arial", 24, "bold"),
            bg="#2c3e50",
            fg="#ecf0f1"
        )
        title_label.pack(pady=20)
        
        # Instructions
        instructions = tk.Label(
            self.root,
            text="Click the button matching the FONT COLOR, not the word!",
            font=("Arial", 12),
            bg="#2c3e50",
            fg="#bdc3c7",
            wraplength=500
        )
        instructions.pack(pady=5)
        
        # Score frame
        self.score_frame = tk.Frame(self.root, bg="#2c3e50")
        self.score_frame.pack(pady=10)
        
        self.round_label = tk.Label(
            self.score_frame,
            text="Round: 0/10",
            font=("Arial", 12),
            bg="#2c3e50",
            fg="#ecf0f1"
        )
        self.round_label.grid(row=0, column=0, padx=20)
        
        self.score_label = tk.Label(
            self.score_frame,
            text="Correct: 0 | Incorrect: 0",
            font=("Arial", 12),
            bg="#2c3e50",
            fg="#ecf0f1"
        )
        self.score_label.grid(row=0, column=1, padx=20)
        
        # Color display label
        self.color_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 48, "bold"),
            bg="#34495e",
            width=15,
            height=2,
            relief=tk.RAISED,
            bd=3
        )
        self.color_label.pack(pady=30)
        
        # Buttons frame
        self.buttons_frame = tk.Frame(self.root, bg="#2c3e50")
        self.buttons_frame.pack(pady=20)
        
        self.color_buttons = {}
        for i, color in enumerate(self.colors):
            btn = tk.Button(
                self.buttons_frame,
                text=color,
                font=("Arial", 14, "bold"),
                width=10,
                height=2,
                bg=self.color_codes[color],
                fg="white",
                activebackground=self.color_codes[color],
                activeforeground="white",
                disabledforeground="white",
                relief=tk.RAISED,
                bd=2,
                cursor="hand2",
                state=tk.DISABLED,
                command=lambda c=color: self.check_answer(c)
            )
            row = i // 3
            col = i % 3
            btn.grid(row=row, column=col, padx=10, pady=10)
            self.color_buttons[color] = btn
        
        # Control buttons
        control_frame = tk.Frame(self.root, bg="#2c3e50")
        control_frame.pack(pady=20)
        
        self.start_button = tk.Button(
            control_frame,
            text="Start Game",
            font=("Arial", 14, "bold"),
            bg="#7f8c8d",
            fg="white",
            activeforeground="white",
            relief=tk.RAISED,
            bd=2,
            width=12,
            height=2,
            cursor="hand2",
            command=self.start_game
        )
        self.start_button.grid(row=0, column=0, padx=10)
        
        self.restart_button = tk.Button(
            control_frame,
            text="Restart",
            font=("Arial", 14, "bold"),
            bg="#7f8c8d",
            fg="white",
            activeforeground="white",
            disabledforeground="white",
            relief=tk.RAISED,
            bd=2,
            width=12,
            height=2,
            cursor="hand2",
            state=tk.DISABLED,
            command=self.restart_game
        )
        self.restart_button.grid(row=0, column=1, padx=10)
    
    def start_game(self):
        """Initialize a new game session"""
        self.game_active = True
        self.current_round = 0
        self.correct_answers = 0
        self.incorrect_answers = 0
        self.reaction_times = []
        
        self.start_button.config(state=tk.DISABLED)
        self.restart_button.config(state=tk.DISABLED)
        
        # Enable color selection buttons
        for btn in self.color_buttons.values():
            btn.config(state=tk.NORMAL)
        
        self.next_round()
    
    def next_round(self):
        """Set up and display the next challenge"""
        if self.current_round >= self.total_rounds:
            self.end_game()
            return
        
        self.current_round += 1
        self.update_score()
        
        # Pick random word and random color (Stroop effect - they can be different!)
        color_word = random.choice(self.colors)
        font_color = random.choice(self.colors)
        
        # The correct answer is always the FONT COLOR, not the word
        self.current_correct_color = font_color
        
        # Display the word in the chosen font color
        self.color_label.config(
            text=color_word,
            fg=self.color_codes[font_color]
        )
        
        # Start timing the reaction
        self.start_time = time.time()
    
    def check_answer(self, selected_color):
        """Validate player's choice and record reaction time"""
        if not self.game_active:
            return
        
        # Calculate how fast the player responded
        reaction_time = time.time() - self.start_time
        self.reaction_times.append(reaction_time)
        
        # Check if the selected color matches the font color
        if selected_color == self.current_correct_color:
            self.correct_answers += 1
            self.flash_feedback(True)
        else:
            self.incorrect_answers += 1
            self.flash_feedback(False)
        
        # Move to next round after brief visual feedback
        self.root.after(500, self.next_round)
    
    def flash_feedback(self, is_correct):
        original_bg = self.color_label.cget("bg")
        feedback_color = "#2ecc71" if is_correct else "#e74c3c"
        self.color_label.config(bg=feedback_color)
        self.root.after(300, lambda: self.color_label.config(bg=original_bg))
    
    def update_score(self):
        self.round_label.config(text=f"Round: {self.current_round}/{self.total_rounds}")
        self.score_label.config(
            text=f"Correct: {self.correct_answers} | Incorrect: {self.incorrect_answers}"
        )
    
    def end_game(self):
        """Display results and calculate final score"""
        self.game_active = False
        
        # Disable color buttons
        for btn in self.color_buttons.values():
            btn.config(state=tk.DISABLED)
        
        # Clear the color label
        self.color_label.config(text="Game Over!", fg="#ecf0f1")
        
        # Calculate statistics
        avg_time = sum(self.reaction_times) / len(self.reaction_times) if self.reaction_times else 0
        
        # Scoring: base points + bonus for fast reactions
        base_score = self.correct_answers * 100
        speed_bonus = max(0, int((2.0 - avg_time) * 50)) if avg_time < 2.0 else 0
        total_score = base_score + speed_bonus
        
        # Show results
        result_message = (
            f"Game Complete!\n\n"
            f"Rounds: {self.total_rounds}\n"
            f"Correct: {self.correct_answers}\n"
            f"Incorrect: {self.incorrect_answers}\n"
            f"Accuracy: {(self.correct_answers/self.total_rounds)*100:.1f}%\n\n"
            f"Average Reaction Time: {avg_time:.3f}s\n"
            f"Best Time: {min(self.reaction_times):.3f}s\n"
            f"Worst Time: {max(self.reaction_times):.3f}s\n\n"
            f"Base Score: {base_score}\n"
            f"Speed Bonus: {speed_bonus}\n"
            f"Total Score: {total_score}"
        )
        
        messagebox.showinfo("Game Results", result_message)
        
        # Enable restart button
        self.restart_button.config(state=tk.NORMAL)
    
    def restart_game(self):
        self.color_label.config(text="", bg="#34495e")
        self.start_button.config(state=tk.NORMAL)
        self.restart_button.config(state=tk.DISABLED)
        self.current_round = 0
        self.correct_answers = 0
        self.incorrect_answers = 0
        self.update_score()

if __name__ == "__main__":
    root = tk.Tk()
    game = ColourMatchGame(root)
    root.mainloop()