# python‑lab‑from‑scratch 🧪🐍

*A grab‑bag of procedural Python scripts written entirely from scratch — no frameworks, just raw code and curiosity.*

---

## ✨ Why this repo?

This repository showcases my hands‑on experimentation with the fundamentals of Python. Each script was implemented “by hand” to deepen understanding of algorithms, recursion, testing and general problem‑solving without leaning on heavy external libraries.

---

## 📂 Contents

| Path / Script                                          | Description                                                                                  |
| ------------------------------------------------------ | -------------------------------------------------------------------------------------------- |
| `NIM-game.py`                                          | Play a terminal‑based game of NIM against the computer.                                      |
| `COH-PIAH-Virus-Simulation_for_Plagiarism-Detector.py` | Naïve similarity checker for text files.                                                     |
| `Annoying-elephants_Song-generator.py`                 | Generates a simple melody using recursion (pure Python, **no external audio lib required**). |
| `Binary-search_Recursive-algorithm_with-pytest.py`     | Recursive binary search implementation with unit tests.                                      |
| `Bubble-sort_with-test.py`                             | Bubble sort implementation with pytest support.                                              |
| `Insertion-sort_with-assert.py`                        | Insertion sort using inline assertions.                                                      |
| `Merge-sort_Recursive-algorithm_with-pytest.py`        | Merge sort with recursive implementation with pytest support.                                         |

> **Note** File names match the actual scripts in the repository; adjust if they differ.

---

## 🛠️ Requirements

* Python ≥ 3.10
* [pytest](https://pytest.org/) (only needed to run the automated tests)

Everything else uses only the Python Standard Library (`re`, `typing`, etc.).

Install dependencies into a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate   # PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt  # file lists: pytest
```

---

## 🚀 Quick start

```bash
# 1 ▪ Clone
$ git clone https://github.com/your‑user/python‑lab‑from‑scratch.git
$ cd python‑lab‑from‑scratch

# 2 ▪ (Optionally) activate the venv created above

# 3 ▪ Run a script
$ python NIM-game.py        # replace with any script name
```

### Running the tests

```bash
# From the project root
python -m pytest            # or simply: pytest
```

> ⚠️ **IDLE users:** the integrated shell cannot run `pytest` directly. Run the command above from your terminal (PowerShell, Bash, CMD) or use an IDE that integrates pytest (e.g. VS Code, PyCharm).

---

## 💡 Project philosophy

1. **Minimal dependencies** — only `pytest` for testing.
2. **Readable code** — descriptive variable names, type hints (`typing`), and docstrings.
3. **Small, focused scripts** — each file does one thing well.
4. **Tests where it matters** — key algorithms are covered by unit tests so you can refactor with confidence.

---

## 🤝 Contributing

Found an issue or have an idea? Feel free to open an issue or pull request. For major changes, please start a discussion first.

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 📣 Contact

Questions? Ping me on GitHub or reach out via LinkedIn. Happy coding!
