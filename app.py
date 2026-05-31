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

    st.title("🌍 Guess The Country")

    countries = [
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

    level1_hints = {
        "afghanistan":"a.g..ni...n",
        "albania":"a.b..i.",
        "algeria":"a.g.ri.",
        "andorra":"a..o.ra",
        "angola":"a.g..a",
        "antigua":"an.i..a",
        "argentina":"ar...t..a",
        "armenia":"a..e..a",
        "australia":"a..tr..i.",
        "austria":"a..t..a"
    }

    level2_hints = {
        "afghanistan":"The flag of this country has changed 20 times in 102 years.",
        "albania":"This country has 4 UNESCO World Heritage Sites.",
        "algeria":"The capital city is known as 'The White'.",
        "andorra":"This country has no military.",
        "angola":"This country is twice the size of France.",
        "antigua":"Its mountains are named after presidents.",
        "argentina":"The first animated creature film was made here.",
        "armenia":"First country to adopt Christianity.",
        "australia":"The flattest continent-country.",
        "austria":"The first postcard came from this country."
    }

    # Start new game
    if "country" not in st.session_state:

        st.session_state.country = random.choice(countries)
        st.session_state.progress = ""
        st.session_state.position = 0
        st.session_state.level = None
        st.session_state.attempts = len(st.session_state.country)

    # Level selection
    if st.session_state.level is None:

        level = st.selectbox(
            "Select Level",
            [1, 2]
        )

        if st.button("Start Game"):

            st.session_state.level = level
            st.rerun()

    else:

        country = st.session_state.country

        st.subheader(
            f"Attempts Remaining: {st.session_state.attempts}"
        )

        st.write(
            f"Country starts with: **{country[0].upper()}**"
        )

        if st.session_state.level == 1:

            st.success("Level 1 Hint")
            st.code(level1_hints[country])

        else:

            st.success("Level 2 Hint")
            st.info(level2_hints[country])

        st.write(
            f"Progress: **{st.session_state.progress}**"
        )

        guess = st.text_input(
            "Guess the next character",
            max_chars=1
        )

        if st.button("Submit Guess"):

            if guess:

                guess = guess.lower()

                expected = country[
                    st.session_state.position
                ]

                if guess == expected:

                    st.session_state.progress += guess
                    st.session_state.position += 1

                    if (
                        st.session_state.progress
                        == country
                    ):
                        st.success(
                            f"🎉 You Won! The country was {country.title()}"
                        )

                else:

                    st.error("Wrong Guess")

                    st.session_state.attempts -= 1

                    if st.session_state.attempts <= 0:

                        st.error(
                            f"Game Over! The country was {country.title()}"
                        )

                st.rerun()

        if st.button("🔄 New Game"):

            st.session_state.country = random.choice(countries)
            st.session_state.progress = ""
            st.session_state.position = 0
            st.session_state.level = None
            st.session_state.attempts = len(st.session_state.country)

            st.rerun()
