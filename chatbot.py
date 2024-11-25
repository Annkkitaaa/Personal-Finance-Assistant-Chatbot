from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import ConversationChain

# Initialize OpenAI model (replace with your OpenAI API key)
llm = OpenAI(openai_api_key="your-openai-api-key")

# Define the prompt template for personal finance questions
prompt_template = """
You are a personal finance assistant. Answer questions related to budgeting, saving, investments, and expense tracking.
User: {input}
Assistant:
"""
template = PromptTemplate(input_variables=["input"], template=prompt_template)
conversation_chain = ConversationChain(prompt=template, llm=llm)

def get_financial_advice(user_input):
    """Generates financial advice based on user input."""
    response = conversation_chain.run(input=user_input)
    return response
