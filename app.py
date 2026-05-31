import streamlit as st
import ast
import random

st.set_page_config(
    page_title="Python Code Explainer",
    page_icon="🐍",
    layout="wide"
)

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select a Page",
 [
    "🏠 Home",
    "💻 Source Code",
    "📊 Code Analysis",
    "📄 Code Summary",
    "🔄 Program Flow",
    "▶️ Run Game"
]
)

uploaded_file = st.sidebar.file_uploader(
    "Upload Python File",
    type=["py"]
)

code = ""

if uploaded_file is not None:
    code = uploaded_file.read().decode("utf-8")
    functions = 0
imports = 0
lines = 0

if code:
    lines = len(code.splitlines())

    try:
        tree = ast.parse(code)

        for node in ast.walk(tree):

            if isinstance(node, ast.FunctionDef):
                functions += 1

            elif isinstance(node, ast.Import):
                imports += len(node.names)

            elif isinstance(node, ast.ImportFrom):
                imports += 1

    except:
        pass
    
    

if page == "🏠 Home":
    st.title("🐍 Python Code Explainer Dashboard")
    st.write(
        "Upload a Python file and explore its code and explanations."
    )

elif page == "💻 Source Code":
    st.title("💻 Source Code")

    if code:
        st.code(code, language="python")
    else:
        st.warning("Please upload a Python file.")

elif page == "📊 Code Analysis":

    st.title("📊 Code Analysis")

    if code:

        col1, col2, col3 = st.columns(3)

        col1.metric("Lines of Code", lines)
        col2.metric("Functions", functions)
        col3.metric("Imports", imports)

    else:
        st.warning("Please upload a Python file.")

elif page == "📄 Code Summary":

    st.title("📄 Code Summary")

    st.markdown("""
    ### Purpose
    This program implements a Hangman-style word guessing game.

    ### Main Features
    - Randomly selects a word from a predefined list.
    - Accepts guesses from the player.
    - Checks whether the guessed letter exists in the word.
    - Updates the displayed progress after each guess.
    - Continues until the word is guessed or attempts are exhausted.

    ### Concepts Used
    - Variables
    - Lists
    - Loops
    - Conditional Statements
    - User Input
    - Random Module
    """)
elif page == "🔄 Program Flow":

    st.title("🔄 Program Flow")

    st.markdown("""
    ### Hangman Game Flow

    Start

    ↓

    Display Welcome Message

    ↓

    Select Random Word

    ↓

    Initialize Game Variables

    ↓

    Ask User for a Letter

    ↓

    Is Letter in Word?

    ↓

    Yes → Update Progress

    ↓

    No → Reduce Attempts

    ↓

    Is Word Complete?

    ↓

    Yes → Player Wins

    ↓

    No → Continue Loop

    ↓

    End Game
    """)
elif page == "▶️ Run Game":

    import random

    st.title("🎮 Hangman Game")
    st.info("Play the Hangman game directly from the dashboard!")

    words = [
        "afghanistan",
        "albania",
        "algeria",
        "andorra",
        "angola",
        "antigua",
        "argentina",
        "armenia",
        "australia",
        "austria"
    ]

    # Initialize game
    if "word" not in st.session_state:
        st.session_state.word = random.choice(words)

    if "guessed" not in st.session_state:
        st.session_state.guessed = []

    if "attempts" not in st.session_state:
        st.session_state.attempts = 6

    # Display current progress
    display_word = ""

    for letter in st.session_state.word:
        if letter in st.session_state.guessed:
            display_word += letter + " "
        else:
            display_word += "_ "

    st.subheader(display_word)

    # Show guessed letters
    st.write(
        "Guessed Letters:",
        ", ".join(st.session_state.guessed)
        if st.session_state.guessed
        else "None"
    )

    # Show attempts left
    st.write(
        f"Attempts Remaining: {st.session_state.attempts}"
    )

    # User input
    guess = st.text_input(
        "Enter a letter",
        max_chars=1
    )

    # Guess button
    if st.button("Guess"):

        guess = guess.lower()

        if guess:

            if guess not in st.session_state.guessed:

                st.session_state.guessed.append(guess)

                if guess not in st.session_state.word:
                    st.session_state.attempts -= 1

            st.rerun()

    # Check win condition
    if all(
        letter in st.session_state.guessed
        for letter in st.session_state.word
    ):
        st.success("🎉 Congratulations! You Won!")

    # Check lose condition
    elif st.session_state.attempts <= 0:
        st.error(
            f"💀 Game Over! The word was '{st.session_state.word}'."
        )

    # New game button
    if st.button("🔄 New Game"):

        st.session_state.word = random.choice(words)
        st.session_state.guessed = []
        st.session_state.attempts = 6

        st.rerun()
