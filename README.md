# 🧮 CLI Calculator (Expression-Based)

A simple yet powerful **Command Line Interface (CLI) Calculator** built using Python.
This calculator supports full arithmetic expressions, operator precedence, and maintains a history of calculations.

---

## 🚀 Features

* ✅ Supports full expressions (e.g. `2 + 3 * 4 - 5 / 2`)
* ✅ Handles operator precedence automatically
* ✅ Supports operators:

  * Addition `+`
  * Subtraction `-`
  * Multiplication `*`
  * Division `/`
  * Power `**`
  * Modulus `%`
* ✅ Input validation (rejects invalid characters)
* ✅ Handles division by zero safely
* ✅ Calculation history tracking
* ✅ Interactive CLI-based menu

---

## 🖥️ How It Works

1. Run the program
2. Enter a mathematical expression
3. Get the result instantly
4. Use commands:

   * `history` → View past calculations
   * `exit` → Quit the program

---

## 📌 Example

```
Enter Expression: 2 + 3 * 4
Result: 14
------------------------------
Enter Expression: history
2 + 3 * 4 = 14
```

---

## 🛠️ Tech Used

* Python
* CLI (Command Line Interface)
* Built-in functions (`eval`, `try-except`)

---

## ⚠️ Note

This project uses Python's `eval()` for expression evaluation.
It is safe for learning purposes but **should not be used with untrusted input in production applications**.

---

## 📈 Future Improvements

* Add persistent history (save to file)
* Build GUI version (Tkinter / Web app)
* Replace `eval()` with custom expression parser
* Add scientific functions (sqrt, log, etc.)

---

## 👨‍💻 Author

Abhijeet

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to improve it!
