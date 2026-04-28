# Sidebar Navigation
# Text input & sliders
# Data & Tables
# Image & Video
# Form Handling


import streamlit as st
import pandas as pd

st.set_page_config(page_title = "UI", 
               page_icon = "icon.png",
               layout = "wide")

#title
st.title("Streamlit User Interface App")

#sidebar
st.sidebar.title("Navigation")
option = st.sidebar.radio("Go to", ["Home", "Data", "Media", "Form", "Counter"])

#Home
if option == "Home":   
    st.header("Home Page")
    st.write("Welcome to the Home Page of the Streamlit User Interface App")

    name=st.text_input("Enter your name:")
    age=st.slider("Select your age:", 1, 100)
    if st.button("Submit"):
        st.success(f"Hello, {name}!, You are {age} years old.")


#Data
elif option == "Data":
    st.header("Data Page")

    df=pd.DataFrame({
        "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
        "Marks": [85, 90, 78, 92, 88],
    })

    st.dataframe(df)
    st.table(df)
    st.subheader("Charts")
    st.line_chart(df.set_index("Name")["Marks"])

elif option == "Media":
    st.header("Media Page")
    st.subheader("Play Media")
    st.image("image.jpg")
    st.video("output_video.avi")


elif option=="Form":
    st.header("Edunet Application Form")
    with st.form("my_form"):
        username = st.text_input("Enter your username:")
        password=st.text_input("Enter your password:", type="password")
        submit = st.form_submit_button("Login")
    if submit:
        st.success(f"Hello, {username} Welcome to Edunet.!")


#counter
elif option=="Counter":
    st.header("Counter Page")
    
    if "count" not in st.session_state:
        st.session_state.count = 0
    col1,col2=st.columns(2)

    with col1:
        if st.button("Increase "):
            st.session_state.count += 1
    with col2:
        if st.button("Decrease "):
            st.session_state.count -= 1
    st.write(f"Current Count: {st.session_state.count}")