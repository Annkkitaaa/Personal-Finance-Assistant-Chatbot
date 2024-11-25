import pandas as pd
import json

# Sample Data: You can store this in a database or file later for persistence
expense_data = pd.DataFrame(columns=["Category", "Amount"])
goals = {}

def add_expense(category, amount):
    """Adds a new expense to the expense data."""
    global expense_data
    expense_data = expense_data.append({"Category": category, "Amount": amount}, ignore_index=True)

def get_summary():
    """Returns a summary of expenses by category."""
    return expense_data.groupby("Category")["Amount"].sum()

def calculate_budget(income, target_savings_percentage=20):
    """Calculates a budget based on income."""
    expenses = expense_data["Amount"].sum()
    target_savings = (income * target_savings_percentage) / 100
    suggested_budget = income - target_savings
    return f"Suggested Budget: {suggested_budget} after saving {target_savings}."

def set_goal(goal_name, target_amount):
    """Sets a financial goal."""
    goals[goal_name] = {"target": target_amount, "progress": 0}

def update_goal(amount, goal_name):
    """Updates the goal progress."""
    if goal_name in goals:
        goals[goal_name]["progress"] += amount
        return f"Goal '{goal_name}' Progress: {goals[goal_name]['progress']} / {goals[goal_name]['target']}"
    return "Goal not found."
