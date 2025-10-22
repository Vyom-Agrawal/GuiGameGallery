# 🚀 Getting Started with GuiGameGallery

Welcome to GuiGameGallery! This guide will help you get up and running with the project, whether you want to play the games, contribute a new game, or learn from the existing code.

---

## 📋 Prerequisites

Before you begin, make sure you have the following installed:

- **Python 3.7 or higher** - [Download Python](https://www.python.org/downloads/)
- **Git** - [Download Git](https://git-scm.com/downloads)
- **Basic knowledge of Python and Tkinter** (helpful but not required)

---

## 🎮 Running the Games

### Option 1: Clone the Repository

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Vyom-Agrawal/GuiGameGallery.git
   cd GuiGameGallery
   ```

2. **Navigate to a game folder:**
   ```bash
   cd games/your-game-name
   ```

3. **Run the game:**
   ```bash
   python main.py
   ```

### Option 2: Download a Specific Game

You can also download just the game folder you're interested in and run it independently!

---

## 🛠️ Setting Up for Development

If you want to contribute or modify games, follow these steps:

### 1. Fork and Clone

1. **Fork this repository** by clicking the "Fork" button at the top right of the GitHub page
2. **Clone your fork:**
   ```bash
   git clone https://github.com/YOUR-USERNAME/GuiGameGallery.git
   cd GuiGameGallery
   ```

### 2. Set Up Your Environment

1. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install dependencies** (if any):
   ```bash
   pip install -r requirements.txt
   ```
   *Note: Most games use only Tkinter which comes with Python, so additional dependencies may be minimal.*

### 3. Create a New Branch

Before making changes, create a new branch:
```bash
git checkout -b my-new-game
```

---

## 🎨 Creating Your First Game

### Step 1: Set Up Your Game Folder

1. Navigate to the `games/` directory
2. Create a new folder for your game:
   ```bash
   mkdir games/my-awesome-game
   cd games/my-awesome-game
   ```

### Step 2: Create Essential Files

Your game folder should contain:

```
/my-awesome-game/
├── main.py          # Game entry point
├── README.md        # Game description and instructions
└── assets/          # (Optional) Images, sounds, etc.
```

### Step 3: Write Your Game Code

Create `main.py` with basic Tkinter structure:

```python
import tkinter as tk

class MyAwesomeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("My Awesome Game")
        self.root.geometry("800x600")
        
        # Your game code here
        self.setup_ui()
        
    def setup_ui(self):
        # Add your UI elements
        label = tk.Label(self.root, text="Welcome to My Game!", font=("Arial", 24))
        label.pack(pady=20)
        
if __name__ == "__main__":
    root = tk.Tk()
    game = MyAwesomeGame(root)
    root.mainloop()
```

### Step 4: Document Your Game

Create a `README.md` in your game folder:

```markdown
# My Awesome Game

## Description
A brief description of what makes your game unique.

## How to Play
- Explain the controls
- Explain the objective
- Explain any special features

## Controls
- Key1: Action1
- Key2: Action2

## Features
- Feature 1
- Feature 2

## Credits
Created by [Your Name]
```

---

## 🚩 Submitting Your Game

Once your game is ready:

1. **Test your game** thoroughly
2. **Add and commit your changes:**
   ```bash
   git add .
   git commit -m "Add My Awesome Game"
   ```

3. **Push to your fork:**
   ```bash
   git push origin my-new-game
   ```

4. **Create a Pull Request:**
   - Go to your fork on GitHub
   - Click "Pull Request"
   - Fill out the template describing your game
   - Submit!

---

## 📚 Best Practices

### Code Quality
- Write clean, readable code
- Add comments for complex logic
- Use meaningful variable names

### Game Design
- Make controls intuitive and document them clearly
- Include a pause/restart feature if applicable
- Handle errors gracefully
- Test on different screen sizes if possible

### Documentation
- Write a clear README for your game
- Include screenshots or GIFs if possible
- Credit any resources or inspirations used

---

## 🆘 Getting Help

### Common Issues

**Issue: Python not found**
- Make sure Python is installed and added to your PATH
- Try `python3` instead of `python`

**Issue: Tkinter not available**
- On Linux: `sudo apt-get install python3-tk`
- On macOS: Tkinter comes with Python from python.org
- On Windows: Tkinter is included by default

**Issue: Game won't run**
- Check you're in the correct directory
- Verify all dependencies are installed
- Check the game's README for specific requirements

### Resources

- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [Python Documentation](https://docs.python.org/3/)
- Check the main [README.md](../README.md) for more information
- Check [CONTRIBUTING.md](../CONTRIBUTING.md) for contribution guidelines

### Need More Help?

- Open an issue on GitHub
- Check existing issues for similar problems
- Connect on [LinkedIn](https://www.linkedin.com/in/vyom-agrawal) for questions

---

## 🎯 Next Steps

Now that you're all set up:

1. ✅ Explore the existing games in `/games/`
2. ✅ Try modifying a simple game to learn
3. ✅ Create your own unique game
4. ✅ Share it with the community!

---

**Happy coding and game creating! 🎮🚀**
