import tkinter as tk
from tkinter import messagebox
import random

class EmojiMemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Emoji Sequence Memory Game")
        self.root.geometry("570x720")
        self.root.resizable(False, False)
        self.root.configure(bg="#2C3E50")
        
        # Game data
        self.emojis = ["😀", "😎", "🤔", "😍", "🥳", "😴", "🤯", "🥺", "😈", "🤖", "👻", "🦄"]
        self.sequence = []  # Correct sequence shown to player
        self.user_sequence = []  # Player's input
        self.round_num = 0
        self.score = 0
        
        # Game state flags
        self.is_playing = False
        self.is_showing = False  # True when displaying sequence
        
        # Timing controls (in milliseconds)
        self.show_speed = 800  # How long each emoji is displayed
        self.pause_speed = 400  # Pause between emojis
        
        self.setup_ui()
        
        # Keyboard shortcuts
        self.root.bind('<Return>', lambda e: self.check_sequence() if self.submit_button['state'] == tk.NORMAL else None)
        self.root.bind('<Escape>', lambda e: self.clear_user_sequence() if self.clear_button['state'] == tk.NORMAL else None)
        
    def setup_ui(self):
        title_label = tk.Label(
            self.root,
            text="🧠 Emoji Sequence Memory 🧠",
            font=("Arial", 18, "bold"),
            bg="#2C3E50",
            fg="#ECF0F1"
        )
        title_label.pack(pady=10)
        
        info_frame = tk.Frame(self.root, bg="#2C3E50")
        info_frame.pack(pady=5)
        
        self.round_label = tk.Label(
            info_frame,
            text="Round: 0",
            font=("Arial", 13),
            bg="#2C3E50",
            fg="#3498DB"
        )
        self.round_label.pack(side=tk.LEFT, padx=15)
        
        self.score_label = tk.Label(
            info_frame,
            text="Score: 0",
            font=("Arial", 14),
            bg="#2C3E50",
            fg="#2ECC71"
        )
        self.score_label.pack(side=tk.LEFT, padx=15)
        
        self.display_frame = tk.Frame(self.root, bg="#34495E", height=120)
        self.display_frame.pack(pady=10, padx=40, fill=tk.BOTH)
        self.display_frame.pack_propagate(False)
        
        self.display_label = tk.Label(
            self.display_frame,
            text="Click 'Start' to begin!",
            font=("Arial", 36),
            bg="#34495E",
            fg="#ECF0F1"
        )
        self.display_label.pack(expand=True)
        
        self.status_label = tk.Label(
            self.root,
            text="Watch the sequence, then repeat it!\n(Press Enter to Submit, Esc to Clear)",
            font=("Arial", 12),
            bg="#2C3E50",
            fg="#E74C3C"
        )
        self.status_label.pack(pady=5)
        
        input_label = tk.Label(
            self.root,
            text="Your Sequence:",
            font=("Arial", 12, "bold"),
            bg="#2C3E50",
            fg="#ECF0F1"
        )
        input_label.pack(pady=(10, 3))
        
        user_frame = tk.Frame(self.root, bg="#34495E")
        user_frame.pack(pady=3)
        
        self.user_display_label = tk.Label(
            user_frame,
            text="",
            font=("Arial", 20),
            bg="#34495E",
            fg="#ECF0F1",
            height=2,
            width=25,
            wraplength=500,
            justify=tk.CENTER
        )
        self.user_display_label.pack(padx=8, pady=8)
        
        emoji_frame = tk.Frame(self.root, bg="#2C3E50")
        emoji_frame.pack(pady=10)
        
        self.emoji_buttons = []
        for i, emoji in enumerate(self.emojis):
            btn = tk.Button(
                emoji_frame,
                text=emoji,
                font=("Arial", 24),
                width=3,
                height=1,
                command=lambda e=emoji, b=None: self.add_emoji_to_sequence(e, b),
                state=tk.DISABLED,
                bg="#95A5A6",
                activebackground="#7F8C8D",
                relief=tk.RAISED,
                bd=2
            )
            btn.grid(row=i // 4, column=i % 4, padx=4, pady=4)
            btn.config(command=lambda e=emoji, b=btn: self.add_emoji_to_sequence(e, b))
            self.emoji_buttons.append(btn)
        
        control_frame = tk.Frame(self.root, bg="#2C3E50")
        control_frame.pack(pady=10)
        
        self.start_button = tk.Button(
            control_frame,
            text="Start Game",
            font=("Arial", 11, "bold"),
            bg="#2ECC71",
            fg="white",
            width=10,
            height=1,
            command=self.start_game
        )
        self.start_button.pack(side=tk.LEFT, padx=5)
        
        self.submit_button = tk.Button(
            control_frame,
            text="Submit",
            font=("Arial", 11, "bold"),
            bg="#3498DB",
            fg="white",
            width=10,
            height=1,
            command=self.check_sequence,
            state=tk.DISABLED
        )
        self.submit_button.pack(side=tk.LEFT, padx=5)
        
        self.clear_button = tk.Button(
            control_frame,
            text="Clear",
            font=("Arial", 11, "bold"),
            bg="#E67E22",
            fg="white",
            width=10,
            height=1,
            command=self.clear_user_sequence,
            state=tk.DISABLED
        )
        self.clear_button.pack(side=tk.LEFT, padx=5)
        
    def start_game(self):
        """Initialize or restart the game"""
        if self.is_playing:
            if not messagebox.askyesno("Restart Game", "Are you sure you want to restart?"):
                return
        
        # Reset game state
        self.is_playing = True
        self.round_num = 0
        self.score = 0
        self.sequence = []
        self.user_sequence = []
        self.update_display()
        self.user_display_label.config(text="")
        self.start_button.config(state=tk.DISABLED, text="Playing...")
        self.next_round()
        
    def next_round(self):
        """Start a new round by adding one emoji to the sequence"""
        if not self.is_playing:
            return
            
        self.round_num += 1
        self.update_display()
        
        # Add random emoji to sequence
        new_emoji = random.choice(self.emojis)
        self.sequence.append(new_emoji)
        
        # Increase difficulty after round 5
        if self.round_num > 5:
            self.show_speed = max(500, 800 - (self.round_num - 5) * 30)
            self.pause_speed = max(200, 400 - (self.round_num - 5) * 20)
        
        self.set_emoji_buttons_state(tk.DISABLED)
        self.submit_button.config(state=tk.DISABLED)
        self.clear_button.config(state=tk.DISABLED)
        
        self.status_label.config(
            text=f"Watch carefully! (Round {self.round_num})\n(Press Enter to Submit, Esc to Clear)", 
            fg="#E74C3C"
        )
        self.user_sequence = []
        self.user_display_label.config(text="")
        
        self.root.after(500, lambda: self.show_sequence(0))
        
    def show_sequence(self, index):
        """Recursively display each emoji in the sequence"""
        if not self.is_playing:
            return
            
        if index < len(self.sequence):
            self.is_showing = True
            emoji = self.sequence[index]
            self.display_label.config(text=emoji)
            self.root.after(self.show_speed, lambda: self.clear_display(index))
        else:
            # Sequence finished - enable user input
            self.is_showing = False
            self.status_label.config(
                text="Now repeat the sequence!\n(Press Enter to Submit, Esc to Clear)", 
                fg="#2ECC71"
            )
            self.set_emoji_buttons_state(tk.NORMAL)
            self.submit_button.config(state=tk.NORMAL)
            self.clear_button.config(state=tk.NORMAL)
            
    def clear_display(self, index):
        if not self.is_playing:
            return
        self.display_label.config(text="")
        self.root.after(self.pause_speed, lambda: self.show_sequence(index + 1))
        
    def add_emoji_to_sequence(self, emoji, button):
        """Handle emoji button click - add to user's sequence"""
        if not self.is_showing and self.is_playing:
            self.user_sequence.append(emoji)
            self.user_display_label.config(text=" ".join(self.user_sequence))
            
            # Visual feedback: flash button
            original_bg = button.cget('bg')
            button.config(bg="#3498DB")
            self.root.after(150, lambda: button.config(bg=original_bg) if button.winfo_exists() else None)
            
            # Auto-submit when sequence is complete
            if len(self.user_sequence) == len(self.sequence):
                self.root.after(300, self.check_sequence)
            
    def clear_user_sequence(self):
        self.user_sequence = []
        self.user_display_label.config(text="")
        
    def check_sequence(self):
        """Validate user's answer and proceed accordingly"""
        if not self.is_playing or len(self.user_sequence) == 0:
            return
            
        # Disable buttons during check
        self.set_emoji_buttons_state(tk.DISABLED)
        self.submit_button.config(state=tk.DISABLED)
        self.clear_button.config(state=tk.DISABLED)
        
        if len(self.user_sequence) != len(self.sequence):
            self.game_over("Wrong length! You need to match the exact sequence.")
            return
            
        if self.user_sequence == self.sequence:
            # Correct answer - award points and continue
            self.score += self.round_num * 10
            self.update_display()
            
            self.status_label.config(text="✓ Correct! Get ready for next round...", fg="#2ECC71")
            self.display_label.config(text="✓", fg="#2ECC71")
            
            self.root.after(1500, self.next_round)
        else:
            self.game_over("Wrong sequence! Try again.")
            
    def game_over(self, reason):
        self.is_playing = False
        self.set_emoji_buttons_state(tk.DISABLED)
        self.submit_button.config(state=tk.DISABLED)
        self.clear_button.config(state=tk.DISABLED)
        
        correct = " ".join(self.sequence)
        user = " ".join(self.user_sequence) if self.user_sequence else "(empty)"
        
        rounds_completed = max(0, self.round_num - 1)
        
        message = f"{reason}\n\n"
        message += f"Final Score: {self.score}\n"
        message += f"Rounds Completed: {rounds_completed}\n\n"
        message += f"Correct sequence:\n{correct}\n\n"
        message += f"Your answer:\n{user}"
        
        messagebox.showinfo("Game Over", message)
        
        self.display_label.config(text="Game Over!", fg="#ECF0F1")
        self.status_label.config(
            text="Click 'Start Game' to play again\n(Press Enter to Submit, Esc to Clear)", 
            fg="#E74C3C"
        )
        self.start_button.config(state=tk.NORMAL, text="Start Game")
        
        self.show_speed = 800
        self.pause_speed = 400
        
    def set_emoji_buttons_state(self, state):
        for btn in self.emoji_buttons:
            btn.config(state=state)
            
    def update_display(self):
        self.round_label.config(text=f"Round: {self.round_num}")
        self.score_label.config(text=f"Score: {self.score}")

if __name__ == "__main__":
    root = tk.Tk()
    game = EmojiMemoryGame(root)
    root.mainloop()