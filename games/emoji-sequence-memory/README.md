# 🧠 Emoji Sequence Memory Game

A fun and challenging memory game built with Python Tkinter where you must remember and repeat increasingly longer sequences of emojis!

## 🎮 Game Description

Test your memory skills by watching sequences of emojis flash on screen, then reproducing them in the correct order. Each round adds a new emoji to the sequence, making it progressively more challenging!

## ✨ Features

- **Progressive Difficulty**: Each round adds one more emoji to remember
- **Visual Feedback**: Clear display of sequences with timed animations
- **Score System**: Earn points based on the round number (Round × 10 points)
- **12 Unique Emojis**: Diverse emoji set for varied sequences
- **User-Friendly Interface**: Clean, modern UI with clear instructions
- **Game Statistics**: Track your current round and total score

## 🕹️ How to Play

1. **Start**: Click the "Start Game" button to begin
2. **Watch**: Observe the emoji sequence as it flashes on screen (each emoji shows for 0.8 seconds)
3. **Remember**: Memorize the order of emojis shown
4. **Repeat**: Click the emoji buttons below to recreate the sequence
5. **Submit**: Press "Submit" when you're confident in your answer
6. **Progress**: If correct, you advance to the next round with a longer sequence!

### Controls

- **Start Game**: Begin a new game
- **Submit**: Check if your sequence matches the shown sequence
- **Clear**: Remove all emojis from your current input

## 📋 Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)

## 🚀 Installation & Running

1. Ensure Python 3.x is installed on your system
2. Save the code as `main.py`
3. Run the game:
   ```bash
   python main.py
   ```

## 🎯 Scoring

- Each completed round earns you: **Round Number × 10 points**
- Example: Completing Round 5 gives you 50 points
- Challenge yourself to achieve the highest score possible!

## 🎨 Game Interface

The game features:
- **Dark theme** for comfortable viewing
- **Large emoji display** for easy visibility
- **Color-coded status messages** (red for instructions, green for success)
- **Grid layout** of emoji buttons for easy selection
- **Real-time feedback** on your current sequence

## 🧩 Emoji Set

The game includes 12 different emojis:
😀 😎 🤔 😍 🥳 😴 🤯 🥺 😈 🤖 👻 🦄

## 💡 Tips

- Focus on creating memorable patterns or stories with the emojis
- Try saying the emojis out loud as they appear
- Start with visualization techniques to remember longer sequences
- Practice makes perfect - your memory will improve with each game!

## 🐛 Troubleshooting

**Emojis not displaying correctly?**
- Ensure your system supports emoji rendering
- Try updating your Python version
- On some systems, emoji display depends on system fonts

**Game running too fast/slow?**
- You can modify the timing in the code by adjusting the `after()` delays in the `show_sequence()` method

## 🔧 Customization

You can easily customize the game by modifying:
- `self.emojis` list: Add or change emojis
- Timing values in `show_sequence()`: Adjust flash duration (currently 800ms display, 400ms gap)
- Scoring formula in `check_sequence()`: Change point calculation
- Window size: Modify `geometry()` in `__init__`
- Color scheme: Update `bg` and `fg` parameters

## 🎉 Enjoy!

Have fun testing and improving your memory skills!