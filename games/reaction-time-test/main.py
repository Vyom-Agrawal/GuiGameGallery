import tkinter as tk
from tkinter import ttk, messagebox
import random
import time
from statistics import mean

# Config
WINDOW_W = 800
WINDOW_H = 600
MIN_DELAY = 1.5    # minimum wait before green (seconds)
MAX_DELAY = 4.0    # maximum wait before green (seconds)

class ReactionTestApp:
    def __init__(self, root):
        self.root = root
        root.title("Reaction Time Test")
        root.geometry(f"{WINDOW_W}x{WINDOW_H}")

        self.state = "idle"  # idle, waiting, ready
        self.start_time = None
        self.after_id = None
        self.trials = []  # list of ms (float), 'Too soon' trials stored as None

        self._build_ui()
        self._bind_keys()

    def _build_ui(self):
        # Top frame for instructions
        top = ttk.Frame(self.root, padding=(12, 8))
        top.pack(fill="x")
        self.instr = ttk.Label(top, text="Click the big area to begin.", anchor="center", font=("Helvetica", 12))
        self.instr.pack(fill="x")

        # Big clickable area
        self.area = tk.Canvas(self.root, bg="#00b0ff", highlightthickness=0)
        self.area.pack(expand=True, fill="both", padx=20, pady=10)
        self.area_text = self.area.create_text(WINDOW_W//2, WINDOW_H//2 - 30, text="Click to begin",
                                               fill="white", font=("Helvetica", 24, "bold"))
        self.area.bind("<Button-1>", self.on_click)
        self.area.bind("<Return>", lambda e: self.on_click(e))
        # small hint
        self.hint_text = self.area.create_text(WINDOW_W//2, WINDOW_H//2 + 20,
                                               text="(or press Space / Enter)", fill="white", font=("Helvetica", 12))

        # Bottom frame for stats and controls
        bottom = ttk.Frame(self.root, padding=(12, 8))
        bottom.pack(fill="x")

        # Stats labels
        stats_frame = ttk.Frame(bottom)
        stats_frame.pack(side="left", fill="x", expand=True)

        self.last_label = ttk.Label(stats_frame, text="Last: — ms", font=("Helvetica", 11))
        self.last_label.pack(anchor="w")
        self.best_label = ttk.Label(stats_frame, text="Best: — ms", font=("Helvetica", 11))
        self.best_label.pack(anchor="w")
        self.avg_label = ttk.Label(stats_frame, text="Average: — ms", font=("Helvetica", 11))
        self.avg_label.pack(anchor="w")

        # History listbox
        hist_frame = ttk.Frame(bottom)
        hist_frame.pack(side="right", fill="y")
        ttk.Label(hist_frame, text="History").pack()
        self.histbox = tk.Listbox(hist_frame, height=6, width=18)
        self.histbox.pack(side="left", fill="y")
        scrollbar = ttk.Scrollbar(hist_frame, orient="vertical", command=self.histbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.histbox.config(yscrollcommand=scrollbar.set)

        # Controls under the history
        ctrl_frame = ttk.Frame(self.root, padding=(12, 6))
        ctrl_frame.pack(fill="x")
        self.reset_btn = ttk.Button(ctrl_frame, text="Clear History", command=self.clear_history)
        self.reset_btn.pack(side="left")
        ttk.Label(ctrl_frame, text="  ").pack(side="left")  # spacer
        self.info_btn = ttk.Button(ctrl_frame, text="How it works", command=self.show_info)
        self.info_btn.pack(side="left")

    def _bind_keys(self):
        # Bind keyboard to root for global handling
        self.root.bind("<space>", self.on_click)
        self.root.bind("<Return>", self.on_click)

    def on_click(self, event=None):
        # Clicking behavior depends on state
        if self.state == "idle":
            # Start waiting period
            self._start_wait()
        elif self.state == "waiting":
            # Clicked too early
            self._cancel_wait(too_soon=True)
        elif self.state == "ready":
            # Measure reaction
            self._record_reaction()

    def _start_wait(self):
        # Change visual to waiting (red)
        self.state = "waiting"
        self._set_area_style(bg="#b30000", text="Wait for green...", hint="")
        # schedule green after random delay
        delay = random.uniform(MIN_DELAY, MAX_DELAY)
        self.after_id = self.root.after(int(delay * 1000), self._go_green)

    def _cancel_wait(self, too_soon=False):
        # Called when user clicks too early
        if self.after_id:
            self.root.after_cancel(self.after_id)
            self.after_id = None
        self.state = "idle"
        if too_soon:
            # record a failed trial (None)
            self.trials.append(None)
            self._add_history_entry(None)
            self._update_stats()
            # show 'Too soon' feedback briefly
            self._set_area_style(bg="#444444", text="Too soon! Click to try again", hint="Don't click until it turns green.")
        else:
            self._set_area_style(bg="#2b2b2b", text="Click to begin", hint="(or press Space / Enter)")

    def _go_green(self):
        # Signal user to click now
        self.after_id = None
        self.state = "ready"
        self.start_time = time.perf_counter()
        self._set_area_style(bg="#1b8a1b", text="Click!", hint="Click or press Space/Enter")
        # optionally provide small beep? (no external libs, so skip)

    def _record_reaction(self):
        if self.start_time is None:
            return
        elapsed = (time.perf_counter() - self.start_time) * 1000.0  # milliseconds
        self.trials.append(elapsed)
        self._add_history_entry(elapsed)
        self._update_stats()
        # show result briefly then reset to idle
        self._set_area_style(bg="#00b0ff", text=f"{int(elapsed)} ms", hint="Click to try again")
        self.state = "idle"
        self.start_time = None

    def _set_area_style(self, bg="#2b2b2b", text="", hint=""):
        # update canvas appearance responsively
        self.area.configure(bg=bg)
        self.area.itemconfigure(self.area_text, text=text, fill=self._contrasting_text_color(bg))
        self.area.itemconfigure(self.hint_text, text=hint, fill=self._contrasting_hint_color(bg))

    def _contrasting_text_color(self, bg_hex):
        # simple luminance-based contrast: return white or black text
        # bg_hex like "#rrggbb"
        try:
            h = bg_hex.lstrip("#")
            r = int(h[0:2], 16)
            g = int(h[2:4], 16)
            b = int(h[4:6], 16)
            luminance = (0.299*r + 0.587*g + 0.114*b)
            return "black" if luminance > 186 else "white"
        except Exception:
            return "white"

    def _contrasting_hint_color(self, bg_hex):
        # slightly dimmer than main text
        tc = self._contrasting_text_color(bg_hex)
        return "#dddddd" if tc == "white" else "#333333"

    def _add_history_entry(self, value):
        if value is None:
            label = "Too soon!"
        else:
            label = f"{int(value)} ms"
        self.histbox.insert(0, label)  # newest at top

    def _update_stats(self):
        # Build list of successful times only
        good = [t for t in self.trials if isinstance(t, float) or isinstance(t, int)]
        if good:
            last = int(good[-1])
            best = int(min(good))
            avgv = int(mean(good))
            self.last_label.config(text=f"Last: {last} ms")
            self.best_label.config(text=f"Best: {best} ms")
            self.avg_label.config(text=f"Average: {avgv} ms")
        else:
            self.last_label.config(text="Last: — ms")
            self.best_label.config(text="Best: — ms")
            self.avg_label.config(text="Average: — ms")

    def clear_history(self):
        if messagebox.askyesno("Clear history", "Clear all recorded trials?"):
            self.trials.clear()
            self.histbox.delete(0, tk.END)
            self._update_stats()
            # reset area
            self.state = "idle"
            if self.after_id:
                self.root.after_cancel(self.after_id)
                self.after_id = None
            self._set_area_style(bg="#2b2b2b", text="Click to begin", hint="(or press Space / Enter)")

    def show_info(self):
        messagebox.showinfo(
            "How it works",
            "1. Click the big area (or press Space/Enter) to start.\n"
            "2. Wait until the box turns green. A random delay of ~1.5–4s.\n"
            "3. When it turns green, click as fast as you can.\n"
            "Early clicks are marked 'Too soon!'.\n"
            "Your reaction times are shown in milliseconds; the best and average are tracked."
        )

def main():
    root = tk.Tk()
    style = ttk.Style(root)
    # Optional: use a platform default theme for nicer widgets
    try:
        style.theme_use("clam")
    except Exception:
        pass
    app = ReactionTestApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
