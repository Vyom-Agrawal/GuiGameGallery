# 🌀 Fibonacci 2048

*A twist on the classic 2048 — powered by Fibonacci logic and Python’s Tkinter.*

## 🎮 Overview

This project reimagines the iconic **2048** game — but instead of powers of 2, tiles follow the **Fibonacci sequence** and instead of sliding, you **click** to merge.

You can merge **two consecutive Fibonacci numbers** (like `2` and `3`, or `5` and `8`) by **clicking them one after another**.  
Your goal: reach **level maximum value** on the 4×4 board before you run out of moves.

Built completely in **Python (Tkinter)**, this version handles:

- A dynamic GUI
- Click-based merging
- Difficulty modes (Easy → Super Hard)
- Real-time scoring
- Win and game-over detection

---

## 🧮 Game Logic

Traditional 2048 merges identical tiles (`2 + 2 → 4`).

Here, merging happens only between **consecutive Fibonacci numbers** — and they sum up to the *next* Fibonacci value.

Example:

```
1 + 1 → 2
2 + 3 → 5
5 + 8 → 13
...

```

Tiles can only merge if:

- Both are Fibonacci numbers, and
- Their indices in the Fibonacci sequence differ by exactly 1.

---

## 🧩 Controls

- **Click any two tiles** that are consecutive Fibonacci numbers to merge them.  
- The result appears in the **second clicked** tile.  
- No new tiles are added — every move counts!  
- You can change **difficulty** at any time from the top menu:
  - Easy → target = 34  
  - Medium → target = 89  
  - Hard → target = 233  
  - Super Hard → target = 987  

---

## 🧱 Features

- **Interactive click-based gameplay**  
- **4 difficulty modes** with distinct Fibonacci targets  
- **Polished Tkinter GUI** with dynamic colors and fonts  
- **Real-time score updates**  
- **Automatic win/loss detection**  
- **Restart button** to reset instantly  

---

## 🗂️ Project Structure

```
.
├── main.py      # Main game logic
└── README.md        # You’re reading it

```
---

## 🚀 Running the Game

### Prerequisites

- Python 3.7+
- Tkinter

### Run

```bash
python main.py

```

The game window opens automatically.

---

## 🏆 Win Condition

You win when a tile reaches **the maximum value** for the level chosen. 
---

**Made with Python, logic, and a bit of Fibonacci magic.**

---
