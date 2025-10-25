
# ⚡ Reaction Time Test

A small GUI game that measures how quickly you can respond to a visual cue. Click (or press Space / Enter) when the area turns green and the game records your reaction time.

## 🎮 Game Description

Reaction Time Test displays a large colored area that changes after a short random delay. When it turns green, click as fast as you can. The app records each trial, shows a short history, and calculates simple stats (last, best, average).

## 🕹️ How to Play

1. Click the large colored area or press Space / Enter to start a trial.
2. Wait for the area to change color to green.
3. As soon as it turns green, click the area (or press Space/Enter) as fast as possible.
4. Clicking before it turns green records a "Too soon!" (early click) ❌.
5. Use "Clear History" to reset your recorded trials.

## ✨ Features

- 🎯 Large, focusable canvas area for the reaction test
- ⏱️ Records reaction times in milliseconds
- 📋 Keeps a short history (newest at top)
- 🏆 Shows Last, Best, and Average reaction times
- 🧾 Clear history and in-app instructions
- ⌨️ Keyboard controls (Space / Enter)

## 📋 Requirements

- Python 3.6 or higher
- tkinter (usually comes pre-installed with Python)

## 🚀 Installation & Running

1. Make sure Python is installed on your system.
2. Open terminal/command prompt in that folder.

```powershell
python main.py
```

On other platforms use `python3 main.py` if required.

## 🔧 Customization

Edit `main.py` to change behavior (top-of-file constants):

- `WINDOW_W` / `WINDOW_H` — window size (pixels)
- `MIN_DELAY` / `MAX_DELAY` — min/max random wait time (seconds) before the area turns green

Other UI tweaks (fonts, colors, text) can be changed inside the `ReactionTestApp` class where the canvas and labels are created.

## 📝 License

This game is part of the GuiGameGallery repository. See the project `LICENSE.md` in the repository root for licensing information.
