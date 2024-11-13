import streamlit as st
from typing import Any
import sys
from io import StringIO

def display_variable_info(var: Any, show_id: bool = False) -> None:
    """Display information about a variable with optional ID display"""
    st.write(f"Type: {type(var).__name__}")
    st.write(f"Value: {var}")
    if show_id:
        st.write(f"Memory ID: {id(var)}")

# Title and introduction
st.title("🐍 Python Objects & Variables Explorer")
st.markdown("""
    Learn about Python variables, objects, and data types through this interactive guide.
    Each section includes examples and explanations to help you understand core Python concepts.
""")

# Section 1: Basic Variable Assignment
st.header("1. Basic Variable Assignment")
st.markdown("""
    In Python, variables are names that refer to values. When you assign a value to a variable,
    Python creates an object and makes the variable point to it.
    
    For example:
    ```python
    age = 25              # Integer
    name = "Alice"        # String
    is_student = True     # Boolean
    ```
""")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Try it yourself:")
    number = st.number_input("Enter a number:", value=42)
    text = st.text_input("Enter text:", value="Hello Python!")
    is_true = st.checkbox("Toggle a boolean")
    
with col2:
    st.subheader("See the results:")
    st.markdown("Your variables are stored as:")
    st.code(f"""
number = {number}    # Type: {type(number).__name__}
text = "{text}"    # Type: {type(text).__name__}
is_true = {is_true}    # Type: {type(is_true).__name__}
""")

# Section 2: Lists vs Tuples
st.header("2. Lists vs Tuples")
st.markdown("""
    Lists and tuples are both sequences, but they have a key difference:
    - Lists are **mutable** (can be modified)
    - Tuples are **immutable** (cannot be modified)
    
    Example:
    ```python
    # List
    fruits = ['apple', 'banana']
    fruits.append('orange')     # This works!
    
    # Tuple
    coordinates = (10, 20)
    coordinates[0] = 30         # This raises an error!
    ```
""")

# Interactive List Demo
st.subheader("Interactive List Demo")
demo_list = ['apple', 'banana']
st.write("Starting list:", demo_list)

new_item = st.text_input("Enter an item to add:", "orange")
if st.button("Add to list"):
    demo_list.append(new_item)
    st.write("Updated list:", demo_list)
    st.code(f"demo_list = {demo_list}")

# Section 3: Dictionaries
st.header("3. Dictionaries")
st.markdown("""
    Dictionaries are key-value pairs - think of them like a contact list in your phone:
    - Keys are unique (like phone contacts' names)
    - Values can be any type (numbers, strings, lists, even other dictionaries!)
    
    **Creating a Dictionary:**
    ```python
    # Empty dictionary
    my_dict = {}
    
    # Dictionary with initial values
    person = {
        'name': 'Alice',
        'age': 25,
        'hobbies': ['reading', 'hiking']
    }
    ```
    
    **Common Dictionary Operations:**
    ```python
    # Adding/Updating items
    person['city'] = 'New York'     # Adds new key-value pair
    person['age'] = 26              # Updates existing value
    
    # Accessing items
    print(person['name'])           # Output: Alice
    print(person.get('email'))      # Output: None (safer than direct access)
    
    # What happens if key doesn't exist?
    print(person['email'])          # Raises KeyError!
    print(person.get('email'))      # Returns None (safe)
    print(person.get('email', 'Not found'))  # Returns 'Not found'
    ```
""")

st.subheader("Build a Dictionary")
demo_dict = {}

col1, col2 = st.columns(2)
with col1:
    key = st.text_input("Enter a key:", "name")
    value = st.text_input("Enter a value:", "Alice")
    if st.button("Add to Dictionary"):
        demo_dict[key] = value
        st.write("Your dictionary:", demo_dict)
        st.code(f"""
# Your dictionary code:
demo_dict = {demo_dict}

# Try accessing values:
print(demo_dict['{key}'])  # Output: {value}
print(demo_dict.get('nonexistent', 'Not found'))  # Output: Not found
""")

with col2:
    st.markdown("""
    **Try These Keys:**
    - name → stores person's name
    - age → stores person's age
    - hobbies → stores a list of hobbies
    
    **What's Happening:**
    1. When you enter a key and value, Python:
        - Creates space for the new key-value pair
        - Adds it to the dictionary
    2. Keys must be unique:
        - Using same key updates the value
        - Different keys can have same values
    """)

# Section 4: Code Playground
st.header("4. Code Playground")
st.markdown("""
    Try writing your own Python code! Here are some ideas:
    
    **Working with Dictionaries:**
    ```python
    # Create a student record
    student = {'name': 'Alex', 'grades': [85, 90, 88]}
    
    # Add new grade
    student['grades'].append(92)
    
    # Calculate average
    avg = sum(student['grades']) / len(student['grades'])
    print(f"Average grade: {avg}")
    ```
    
    **Working with Lists:**
    ```python
    # Create and modify a shopping list
    shopping = ['milk', 'bread']
    shopping.append('eggs')
    print(f"Need to buy: {shopping}")
    ```
""")

code = st.text_area("Write your Python code:", value="""# Try this example:
student = {'name': 'Alex', 'grades': [85, 90, 88]}
student['grades'].append(92)

print(f"Student: {student['name']}")
print(f"Grades: {student['grades']}")
avg = sum(student['grades']) / len(student['grades'])
print(f"Average grade: {avg:.1f}")
""")

if st.button("Run Code"):
    # Capture the output
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    
    try:
        exec(code)
        output = mystdout.getvalue()
        st.write("Output:")
        st.code(output)
    except Exception as e:
        st.error(f"Error: {str(e)}")
    finally:
        sys.stdout = old_stdout

# Footer with tips
st.markdown("""
---
💡 **Key Takeaways:**
- Variables are names that point to values in memory
- Different data types (int, str, bool) serve different purposes
- Lists are mutable, tuples are immutable
- Dictionaries are perfect for storing related data using key-value pairs
- Dictionary keys must be unique, but values can be duplicated
- Use .get() for safe dictionary access to avoid errors
""")