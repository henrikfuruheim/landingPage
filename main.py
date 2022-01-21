import streamlit as st


st.set_page_config(layout="wide")
st.image('./header_english.png')

col1, col2 = st.columns([3, 2])

with col1:
    st.markdown('# <span style="color:#410464">Our use of AI </span>', unsafe_allow_html=True)
