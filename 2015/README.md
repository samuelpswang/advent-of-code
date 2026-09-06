# Advent of Code 2015 - 🎄

![](https://img.shields.io/badge/stars%20⭐-50-yellow) ![](https://img.shields.io/badge/days%20completed-25-red)

### Intro

This repository is my solutions in `Python3.11.7` to the 2015 Advent of Code event. The solutions were written in late 2023 and early 2024 after the completion of the 2023 Advent of Code.

### Results

All results were >24h as they were completed after the event.

### File Structure

```txt
root/
├─ .github/workflow/actions.yml     -> YAML file that updates the badges on README.md
├─ .venv/                           -> Python virtual environment supporting files
├─ day_<N>/                         -> <N> = day number
│  ├─ input.txt                     -> User-specific input (removed)
│  └─ part_<M>.py                   -> Solution in Python; <M> = part number
├─ requirements.txt                 -> Package information for pip
├─ README.md                        -> Main docs
└─ .gitignore
```

### Python Virtual Environment Usage

1. To create the virtual environment and install the packages:

    ```bash
    virtualenv .venv --python=3.11
    pip3 install -r requirements.txt
    ```

2. To activate the virtual invironment:

    ```bash
    source .venv/bin/activate
    ```

3. To exit the virtual environment:

    ```bash
    deactivate
    ```

### Experience

This is the second Advent of Code event that I had attempted. Compared to the puzzles from 2023, most of them seemed to be about [Number Theory](https://en.wikipedia.org/wiki/Number_theory) rather than about graphs. During my puzzle cracking process, I frequently looked to [@mjpieters](https://github.com/mjpieters)'s repository for inspiration and used it as a reference for my programs, I would like to thank him for the guidance he provided unknowingly.

### Notable Topics

1. Day 05: [`hashlib` Module](https://docs.python.org/3/library/hashlib.html)
2. Day 08: [`ast` Module](https://docs.python.org/3/library/ast.html).
3. Day 09: [`itertools` Module](https://docs.python.org/3/library/itertools.html), [Traveling Salesman Problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem).
4. Day 10: [Look-and-Say Sequence](https://en.wikipedia.org/wiki/Look-and-say_sequence), [`functools` Module and `reduce()`](https://realpython.com/python-reduce-function/).
5. Day 15: [`gekko` Module](https://gekko.readthedocs.io/en/latest/), [Non-Linear Programming](https://en.wikipedia.org/wiki/Nonlinear_programming).
6. Day 20: [`sympy` Module](https://www.sympy.org/en/index.html).
