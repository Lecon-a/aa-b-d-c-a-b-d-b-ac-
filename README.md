# Regular Expression Matcher (Python)

## 👨‍💻 Author Information

**Author:** Sunday P. Afolabi
**Lecturer:** Dr. Azeez N.
**Course Title:** Compiler Construction
**Course Code:** CSC802
**University:** University of Lagos
**Semester:** Second

---

## 🎯 Project Overview

This project demonstrates the **conversion and evaluation of a Regular Expression (RE) into its corresponding NFA/DFA representation**, and simulates input acceptance using Python. It serves as part of a practical exercise in **Compiler Construction** to illustrate how lexical analyzers interpret patterns defined by REs.

The implemented Regular Expression (RE) is:

```
aa(b|d)c*(a|b|d)*b+(ac)
```

This expression defines a language over the alphabet **Σ = {a, b, c, d}**, accepted only if the string begins and ends following the given structure.

---

## ⚙️ How It Works

The implementation consists of two main Python scripts:

1. **`re_nfa_dfa.py`** – The driver file that accepts an input string and checks whether it follows the RE-defined path in the DFA.
2. **`dfa_trans_table.py`** – Contains helper functions and the DFA transition table, implementing:

   * `isVariableIn_abcd()` → Validates if input characters belong to Σ.
   * `decide()` → Simulates DFA transitions and determines acceptance.

The DFA simulation traces the input character transitions across states and prints whether the input is accepted or rejected, along with the transition path.

---

## 🧠 Regular Expression Breakdown

| Component | Description                 |                        |                                          |
| --------- | --------------------------- | ---------------------- | ---------------------------------------- |
| `aa`      | String must start with 'aa' |                        |                                          |
| `(b       | d)`                         | Followed by 'b' or 'd' |                                          |
| `c*`      | Zero or more 'c's           |                        |                                          |
| `(a       | b                           | d)*`                   | Zero or more 'a', 'b', or 'd' characters |
| `b+`      | One or more 'b's            |                        |                                          |
| `(ac)`    | Ends with 'ac'              |                        |                                          |

---

## 🧩 Example Implementation (`re_nfa_dfa.py`)

```python
from dfa_trans_table import isVariableIn_abcd, decide

input_string = input("Enter: ")

if isVariableIn_abcd(input_string):
    print(f"The variable '{isVariableIn_abcd(input_string)}' is not recognized")
    exit()

status, path = decide(input_string=input_string)

if status:
    print(f"{input_string} follows the path {{ {' -> '.join(path)} }} is accepted!")
else:
    print(f"{input_string} is rejected!")
```

---

## 🧪 Example Runs

```
Enter: aabbac
aabbac follows the path { q0 -> q1 -> q2 -> q3 -> q4 -> qf } is accepted!

Enter: aabac
aabac is rejected!
```

### ✅ Valid Strings

* `aabbac`
* `aadbbac`
* `aadcbbac`

### ❌ Invalid Strings

* `aabac` → Missing `b+` before final `ac`
* `aacac` → Missing `(b|d)` after initial `aa`

---

## 🧰 Requirements

* Python 3.7 or higher
* VS Code or any Python IDE

To verify installation:

```bash
python --version
```

Run the program:

```bash
python re_nfa_dfa.py
```

---

## 🧾 Environment Details

| Tool    | Version           |
| ------- | ----------------- |
| Python  | 3.13.5            |
| VS Code | 1.94+             |
| OS      | macOS 14.5 Sonoma |

---

## 📂 Project Structure

```
compiler_ass/
├── re_nfa_dfa.py          # Main driver script
├── dfa_trans_table.py     # DFA logic and helper functions
├── README.md              # Project documentation
└── .gitignore             # Ignore cache files
```

---

## 🧩 Notes

This Python-only implementation illustrates the **RE → NFA → DFA** construction and simulation process. The last phase (Minimal DFA reduction) is excluded as per project instruction.

Future enhancement: Integration with **Lex/Yacc** for automated token recognition and syntax-driven analysis.

---

## 📜 License

This project is open-source and available under the **MIT License**.
