import streamlit as st
st.title("Hello App")
st.subheader("Brewed with streamlit")
st.text("welcome to first interactive app")
st.write("choose favarite tv show")
show = st.selectbox("Select our favarite show :",["Breaking bad","Game of thrones","Peaky Blinders","Stranger things","Dark","True decetive"])
st.write(f"Your favaurtie show i.e..,{show}.Excellent choice!")
st.success("Your choice is awesome!!")