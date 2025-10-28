# 🌀 Fibonacci 2048

*A twist on the classic 2048 — powered by Fibonacci logic and Python’s Tkinter.*

## 🎮 Overview

This project reimagines the iconic **2048** game — but instead of powers of 2, tiles follow the **Fibonacci sequence**.

You combine *consecutive* Fibonacci numbers (like `2` and `3`, or `5` and `8`) to progress up the sequence. The goal: reach **987** on the 4×4 board.

Built completely in **Python (Tkinter)**, this version handles:

- A live score tracker
- Smooth GUI updates for each move
- Randomized tile spawns
- Win and game-over detection
- Logical Fibonacci validation for merges

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

That’s handled using a Fibonacci lookup table and index map for O(1) checks.

---

## 🧩 Controls

Use your **arrow keys** to slide tiles:

- ⬅️ Left
- ➡️ Right
- ⬆️ Up
- ⬇️ Down

New tiles (either `1` or `2`) appear randomly after each move.

---

## 🧱 Features

- **Dynamic Tkinter GUI** – updates colors, fonts, and tiles in real-time
- **Accurate Fibonacci merges** – consecutive-only combination logic
- **Adaptive tile generation** – random tile spawns on every move
- **Game-over detection** – checks for valid moves both horizontally and vertically
- **Simple, extensible structure** – clear modular methods for stacking, combining, and transposing the grid

---

## 🗂️ Project Structure

```
.
├── colors.py        # Color & font definitions for the grid (imported as 'c')
├── main.py      # Main game logic (this file)
└── README.md        # You’re reading it

```

> Note:
> 
> 
> The `colors.py` file defines all visual constants such as `CELL_COLORS`, `CELL_NUMBER_COLORS`, and fonts.
> 
> Make sure it exists in the same directory or import paths will fail.
> 

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

You win when a tile reaches **987** (the 16th Fibonacci number for a 4×4 board).

---

## 💡 Design Notes

- **Stacking logic** ensures all tiles slide fully left before and after merging.
- **Combination logic** uses a `FIB_INDEX` map to verify valid Fibonacci adjacency.
- **Transpose + reverse** tricks enable using the same logic for all directions (DRY principle).
- No external dependencies — just **Tkinter** and **random**.

---

**Made with Python, logic, and a bit of Fibonacci magic.**

---
