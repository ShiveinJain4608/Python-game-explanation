import streamlit as st
import ast
import random
import graphviz

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

    st.subheader("Program Type")
    st.info("Interactive Country Guessing Game")

    st.subheader("Modules Used")
    st.write("""
    • random
      - Used to randomly select a country from the list.
    """)

    st.subheader("Data Structures")
    st.write("""
    • List
      - Stores the names of countries.
    """)

    st.subheader("Input Processing")
    st.write("""
    • Takes user confirmation to start the game.
    • Accepts level selection (1 or 2).
    • Accepts character guesses from the player.
    """)

    st.subheader("Decision Making")
    st.write("""
    • Uses if-elif-else statements to:
      - Check whether the user wants to play.
      - Determine the selected difficulty level.
      - Validate guessed characters.
      - Decide whether the player wins or loses.
    """)

    st.subheader("Looping")
    st.write("""
    • A while loop is used to continue the game
      until the player either:
        - Completes the country name, or
        - Runs out of attempts.
    """)

    st.subheader("Difficulty Levels")
    st.write("""
    Level 1:
    - Displays a partially completed country name.

    Level 2:
    - Displays a fact-based hint about the country.
    """)

    st.subheader("Output")
    st.write("""
    • Displays hints.
    • Shows game progress.
    • Displays win/lose messages.
    • Reveals the correct answer when necessary.
    """)

    st.subheader("Programming Concepts Demonstrated")
    st.success("""
    ✔ Variables

    ✔ Lists

    ✔ User Input

    ✔ Loops

    ✔ Conditional Statements

    ✔ String Manipulation

    ✔ Random Number Generation

    ✔ Game Logic
    """)

elif page == "📄 Code Summary":

    st.title("📄 Code Summary")

    st.markdown("""
## 🎯 Purpose

This program is a country-guessing game developed in Python.

The player must identify a randomly selected country by guessing its letters in sequence.

---

## 🎮 Gameplay

1. The user chooses whether to play the game.
2. A country is randomly selected from a predefined list.
3. The player selects a difficulty level.
4. A hint is displayed based on the chosen level.
5. The player guesses characters one at a time.
6. Correct guesses build the country name.
7. Incorrect guesses reduce the available attempts.
8. The game continues until the player wins or runs out of attempts.

---

## 🏆 Difficulty Levels

### Level 1
- Displays a partially completed country name.
- Easier because some letters are already revealed.

### Level 2
- Displays a fact-based hint about the country.
- More challenging because the full word is hidden.

---

## 💡 Features

- Random country selection
- Two difficulty levels
- Hint system
- Attempt counter
- Win/Lose detection
- Interactive gameplay

---

## 🛠 Python Concepts Used

- Variables
- Lists
- User Input
- Conditional Statements
- Loops
- String Manipulation
- Random Module

---

## 🎯 Learning Outcome

This project demonstrates how Python can be used to build an interactive game using decision-making, looping, lists, strings, and randomization.
""")
elif page == "🔄 Program Flow":

    st.title("🔄 Program Flow")

    flowchart = graphviz.Digraph()

    flowchart.node("A", "Start")
    flowchart.node("B", "Play Game?")
    flowchart.node("C", "Select Random Country")
    flowchart.node("D", "Choose Level")
    flowchart.node("E", "Display Hint")
    flowchart.node("F", "Take Character Guess")
    flowchart.node("G", "Correct Character?")
    flowchart.node("H", "Update Progress")
    flowchart.node("I", "Word Complete?")
    flowchart.node("J", "Reduce Attempts")
    flowchart.node("K", "Attempts Left?")
    flowchart.node("L", "Player Wins")
    flowchart.node("M", "Game Over")

    flowchart.edge("A", "B")
    flowchart.edge("B", "C", "Yes")
    flowchart.edge("C", "D")
    flowchart.edge("D", "E")
    flowchart.edge("E", "F")
    flowchart.edge("F", "G")
    flowchart.edge("G", "H", "Yes")
    flowchart.edge("H", "I")
    flowchart.edge("I", "L", "Yes")
    flowchart.edge("I", "F", "No")
    flowchart.edge("G", "J", "No")
    flowchart.edge("J", "K")
    flowchart.edge("K", "F", "Yes")
    flowchart.edge("K", "M", "No")

    st.graphviz_chart(flowchart)

    st.subheader("Flow Description")

    st.write("""
    1. The player chooses whether to play the game.
    2. A random country is selected.
    3. The player chooses a difficulty level.
    4. A hint is displayed.
    5. The player guesses characters one at a time.
    6. Correct guesses build the country name.
    7. Wrong guesses reduce the remaining attempts.
    8. The game continues until the country is completed or attempts run out.
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
