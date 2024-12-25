import streamlit as st

st.title("🎈 My new Streamlit app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

import streamlit as st
import google.generativeai as genai

def generate_prompt(tool1, tool2, task):
    """
    Generates a prompt for the Gemini API.

    Args:
        tool1: Name of the first tool.
        tool2: Name of the second tool.
        task: The task to perform (overview, comparison, project).

    Returns:
        The prompt string.
    """
    if task == "overview":
        return f"""
        Provide a concise overview (within 500 words) of the purpose of {tool1} and {tool2}. 
        """
    elif task == "comparison":
        return f"""
        Compare the pros and cons of {tool1} and {tool2} for beginners to start.
        """
    elif task == "project":
        return f"""
        Suggest a beginner-friendly project that utilizes {tool1} and {tool2}.
        """
    else:
        raise ValueError("Invalid task specified.")

# Streamlit App
st.title("AI Agent to Compare Two Tools 🛠️🔧")
st.caption("This app helps you compare the pros and cons of two tools.")

# Get API key from user input
api_key = st.text_input("Enter your Gemini API Key:", type="password") 

tool1 = st.text_input("Name of the first tool")
tool2 = st.text_input("Name of the second tool")

if st.button("Compare"):
    if api_key and tool1 and tool2:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel("gemini-1.5-flash") 

            st.write("**Overview:**")
            overview_prompt = generate_prompt(tool1, tool2, "overview")
            overview_response = model.generate_content(overview_prompt)
            st.write(overview_response.text) 

            st.write("**Comparison for Beginners:**")
            comparison_prompt = generate_prompt(tool1, tool2, "comparison")
            comparison_response = model.generate_content(comparison_prompt)
            st.write(comparison_response.text)

            st.write("**Beginner-Friendly Project:**")
            project_prompt = generate_prompt(tool1, tool2, "project")
            project_response = model.generate_content(project_prompt)
            st.write(project_response.text)

        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter your API key and the names of both tools.")