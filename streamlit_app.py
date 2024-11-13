import streamlit as st
import sys
from typing import Any

def display_variable_info(var: Any) -> None:
    """Display information about a variable"""
    st.write(f"Type: {type(var).__name__}")
    st.write(f"Value: {var}")
    st.write(f"ID: {id(var)}")

# Title and introduction
st.title("🐍 Python Objects & Variables Explorer")
st.markdown("""
    This interactive playground helps you understand Python objects and variables. 
    Try out different examples and see how Python handles different types of objects!
""")

# Section 1: Basic Variable Assignment
st.header("1. Basic Variable Assignment")
st.markdown("Let's create some variables of different types:")

col1, col2, col3 = st.columns(3)
with col1:
    number = st.number_input("Enter an integer:", value=42)
    display_variable_info(number)

with col2:
    text = st.text_input("Enter some text:", value="Hello Python!")
    display_variable_info(text)

with col3:
    is_true = st.checkbox("Toggle a boolean")
    display_variable_info(is_true)

# Section 2: Variable Unpacking
st.header("2. Variable Unpacking")
st.markdown("Try unpacking values into multiple variables:")

list_input = st.text_input("Enter three comma-separated values:", value="1,2,3")
try:
    x, y, z = list_input.split(',')
    st.success("Unpacking successful!")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("x =", x)
    with col2:
        st.write("y =", y)
    with col3:
        st.write("z =", z)
except ValueError as e:
    st.error("Please enter exactly three comma-separated values")

# Section 3: Object Mutability
st.header("3. Object Mutability")
st.markdown("Explore how different objects behave when modified:")

# List example
st.subheader("Lists (Mutable)")
list_demo = [1, 2, 3]
st.write("Original list:", list_demo)
if st.button("Append 4 to list"):
    list_demo.append(4)
    st.write("Modified list:", list_demo)

# Tuple example
st.subheader("Tuples (Immutable)")
tuple_demo = (1, 2, 3)
st.write("Tuple:", tuple_demo)
if st.button("Try to modify tuple"):
    st.error("Tuples cannot be modified after creation!")

# Dictionary playground
st.header("4. Dictionary Playground")
st.markdown("Create and modify a dictionary:")

key = st.text_input("Enter a key:", "name")
value = st.text_input("Enter a value:", "Python")
demo_dict = {}

if st.button("Add to Dictionary"):
    demo_dict[key] = value
    st.write("Dictionary:", demo_dict)

# Interactive code execution
st.header("5. Code Playground")
code = st.text_area("Try your own Python code:", value="x = 42\nprint(f'x is of type {type(x)}')")
if st.button("Run Code"):
    try:
        exec(code)
        st.success("Code executed successfully!")
    except Exception as e:
        st.error(f"Error: {str(e)}")