import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash",google_api_key=st.secrets["GOOGLE_API_KEY"])

prompt = ChatPromptTemplate.from_template("Answer the question:\n{question}")

parser = StrOutputParser()
chain = prompt | llm | parser

st.title("🤖 Gemini Q&A App")
st.write("Ask me anything!")

user_question = st.text_input("Enter your question:")

if st.button("Get Answer"):
    if user_question:
        with st.spinner("Thinking..."):
            response = chain.invoke({"question": user_question})
            st.markdown(response)
    else:
        st.warning("Please enter a question")