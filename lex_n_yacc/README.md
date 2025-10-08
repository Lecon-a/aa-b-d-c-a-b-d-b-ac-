# Lex String Pattern Matcher

## Overview
This project is a simple **Lex (Flex) implementation** that checks if an input string matches a specific regular expression pattern. The program prints **"Accepted."** if the input matches the pattern, or **"Rejected."** otherwise.

The pattern used in this project is:

```
^aa(b|d)c*(a|b|d)*b+(ac)$
```

It demonstrates how to define token patterns in Lex and perform actions based on matches.

---

## Features
- Matches strings against a complex regular expression
- Prints "Accepted." if the input matches the pattern
- Prints "Rejected." if the input does not match
- Ignores newlines for continuous input processing
- Simple interactive command-line interface

---

## Requirements
- **Lex/Flex** installed on your system
- **C compiler** (e.g., `gcc` or `clang`)
- Unix/Linux/macOS environment recommended

---

## Lex Code

```c
%{
#include <stdio.h>
%}

%option noyywrap

%%
^aa(b|d)c*(a|b|d)*b+(ac)$    { printf("Accepted.\n"); }
\n                          { /* ignore newline */ }
.                           { printf("Rejected.\n"); }
%%

int main(void) {
    printf("Enter a string to test (Ctrl + D to stop):\n");
    yylex();
    return 0;
}
```

---

## Usage

### 1. Compile
```bash
flex expr.l          # Generates lex.yy.c
gcc lex.yy.c -o expr -ll    # Compile with Lex library
```

> Note: On some systems, you may need `-lfl` instead of `-ll`.

### 2. Run
```bash
./expr
```

### 3. Example
**Input:**
```
aabbbac
```

**Output:**
```
Accepted.
```

**Input:**
```
abcd
```

**Output:**
```
Rejected.
```

You can enter multiple strings; the lexer will check each one until you press **Ctrl + D** to stop.

---

## How It Works
The regular expression:

```
^aa(b|d)c*(a|b|d)*b+(ac)$
```

- `^` → Start of the string  
- `aa` → The string must start with "aa"  
- `(b|d)` → Followed by either 'b' or 'd'  
- `c*` → Zero or more 'c's  
- `(a|b|d)*` → Zero or more of 'a', 'b', or 'd'  
- `b+` → One or more 'b's  
- `(ac)` → Ends with 'ac'  
- `$` → End of the string  

If the input matches this pattern exactly, the lexer prints **Accepted**; otherwise, it prints **Rejected**.

---

## Extending
- Modify the regular expression in the Lex rules to match other string patterns
- Add additional actions or output formatting
- Integrate with larger text-processing or compiler projects

---

## References
- [Flex Manual](https://westes.github.io/flex/manual/)
- Compilers: Principles, Techniques, and Tools (Dragon Book)

---

## License
MIT License
