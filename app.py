#!wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
!unzip ngrok-stable-linux-amd64.zip
! /content/ngrok authtoken 2COdcNWpkLVu4XjeM5n4D8El5uS_6naD4aoomGzaxMKXXqypB
get_ipython().system_raw('./ngrok http 8501 &')
!curl -s http://localhost:4040/api/tunnels | python3 -c \
'import sys, json; print("Execute the next cell and the go to the following URL:"+json.load(sys.stdin)["tunnels"][0]["public_url"])'

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
