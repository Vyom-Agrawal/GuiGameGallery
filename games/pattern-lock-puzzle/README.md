# Pattern Lock Memory Game 🔐

A challenging memory game inspired by smartphone pattern locks! Watch a pattern light up on a 3x3 grid, then replicate it by drawing the same pattern. The patterns get progressively longer as you advance through levels.

## 🎮 Game Features

- **Progressive Difficulty**: Each level increases the pattern length, starting from 3 dots and growing longer
- **Visual Feedback**: Clear animations show you the pattern, then highlight your input
- **Smooth Controls**: Click or drag across dots to draw your pattern
- **Level Tracking**: See your current level and pattern length as you progress
- **Modern UI**: Clean, dark-themed interface with neon accents

## 🕹️ How to Play

1. **Start the Game**: Click the "Start Game" button
2. **Watch Carefully**: A random pattern will light up on the 3x3 grid - memorize the sequence!
3. **Replicate the Pattern**: After the pattern disappears, draw the same pattern by:
   - **Clicking** on each dot in sequence, OR
   - **Dragging** your mouse across the dots in order
4. **Advance or Retry**: 
   - ✓ Correct pattern = advance to the next level with a longer pattern
   - ✗ Wrong pattern = game over! See your final level achieved
5. **Challenge Yourself**: Try to reach the highest level possible!

## 🚀 Requirements

- Python 3.x
- tkinter (usually included with Python)

## 📦 Installation & Running

1. Ensure Python 3 is installed on your system
2. Save `main.py` to a directory
3. Run the game:
   ```bash
   python main.py
   ```

## 🎯 Game Rules

- You must draw the pattern in the **exact same order** as shown
- Each dot can only be used **once** per pattern
- Release the mouse button to submit your pattern
- The pattern length increases by 1 with each level (starts at 3)

## 🎨 Visual Design

- **Dark Theme**: Easy on the eyes with a modern dark interface
- **Neon Accents**: Cyan highlights for active dots and lines
- **Color Feedback**:
  - 🔵 Blue: Default dot state
  - 🔷 Cyan: Active/selected dots
  - 🟢 Green: Correct pattern
  - 🔴 Red: Wrong pattern

## 🔧 Technical Details

- **Grid Size**: 3x3 dots (9 total positions)
- **Pattern Generation**: Random valid sequences
- **Input Methods**: Both click and drag are supported
- **Animation**: Smooth pattern preview with timed delays
- **State Management**: Tracks game state, user input, and level progression

## 🎓 Learning Opportunities

This project demonstrates:
- Tkinter Canvas drawing and event handling
- Game state management
- Animation with `after()` method
- Mouse event handling (click, drag, release)
- Pattern validation and comparison
- Dynamic UI updates

## 🌟 Possible Enhancements

- **Larger Grids**: 4x4 or 5x5 for extreme difficulty
- **Sound Effects**: Audio feedback for actions
- **Timer Challenge**: Complete patterns within a time limit
- **High Score**: Save and display best levels achieved
- **Difficulty Modes**: Easy, Medium, Hard with different starting lengths
- **Pattern Replay**: Show the correct pattern after failure
- **Custom Patterns**: Let users create and share patterns
- **Smooth Animations**: Add trail effects or particle animations

**Enjoy the challenge and test your memory skills!** 🧠✨