import streamlit as st
import ast

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
    "📝 Explanation"
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

elif page == "📝 Explanation":
    st.title("📝 Explanation")

    if code:
        st.write("Explanation will be generated here.")
    else:
        st.warning("Please upload a Python file.")
