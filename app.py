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

elif page == "📝 Explanation":
    st.title("📝 Explanation")

    if code:
        st.write("Explanation will be generated here.")
    else:
        st.warning("Please upload a Python file.")
