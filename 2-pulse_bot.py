from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama  # Correct import for Ollama
import streamlit as st

# Set the app title
st.title("Alina Bot using DeepSeek-R1")

# Define the prompt template
template = """Question: {question}

Answer: Let's think step by step."""

# Create the prompt template using the given template
prompt = ChatPromptTemplate.from_template(template)

# Initialize the Ollama model
model = Ollama(model="deepseek-r1")  # Ensure the model name is correct

# Create a chain with the prompt and the model
chain = prompt | model

# Use text_input to capture user question
question = st.text_input("Enter your question here")

# If the user has entered a question, format the prompt and invoke the chain
if question:
    try:
        # Format the input question with the template
        formatted_prompt = prompt.format(question=question)
        
        # Pass the formatted prompt to the chain
        response = chain.invoke({"question": question})  # Pass as a dictionary
        
        # Display the response from the model
        st.write("**Response:**")
        st.write(response)
    except Exception as e:
        st.error(f"Error: {e}")