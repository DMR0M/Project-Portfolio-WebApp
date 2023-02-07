import streamlit as st

st.set_page_config(layout="wide")

col_1, col_2 = st.columns(2)

with col_1:
    st.image("images/Mittens.png")

with col_2:
    st.title("Rommel Rudolf A. Dela Merced")
    content = """
        An Aspiring Python Developer
    """
    st.write(content)

    bio = """
        A Graduate of B.S. in Computer Science in Arellano University Andres Bonifacio Campus\n
        Software Engineer at Tsukiden Global Solutions Inc.\n
        Python, Javascript, Rust\n
    """
    st.info(bio)
