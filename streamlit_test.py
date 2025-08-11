import streamlit as st
import requests

st.title("FBL Operations AI ChatBot")

user_input = st.text_input("Ask a question:")

if st.button("Submit") and user_input:
    with st.spinner("Thinking..."):
        try:
            response = requests.post(
                "http://localhost:5000/query",
                json={"question": user_input}
            )
            data = response.json()
            st.success("✅ Answer:")
            st.write(data["answer"])
            #st.markdown(f"**Source:** {data['source']}")
        except Exception as e:
            st.error(f"Error: {e}")
