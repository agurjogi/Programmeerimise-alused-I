# CLAUDE.md

## Project Overview

This repository contains homework assignments for the University of Tartu course **"Programmeerimise alused I"** (Programming Fundamentals I). All exercises are standalone Python scripts covering beginner-to-intermediate programming concepts.

The course URL: https://courses.cs.ut.ee/2017/eprogalused/spring/Main/

---

## Repository Structure

```
Programmeerimise-alused-I/
├── 6.1. reklaam.py          # Exercise 6.1 – Banner/advertisement function
├── 6.2. teler.py            # Exercise 6.2 – TV diagonal calculator
├── 6.3. pidu.py             # Exercise 6.3 – Party budget calculator
├── 6.4a. mitmes.py          # Exercise 6.4a – Guest greeting with counter
├── 6.4b. myndid_versioon_2.py  # Exercise 6.4b – Coin sum from file
├── 6.4c.kuupaev.py          # Exercise 6.4c – Date format converter
├── myndid.txt               # Sample data file for exercise 6.4b
└── README.md                # Brief course description (Estonian)
```

---

## Language and Conventions

- **Language**: All code, comments, variable names, and prompts are written in **Estonian**.
- **Python version**: Standard Python 3. No external libraries are used.
- **Encoding**: Files with Estonian special characters (ä, ö, ü, õ, š, ž) use **UTF-8** encoding. File I/O explicitly specifies `encoding="UTF-8"`.
- **Naming**: Variable and function names follow Estonian words (e.g., `eelarve`, `tervitus`, `kuu_nimi`). This is intentional and must be preserved.
- **No formatting tools**: No linters or formatters (e.g., `black`, `flake8`) are configured. Do not add them without explicit instruction.

---

## Exercise Summaries

### 6.1. reklaam.py – Advertisement Banner
- **Function**: `banner(sisu)` – takes a string and returns it in uppercase.
- **Program**: Asks user how many times to display a slogan, then prints it that many times using a `while` loop.

### 6.2. teler.py – TV Diagonal Calculator
- **Function**: `teleri_diagonaal(kaugus)` – takes viewing distance in metres, returns TV diagonal in inches (rounded to nearest integer using `round()`).
- **Formula**: `round(kaugus * 100 * 0.39 / 2.5)`
- **Program**: Reads distance from user input, prints the result.

### 6.3. pidu.py – Party Budget Calculator
- **Function**: `eelarve(guests)` – takes number of guests, returns total budget: `guests * 10 + 55` (10 EUR per person + 55 EUR room rent).
- **Program**: Asks total invitees and confirmed attendees, prints maximum and minimum budgets.

### 6.4a. mitmes.py – Guest Greeting Counter
- **Function**: `tervitus(mitmes)` – prints a three-line greeting sequence with the ordinal number of the greeting (no return value).
- **Program**: Reads guest count, calls `tervitus` in a `while` loop from 1 to guest count.

### 6.4b. myndid_versioon_2.py – Bronze Coin Sum
- **Function**: `pronksikarva_summa(fail)` – takes a filename (integer), reads coin values from the file, and returns the sum of bronze coins (values 1, 2, 5 cents).
- **Data file**: `myndid.txt` – one coin value per line.
- **Note**: The function parameter is named `fail` but internally uses the global `failinimi` variable — a known inconsistency in the original student solution.

### 6.4c.kuupaev.py – Date Format Converter
- **Function**: `kuu_nimi(kuu_number)` – takes a month number (1–12), returns the Estonian month name in lowercase using a list.
- **Function**: `kuupäev_sõnena(kuupaev)` – takes a date string in `DD.MM.YYYY` format, returns it as `"D. month YYYY. a"` (Estonian long format).
- **Program**: Reads a date from the user and prints the formatted version.

---

## Running the Scripts

Each script is standalone and run directly with Python 3:

```bash
python3 "6.1. reklaam.py"
python3 "6.2. teler.py"
python3 "6.3. pidu.py"
python3 "6.4a. mitmes.py"
python3 "6.4b. myndid_versioon_2.py"   # prompts for filename, use: myndid.txt
python3 "6.4c.kuupaev.py"
```

Note: File names contain spaces and Estonian characters — always quote them in the shell.

---

## Development Guidelines for AI Assistants

1. **Preserve Estonian**: Do not translate variable names, function names, comments, or user-facing strings to English. The course grader checks exact function names.

2. **Function names are fixed**: The assignment specifies exact function names (e.g., `banner`, `teleri_diagonaal`, `eelarve`, `tervitus`, `pronksikarva_summa`, `kuu_nimi`, `kuupäev_sõnena`). Do not rename them.

3. **No external dependencies**: Do not add `import` statements for third-party packages. Only Python standard library is acceptable.

4. **Minimal changes**: These are student homework exercises. Only fix or add what is explicitly requested. Do not refactor or restructure existing solutions.

5. **No test files**: There is no testing infrastructure. The course uses an online auto-grader at https://courses.cs.ut.ee/2017/eprogalused/spring/Main/Kontroll-funktsioon

6. **File naming**: Follow the existing pattern of `<section>. <topic>.py` when adding new exercises. Note that some files omit the space before the dot (e.g., `6.4c.kuupaev.py`).

7. **Input/Output format**: Each script reads from `input()` and prints to `stdout`. The exact format of prompts and output may matter for the auto-grader — do not change them without explicit instruction.

---

## Git Workflow

- Main branch: `master`
- Feature/AI branches: `claude/<session-id>` pattern
- Commits follow simple descriptive messages in English or Estonian
