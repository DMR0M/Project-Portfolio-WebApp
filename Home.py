import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")

col_1, col_2 = st.columns(2)

with col_1:
    st.image("profile_img/Mittens.png")

with col_2:
    st.title("Rommel Rudolf A. Dela Merced")
    content = """
        Python Developer
    """
    st.write(content)

    bio = """
        A Graduate of B.S. in Computer Science in Arellano University Andres Bonifacio Campus\n
        Software Engineer at Tsukiden Global Solutions Inc.\n
        Python, Javascript, Rust\n
    """
    st.info(bio)

st.subheader('Python Projects: ')

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

# Create dataframe from csv file
projects_df = pd.read_csv('projects/projects.csv', sep=',')


# Add to column 1, 1-10 project title column
with col3:
    for i, row in projects_df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f'[Source Code]({row["url"]})')


# Add to column 2, 11-20 project title column
with col4:
    for i, row in projects_df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.write(f'[Source Code]({row["url"]})')
