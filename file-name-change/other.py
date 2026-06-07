import streamlit as st

st.set_page_config(page_title="Streamlit Calculator", page_icon="🧮")
st.title("🧮 Calculator with Streamlit")

# Inputs
col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("First number", value=0.0)
with col2:
    num2 = st.number_input("Second number", value=0.0)

# Operation
operation = st.radio("Choose operation", ["+", "-", "×", "÷"], horizontal=True)

# Calculate
if st.button("Calculate"):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "×":
        result = num1 * num2
    elif operation == "÷":
        result = num1 / num2 if num2 != 0 else "Error: Divide by 0"
    
    st.success(f"Result = {result}")

st.markdown("---")
st.caption("Run with: streamlit run calculator.py")