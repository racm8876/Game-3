import streamlit as st

st.set_page_config(page_title="Tic Tac Toe 🎮", page_icon="🎯", layout="centered")

# Title
st.title("🎮 Tic Tac Toe Game")
st.markdown("Play a simple game of **X vs O** built using Streamlit!")

# Initialize session state
if "board" not in st.session_state:
    st.session_state.board = [""] * 9
    st.session_state.turn = "X"
    st.session_state.winner = None

# Check winner function
def check_winner(board):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for combo in winning_combinations:
        a, b, c = combo
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]
    if "" not in board:
        return "Draw"
    return None

# Reset function
def reset_game():
    st.session_state.board = [""] * 9
    st.session_state.turn = "X"
    st.session_state.winner = None

# Game logic
cols = st.columns(3)
for i in range(9):
    with cols[i % 3]:
        if st.button(st.session_state.board[i] or " ", key=i, use_container_width=True):
            if st.session_state.board[i] == "" and st.session_state.winner is None:
                st.session_state.board[i] = st.session_state.turn
                st.session_state.winner = check_winner(st.session_state.board)
                st.session_state.turn = "O" if st.session_state.turn == "X" else "X"
            st.experimental_rerun()

# Show game status
if st.session_state.winner:
    if st.session_state.winner == "Draw":
        st.success("It's a draw! 🤝")
    else:
        st.balloons()
        st.success(f"🎉 Winner: {st.session_state.winner}")
else:
    st.info(f"Turn: {st.session_state.turn}")

# Reset button
st.button("🔄 Restart Game", on_click=reset_game)
