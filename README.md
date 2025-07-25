# 🧨 Minesweeper - Python Tkinter Edition

This is a fully functional **Minesweeper game** built in Python using the **Tkinter GUI library**. Players can choose their own custom grid size (up to 25×25), place flags, and reveal tiles, just like the classic version! 

---

## 🎮 Features

- **Customizable Grid Size** - Choose rows and columns for personalized difficulty
- **Randomly Generated Mines** - Every game has random bombs
- **Flag System** - Right-click to place and remove flags (`?`)
- **Smart Reveal** - Automatically reveals adjacent cells when a blank tile is clicked
- **Game Timer** - Track your completion time for competitive play
- **Endgame Dialogs** - Pop-up notifications with retry options
- **Color-Coded Tiles** - Visual indicators based on nearby mine count

---

## 🛠 Technologies Used

- **Python 3** - Core programming language
- **Tkinter** - Built-in GUI library for cross-platform compatibility
- **Random Module** - Mine placement generation
- **Time Module** - Game timer functionality

---

## 📸 Screenshots & Demo

[![Run on Replit](https://replit.com/badge/github/Xtreak-XD/Minesweeper)](https://replit.com/@mikeandresavila/Minesweeper)

<img width="380" height="140" alt="Minesweeper Game Setup" src="https://github.com/user-attachments/assets/b562c4be-2c70-48e3-b601-ff064f1d5266" />
<p></p>
<img width="280" height="425" alt="Minesweeper Gameplay" src="https://github.com/user-attachments/assets/8ff44b49-4867-428e-b36b-3f3f355a1a8e" />

---

## 🎯 Game Rules

1. **Goal** - Clear all tiles without hitting a mine
2. **Numbers** - Indicate how many mines are adjacent to that tile
3. **Flags** - Right-click to mark suspected mine locations
4. **First Click** - Always safe - mines are placed after your first move
5. **Win Condition** - Reveal all non-mine tiles
6. **Lose Condition** - Click on a mine tile

---

## 🚀 Future Enhancements

**Potential Improvements:**
- **Difficulty Presets** - Beginner, Intermediate, and Expert modes
- **High Score System** - Local leaderboard for best completion times
- **Sound Effects** - Audio feedback for clicks, wins, and explosions
- **Themes** - Multiple visual themes and color schemes
- **Statistics** - Win/loss ratios and average completion times

---

## ▶️ How to Run

> ⚠️ **Note:** Due to limitations with browser-based GUIs, please clone this project and run it locally to play the Minesweeper game.

### Prerequisites
Make sure you have Python 3 installed on your system.

### Installation & Launch
```bash
git clone https://github.com/Xtreak-XD/Minesweeper
cd Minesweeper
python3 main.py
```

**That's it!** No additional dependencies required - Tkinter comes built-in with Python.

---

## 🤝 Contributing

Feel free to contribute to this project! Ideas for contributions:
- Bug fixes and performance improvements
- New features and game modes
- UI/UX enhancements
- Code optimization and refactoring

---

## 📝 License

This project is open source and available for educational and personal use.

---

*💣 Classic Minesweeper reimagined in Python - Happy mine hunting!*
