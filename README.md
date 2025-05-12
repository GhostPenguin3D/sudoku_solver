# 🧩 Sudoku Solver — Python Project

A fully functional Sudoku solver built in Python with both a **Command Line Interface (CLI)** and an interactive **Web Interface** using Streamlit. Ideal for showcasing algorithmic thinking and Python development skills.

---

## 🔧 Features

- ✅ Solves Sudoku puzzles using the Backtracking algorithm
- 🖥️ CLI version for terminal use
- 🌐 Web version with a modern interface (Streamlit)
- 📦 Ready for use in portfolios, GitHub projects, or computer science applications

---

## 📁 Project Structure

```
sudoku_solver_full_project/
├── cli/
│ ├── main.py # Run solver in terminal
│ └── sudoku_solver.py # Core solving logic
├── web/
│ ├── app.py # Streamlit web app
│ ├── sudoku_solver.py # Shared solving logic
│ └── requirements.txt # Web dependencies
├── README.md
└── banner.png (optional)
```

---

## 🚀 How to Run

### CLI Version

```bash
cd cli
python main.py
```

### 🌐 Web Version

```bash
cd web
pip install -r requirements.txt
streamlit run app.py
```
- Then open http://localhost:8501 in your browser.
---

### 🧠 Algorithm
- This project uses a Backtracking technique — a brute-force recursive search — to fill in the empty cells of a 9x9 Sudoku board while respecting all Sudoku rules.

### 👨‍💻 Author
- Developed by [GhostPenguin3D] — for use in programming portfolios, learning projects, or CS-related applications.
Feel free to fork, improve, and share!

