import streamlit as st

st.header("Welcome to Jorgo's performance review app.")
st.header('')

col1, col2 = st.columns(2)

with col1:
    st.subheader('Employee profile')
    st.write('**Name:** _Jorgo Haezaerts_  \n**level:** _Junior Advisor 2_  \n**Competence:** _Technology/Lighthouse_  \n**Mentor:** _Bart Van Rompaye_  \n**Coach:** _Mathew Mertens_')
    st.header('')
    st.write("Check out the sidebar to have a look at my goals, dreams and experiences for each year that I've been with KPMG Lighthouse.")

with col2:
    st.image('./images/jorgo_haezaerts_border.jpg')


