import streamlit as st

st.set_page_config(
    page_title="Python Code Explainer",
    page_icon="🐍",
    layout="wide"
)

st.title("🐍 Python Code Explainer Dashboard")

st.write(
    "This dashboard helps explain Python code using AI-generated explanations."
)

st.header("Python Code")

sample_code = """
print("Welcome")
name = input("Enter your name: ")
print("Hello", name)
"""

st.code(sample_code, language="python")

st.header("Explanation")

st.write("""
1. The program displays 'Welcome'.
2. It asks the user to enter their name.
3. The entered name is stored in the variable 'name'.
4. The final line prints a greeting.
""")
