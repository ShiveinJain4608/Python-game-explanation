import streamlit as st

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
        "📝 Explanation",
        "📊 Flowchart",
        "▶️ Run Program"
    ]
)

code = """
print("Welcome")
name = input("Enter your name: ")
print("Hello", name)
"""

if page == "🏠 Home":
    st.title("🐍 Python Code Explainer Dashboard")
    st.write(
        "This dashboard helps explain Python programs visually."
    )

elif page == "💻 Source Code":
    st.title("💻 Source Code")
    st.code(code, language="python")

elif page == "📝 Explanation":
    st.title("📝 Explanation")
    st.write("""
    1. The program prints Welcome.
    2. It asks the user to enter their name.
    3. The name is stored in a variable.
    4. A greeting is displayed.
    """)

elif page == "📊 Flowchart":
    st.title("📊 Program Flow")
    st.markdown("""
    Start

    ↓

    Print Welcome

    ↓

    Take User Input

    ↓

    Store Name

    ↓

    Print Greeting

    ↓

    End
    """)

elif page == "▶️ Run Program":
    st.title("▶️ Run Program")

    name = st.text_input("Enter your name")

    if st.button("Run"):
        st.success(f"Hello {name}")
