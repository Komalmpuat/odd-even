import streamlit as st
import pandas as pd
st.header("Odd Even testing App")
st.write("Enter test data")
def user_inputs():
  input_number = st.number_input("Enter number to check",min_value=0,step=1)
  st.subheader("Result")
  if (input_number % 2)==0:
     st.write("Number is Even")
  else:
    st.write("Number is Odd")
user_inputs()
