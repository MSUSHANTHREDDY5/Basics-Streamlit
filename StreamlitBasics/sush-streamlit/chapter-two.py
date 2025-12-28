import streamlit as st
from datetime import date 
st.title("Chai App")
if st.button("Make Chai"):
    st.success("Your Chai is Getting Ready")
add_masala=st.checkbox("Add Masala")
if add_masala:
    st.write("The masala is added")
chai_base=st.radio("Select the Tea Base:",["Milk","Water","Almond Milk"])
st.write(f"You selected {chai_base} as your Tea Base")
flavour=st.selectbox("Choose favour",["Normal","Allamm","Kesari","Tulsi"])
st.write(f"You selected {flavour} as your Tea Flavour")
sugar_level=st.slider("Suger level(spoon Wise)",0,5,2)
st.write(f"You selected {sugar_level} spoons of sugar")
cups=st.number_input("How many cups", min_value=1,max_value=10)
st.write(f"Selected sugar level {cups}")
name = st. text_input ("Enter your name")
if name:
    st.write(f"Hi {name},your Tea is Getting ready")

dob = st.date_input("Select your Date of Birth")
today = date.today()
age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

st.write(f"Your Date of Birth is: {dob}")
st.write(f"Your Age is: {age} years old")
