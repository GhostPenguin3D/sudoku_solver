import streamlit as st
from sudoku_solver import solve, print_board

def board_input_form():
    board = []
    st.write("### กรอกกระดาน Sudoku (0 = ช่องว่าง)")
    for i in range(9):
        cols = st.columns(9)
        row = []
        for j in range(9):
            num = cols[j].number_input(f"{i},{j}", min_value=0, max_value=9, value=0, label_visibility="collapsed")
            row.append(int(num))
        board.append(row)
    return board

def render_board(board, title):
    st.write(f"### {title}")
    for i in range(9):
        row = ""
        for j in range(9):
            val = board[i][j]
            row += f"{val if val != 0 else '.'} "
            if j % 3 == 2 and j != 8:
                row += "| "
        st.write(row)
        if i % 3 == 2 and i != 8:
            st.write("-" * 21)

def main():
    st.title("🧩 Sudoku Solver by Python")
    st.write("ใส่ตัวเลข Sudoku แล้วกดปุ่มเพื่อให้ AI แก้ให้อัตโนมัติ!")

    board = board_input_form()

    if st.button("🔍 แก้ Sudoku"):
        if solve(board):
            render_board(board, "ผลลัพธ์ที่แก้แล้ว")
        else:
            st.error("แก้ไม่ได้! กระดานอาจจะไม่ถูกต้อง")

if __name__ == "__main__":
    main()