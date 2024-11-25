import streamlit as st
from backend import add_expense, get_summary, calculate_budget, set_goal, update_goal
from chatbot import get_financial_advice
from utils import authenticate_user, register_user

# Streamlit Page Config
st.set_page_config(page_title="Personal Finance Assistant", page_icon="💸")

# Sidebar for Navigation
st.sidebar.title("Personal Finance Assistant")
option = st.sidebar.selectbox("Choose an action", ["Login", "Expense Tracking", "Budget Planning", "Financial Goals", "Chat with Assistant"])

# Handle user authentication
if option == "Login":
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate_user(username, password):
            st.success("Login successful!")
            st.session_state.username = username
        else:
            st.error("Invalid credentials. Please try again.")
            
    if st.button("Register New User"):
        if register_user(username, password):
            st.success("User registered successfully! Please log in.")
        else:
            st.error("Username already exists.")

elif 'username' in st.session_state:  # If user is authenticated
    # Expense Tracking Section
    if option == "Expense Tracking":
        st.title("Track Your Expenses")
        category = st.text_input("Expense Category (e.g., Food, Rent, Entertainment)")
        amount = st.number_input("Expense Amount", min_value=0.0, step=0.01)
        if st.button("Add Expense"):
            add_expense(category, amount)
            st.success(f"Added {amount} for {category}.")
        
        if st.button("Show Expense Summary"):
            summary = get_summary()
            st.write("Expense Summary by Category:")
            st.write(summary)

    # Budget Planning Section
    elif option == "Budget Planning":
        st.title("Plan Your Budget")
        income = st.number_input("Enter Your Monthly Income", min_value=0.0, step=0.01)
        if st.button("Calculate Budget"):
            budget_feedback = calculate_budget(income)
            st.write(budget_feedback)

    # Financial Goals Section
    elif option == "Financial Goals":
        st.title("Set and Track Financial Goals")
        goal_name = st.text_input("Goal Name (e.g., Vacation, Emergency Fund)")
        target_amount = st.number_input("Goal Target Amount", min_value=0.0, step=0.01)
        if st.button("Set Goal"):
            set_goal(goal_name, target_amount)
            st.success(f"Goal '{goal_name}' set with a target of {target_amount}.")
        
        if st.button("Update Goal Progress"):
            progress = st.number_input("Amount Contributed", min_value=0.0, step=0.01)
            progress_status = update_goal(progress, goal_name)
            st.write(progress_status)

    # Chat with Assistant Section
    elif option == "Chat with Assistant":
        st.title("Chat with Personal Finance Assistant")
        user_input = st.text_input("Ask a question (e.g., 'How can I save for retirement?')")
        if st.button("Get Advice"):
            if user_input:
                response = get_financial_advice(user_input)
                st.write(response)
            else:
                st.write("Please ask a question.")
else:
    st.write("Please log in to access the features.")
