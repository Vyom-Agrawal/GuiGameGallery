# 🎨 Doodle Builder

A fun and creative mini-game where players replicate various patterns and shapes within a time limit! Test your drawing skills and speed while trying to match the patterns.

## 🎮 Game Overview

**Doodle Builder** challenges you to recreate different patterns shown on a reference canvas. Draw quickly and accurately to earn maximum points before time runs out!

## ✨ Features

- **8 Unique Patterns**: Circle, Star, Spiral, Zigzag, Smiley, Triangle, Diamond, and Wave
- **Quick Timer**: 15 seconds to complete each drawing challenge
- **Automatic Timer**: Timer starts when you begin drawing (no need to click start!)
- **Score System**: Earn points based on drawing completion
  - Completing a drawing: 10 points
  - Skip without drawing: No penalty
- **Freehand Drawing**: Smooth mouse-based drawing interface
- **Random Pattern Selection**: Keep the game fresh with randomized challenges
- **Visual Feedback**: Clean, modern UI with clear pattern reference
- **Progress Tracking**: Track your total score and number of attempts

## 🕹️ How to Play

1. **Start the Game**: Launch the application and a random pattern will appear on the left canvas
2. **Study the Pattern**: Look at the sample pattern carefully
3. **Start Drawing**: Click on the drawing canvas and begin replicating the pattern
   - The 7-second timer starts automatically when you begin drawing!
4. **Complete Quickly**: Try to finish your drawing before the timer runs out
5. **Submit**: Click "✅ Submit" when you're done (or when time expires) to earn points
6. **Next Challenge**: Click "➡️ Next Pattern" to try a new pattern
7. **Clear**: Use "🗑️ Clear" button anytime to erase and start over

## 🎯 Controls

- **Clear**: Erase your current drawing and start over (timer resets)
- **Submit**: Submit your drawing and receive points (10 points per completion)
- **Next Pattern**: Load a new random pattern to draw

## 📋 Requirements

- Python 3.x
- tkinter (usually comes pre-installed with Python)

## 🚀 Installation & Running

1. Make sure you have Python installed on your system
2. No additional packages needed (tkinter is included with Python)
3. Run the game:

```bash
python main.py
```

## 🎨 Available Patterns

1. **Circle** - A simple round shape
2. **Star** - A classic 5-pointed star
3. **Spiral** - An elegant spiraling curve
4. **Zigzag** - A sharp angular pattern
5. **Smiley** - A cheerful smiley face
6. **Triangle** - An equilateral triangle
7. **Diamond** - A four-sided diamond shape
8. **Wave** - A flowing wave pattern

## 💡 Tips for High Scores

- **Be Quick**: You only have 7 seconds per pattern!
- **Start immediately**: Timer begins when you first click to draw
- **Use smooth strokes**: Continuous movements work best
- **Practice patterns**: Try each pattern multiple times to improve
- **Don't overthink**: The timer is short, so trust your instincts
- **Complete the drawing**: Earn 10 points for each submitted drawing
- **Have fun**: It's about creativity and speed, not perfection!

## 🎓 Learning Value

This game helps develop:
- Hand-eye coordination
- Pattern recognition
- Time management skills
- Fine motor control
- Visual memory
- Quick decision-making

## 🛠️ Technical Details

- **Built with**: Python Tkinter
- **Canvas Size**: 350x350 pixels for each canvas
- **Drawing Method**: Mouse event-based freehand drawing
- **Timer**: 15-second countdown per attempt (auto-starts on first draw)
- **Color Scheme**: Modern dark theme with contrasting elements

## 🎪 Game Features Breakdown

### Visual Elements
- Dual canvas layout for easy comparison
- Color-coded UI elements for better user experience
- Clear labeling and instructions
- Real-time timer and score display

### Gameplay Mechanics
- Smooth drawing with anti-aliased lines
- Auto-start timer on first mouse click
- Unlimited attempts to improve your score
- Can skip patterns without penalty

## 🔧 Customization

You can easily customize the game by modifying:
- `time_limit`: Change the countdown duration (default: 7 seconds)
- Drawing line width and color in the `draw()` method
- Score value in the `submit_drawing()` method (default: 10 points)
- Add new patterns by creating new pattern methods

## 🐛 Troubleshooting

**Game doesn't start?**
- Ensure Python 3.x is installed
- Verify tkinter is available: `python -m tkinter`

**Drawing feels laggy?**
- This is normal on some systems; try drawing a bit slower
- The smooth drawing uses continuous line segments

## 📝 Future Enhancement Ideas

- Add difficulty levels (easy, medium, hard)
- Implement actual pattern matching algorithm
- Add sound effects and animations
- Create a multiplayer mode
- Save and display high scores
- Add more complex patterns
- Time attack mode with decreasing time limits

**Enjoy drawing and have fun improving your Doodle Builder skills!** 🎨✨