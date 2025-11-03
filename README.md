# 🎲 Python Craps Dice Game

This is a simple **Craps-style dice game** built in Python.
It simulates rolling two dice and follows the traditional rules of the **Craps** casino game. The program continues rolling automatically until you either **win** or **lose** based on your dice rolls.

---

## 🧠 How It Works

1. The game rolls **two dice** and adds up their sum.
2. On the **first roll**:

   * If the sum is **7 or 11**, you **win immediately** 🎉
   * If the sum is **2, 3, or 12**, you **lose immediately** 💀
   * If the sum is **4, 5, 6, 8, 9, or 10**, that number becomes your **goal number**.
3. Once you have a **goal number**, the game keeps rolling:

   * If you roll your **goal number** again → **You win!** 🏆
   * If you roll a **7** before hitting your goal number → **You lose!** 😢
   * Otherwise, the game keeps rolling automatically until one of those happens.

---

## 🎮 Example Gameplay

```
The sum of dice is 3 + 4 = 7
You won
```

or

```
The sum of dice is 3 + 5 = 8
Now your goal number is 8
The sum of dice is 4 + 2 = 6
The sum of dice is 1 + 6 = 7
You lost!
```

---

## ⚙️ Features

* 🎲 Realistic dice simulation using `random.randint(1, 6)`
* 🔁 Continuous gameplay until a win or loss condition is met
* 🧩 Implements standard **Craps** rules
* 🗣️ Clear, descriptive text-based output

---


## 📂 File Structure

```
craps-game/
│
├── craps_game.py     # Main game code
└── README.md         # Project documentation
```

---

## 💡 Possible Improvements

* Allow the player to press a key to **roll manually** instead of automatic rolls.
* Add a **scoreboard** or **money system** to simulate betting.
* Include **sound effects** or a **GUI** for a more engaging experience.
* Track **statistics** like total wins/losses.

---

## 🧑‍💻 Author

**Narek**
A fun and simple Python project that demonstrates loops, random number generation, and game logic.

---
