
# Personal Finance Assistant Chatbot 💸

## Overview  
The **Personal Finance Assistant Chatbot** is a simple yet powerful tool designed to help users manage their personal finances effectively. Built using **Streamlit**, **LangChain**, and **Python**, this chatbot enables users to track expenses, plan budgets, set financial goals, and receive personalized advice on managing their money.

---

## Features  
### 🌟 Key Functionalities:
1. **Expense Tracking:**  
   - Input and categorize your daily expenses (e.g., Food, Rent, Entertainment).  
   - View summarized insights into your spending habits.

2. **Budget Planning:**  
   - Calculate suggested budgets based on your monthly income and target savings percentage.  
   - Get insights into your spending and savings balance.

3. **Financial Goals:**  
   - Set and track financial goals such as saving for a vacation or an emergency fund.  
   - Update your goal progress and monitor milestones.

4. **NLP Chatbot:**  
   - Ask financial questions like "What is compound interest?" or "How can I save for retirement?"  
   - Get advice powered by **LangChain**.

5. **User Authentication:**  
   - Secure user authentication to manage personal finance data securely.

6. **Real-Time Data Integration (Planned Enhancements):**  
   - Connect to free APIs to sync expenses with bank data for real-time tracking.

---

## Project Structure  
```plaintext
finance-assistant-chatbot/
│
├── backend.py           # Finance logic and data handling
├── chatbot.py           # LangChain-based NLP chatbot logic
├── streamlit_app.py     # Main Streamlit app for user interaction
├── utils.py             # Utility functions (authentication, etc.)
├── requirements.txt     # Python dependencies
├── README.md            # Project description and instructions
└── data/                # Folder for saving user data locally
```

---

## Installation  
Follow these steps to set up and run the project on your local machine:

1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/your-username/finance-assistant-chatbot.git
   cd finance-assistant-chatbot
   ```

2. **Install Dependencies**:  
   Use the following command to install required libraries:  
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up OpenAI API Key**:  
   Add your OpenAI API key to `chatbot.py` in the `openai_api_key` parameter. You can get a free key [here](https://platform.openai.com/signup/).  

4. **Run the Application**:  
   Launch the chatbot using Streamlit:  
   ```bash
   streamlit run streamlit_app.py
   ```

5. **Access the App**:  
   Open the provided URL (usually `http://localhost:8501`) in your browser.

---

## Usage Instructions  
1. **Login or Register**:  
   - Navigate to the Login page and log in or register as a new user.

2. **Expense Tracking**:  
   - Add your daily expenses and categorize them.  
   - View a summary of your expenses by category.

3. **Budget Planning**:  
   - Input your monthly income to get personalized budget advice.

4. **Set Financial Goals**:  
   - Define financial goals and track progress as you save toward them.

5. **Chat with the Bot**:  
   - Ask financial queries and receive AI-driven advice.

---

## Future Enhancements  
- **Real-Time Data Integration**: Sync with APIs like Plaid or other free tools for real-time expense tracking.  
- **Advanced Goal Tracking**: Set detailed goals with reminders for milestones.  
- **Improved NLP**: Enhance chatbot understanding with custom financial datasets.  

---

## Dependencies  
This project uses the following libraries:  
- **Streamlit**: For building the interactive web app.  
- **LangChain**: For creating the conversational chatbot.  
- **Pandas**: For managing expense and goal data.  
- **OpenAI**: For generating chatbot responses.  

Install all dependencies via the `requirements.txt` file.

---

## Contact  
If you have questions or need help setting up, feel free to reach out:  
**Ankita Singh**  
- [GitHub](https://github.com/Annkkitaaa)  
- [Portfolio](https://ankitasingh.vercel.app/)  

---
