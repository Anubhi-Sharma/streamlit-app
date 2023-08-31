import altair as alt
import streamlit as st 

def find_largest_number(a, b, c):
    return max(a, b, c)

st.title("Largest Number Finder")

st.write("Enter three numbers:")
a = st.number_input("Enter the first number:")
b = st.number_input("Enter the second number:")
c = st.number_input("Enter the third number:")

if st.button("Find Largest"):
    largest = find_largest_number(a, b, c)
    st.success(f"The largest number is: {largest}")