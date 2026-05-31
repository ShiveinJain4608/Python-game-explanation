import streamlit as st

st.set_page_config(
    page_title="Python Code Explainer",
    page_icon="🐍",
    layout="wide"
)

st.title("🐍 Python Code Explainer Dashboard")

st.markdown(
    "Upload or display Python code and explain its working step-by-step."
)

code = """
print("Welcome")
name = input("Enter your name: ")
print("Hello", name)
"""

col1, col2 = st.columns(2)

with col1:
    st.subheader("💻 Python Code")
    st.code(code, language="python")

with col2:
    st.subheader("📝 Explanation")
    st.write("""
    - Line 1 prints 'Welcome'.
    - Line 2 asks the user for input.
    - Line 3 stores the input in a variable called `name`.
    - Line 4 displays a greeting message.
    """)
