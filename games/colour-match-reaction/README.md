# Colour Match Reaction Game

A fast-paced brain-training game that challenges your ability to identify font colors while ignoring the written word. Test your reaction time and focus!

## 🎮 Game Description

In Colour Match Reaction, you'll see color names displayed on screen (like "BLUE"), but here's the twist: the word is written in a different color (e.g., "BLUE" in red font). Your challenge is to click the button that matches the **font color**, not what the word says!

## 🎯 How to Play

1. **Start the Game**: Click the "Start Game" button to begin
2. **Read Carefully**: A color word will appear in a colored font
3. **Choose Wisely**: Click the button matching the **font color** (not the word)
4. **React Quickly**: Your reaction time is being measured!
5. **Complete 10 Rounds**: Finish all rounds to see your final score
6. **Restart**: Click "Restart" to play again and beat your score

## ✨ Features

- **10 Challenging Rounds**: Each round presents a new color/word combination
- **6 Colors**: Red, Blue, Green, Yellow, Purple, and Orange
- **Reaction Time Tracking**: Measures how fast you respond to each challenge
- **Visual Feedback**: Screen flashes green for correct answers, red for incorrect
- **Detailed Statistics**: View your accuracy, average/best/worst reaction times
- **Score System**: 
  - 100 points per correct answer
  - Speed bonus for reaction times under 2 seconds
- **Instant Results**: See comprehensive game statistics at the end

## 🚀 Requirements

- Python 3.6 or higher
- tkinter (usually comes pre-installed with Python)

## 📦 Installation & Running

1. Make sure Python is installed on your system
2. Save `main.py` to a folder
3. Open terminal/command prompt in that folder
4. Run the game:

```bash
python main.py
```

## 🎨 Game Interface

- **Title Bar**: Shows the game name
- **Instructions**: Reminds you to click the font color, not the word
- **Score Display**: Shows current round and correct/incorrect answers
- **Color Display Area**: Large text showing the color word in various colors
- **6 Color Buttons**: Click these to select your answer
- **Control Buttons**: Start Game and Restart buttons

## 🏆 Scoring System

- **Base Score**: 100 points for each correct answer
- **Speed Bonus**: Up to 50 additional points for reaction times under 2 seconds
- **Accuracy Percentage**: Tracks how many you got right
- **Performance Stats**: Average, best, and worst reaction times

## 💡 Tips for High Scores

1. **Focus on the Color**: Train your brain to ignore what the word says
2. **React Quickly**: The faster you respond (accurately), the higher your score
3. **Stay Calm**: Don't let mistakes throw you off
4. **Practice**: Your brain will get better at separating color from text with practice

## 🔧 Customization

You can easily modify the game by editing `main.py`:

- **Change total rounds**: Modify `self.total_rounds = 10`
- **Add more colors**: Add entries to `self.colors` and `self.color_codes` lists
- **Adjust scoring**: Modify the scoring logic in the `end_game()` method
- **Change window size**: Modify `self.root.geometry("600x500")`

## 🐛 Troubleshooting

**Game won't start:**
- Ensure Python 3.6+ is installed
- Check that tkinter is available: `python -m tkinter`

**Colors look wrong:**
- Your system may use different color rendering
- The game should still be fully playable

## 📝 License

Free to use and modify for personal and educational purposes.

## 🎓 Educational Value

This game is based on the **Stroop Effect**, a psychological phenomenon where reading interferes with color identification. It's great for:
- Improving cognitive flexibility
- Training selective attention
- Developing faster reaction times
- Understanding brain processing conflicts

---

**Enjoy the game and challenge yourself to improve your reaction time!** ⚡