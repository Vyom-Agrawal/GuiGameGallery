# Mirror Maze 🪞

A challenging grid-based puzzle game where your controls are mirrored! Navigate through a randomly generated maze while adapting to inverted movement controls.

## 🎮 Game Concept

In Mirror Maze, pressing arrow keys doesn't do what you expect. The controls are mirrored based on the current mirror mode:
- **Vertical Mode**: Up becomes Down, Down becomes Up
- **Horizontal Mode**: Left becomes Right, Right becomes Left
- **Both Mode**: All directions are inverted!

Your goal is to reach the red EXIT marker while adapting to these counterintuitive controls.

## 🕹️ How to Play

### Controls
- **Arrow Keys** - Move your character (but remember, they're mirrored!)
- **R** - Restart the game with a new maze
- **U** - Undo last move (costs 1 move)

### Objective
Navigate from the green starting position (top-left) to the red EXIT (bottom-right) in the fewest moves possible.

### Game Elements
- 🔵 **Blue Circle** - Your character
- 🟢 **Green Dot** - Starting position
- 🔴 **Red Square** - Exit/Goal
- ⬜ **Light Gray** - Path (walkable)
- ⬛ **Dark Gray** - Walls (blocked)

## 🚀 Installation & Running

### Prerequisites
- Python 3.6 or higher
- Tkinter (usually comes pre-installed with Python)

### Running the Game
```bash
python main.py
```

Or on some systems:
```bash
python3 main.py
```

## 🎯 Features

- **Randomly Generated Mazes** - Every game is different
- **Three Mirror Modes** - Vertical, Horizontal, or Both axes
- **Move Counter** - Track your efficiency
- **Timer** - See how long it takes you
- **Undo Function** - Made a mistake? Press 'U' to undo
- **Quick Restart** - Press 'R' or click the Restart button
- **Change Mirror Mode** - Switch mirror modes mid-game for extra challenge

## 💡 Tips & Strategy

1. **Think Backwards** - When you want to go up, press down
2. **Practice Mode** - Start with vertical or horizontal mirroring before trying "both"
3. **Plan Ahead** - Look at the path before moving
4. **Use Undo Wisely** - It counts as a move, so plan carefully
5. **Corner Strategy** - Dead ends can trap you more easily with mirrored controls
6. **Muscle Memory** - Your intuition will fight you - stay focused!

## 🎨 Customization

You can modify the game by editing these constants in `main.py`:

```python
self.GRID_SIZE = 15        # Size of the maze (15x15 grid)
self.CELL_SIZE = 40        # Size of each cell in pixels
```

Colors can be customized in the color constants:
```python
self.COLOR_BG = "#2C3E50"      # Background
self.COLOR_WALL = "#34495E"    # Walls
self.COLOR_PATH = "#ECF0F1"    # Walkable paths
self.COLOR_PLAYER = "#3498DB"  # Player color
self.COLOR_START = "#2ECC71"   # Start marker
self.COLOR_EXIT = "#E74C3C"    # Exit marker
```

## 🏆 Challenge Modes

Try these self-imposed challenges:
1. **Speed Run** - Complete in under 30 seconds
2. **Minimal Moves** - Complete in under 50 moves
3. **No Undo** - Complete without using undo
4. **Both Mode Only** - Only play with both axes mirrored
5. **Marathon** - Complete 5 mazes in a row

## 📋 Requirements

```
Python 3.6+
tkinter (standard library)
```

## 🐛 Troubleshooting

**Game doesn't start:**
- Ensure Python 3.6+ is installed
- Check that Tkinter is installed: `python -m tkinter`

**Controls not responding:**
- Make sure the game window has focus (click on it)
- Try pressing keys more deliberately

**Maze generation issues:**
- This is rare, but if you get an unsolvable maze, press 'R' to restart

## 📝 Technical Details

- **Maze Generation**: Uses recursive backtracking algorithm
- **GUI Framework**: Python Tkinter
- **Grid System**: 15x15 cells (customizable)
- **Path Finding**: Ensures solvable path from start to exit

## 🎓 Learning Concepts

This game demonstrates:
- Canvas drawing and manipulation
- Event handling (keyboard input)
- Algorithm implementation (maze generation)
- Game state management
- Timer and counter mechanics
- Adaptive difficulty (mirror modes)

## 🌟 Possible Enhancements

- Add difficulty levels (larger mazes)
- Implement high score tracking
- Add sound effects
- Create power-ups (temporary normal controls)
- Add multiplayer mode

---

**Have fun adapting to the mirror world!** 🪞🎮
