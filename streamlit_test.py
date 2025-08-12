import streamlit as st
import requests

st.title("FBL HR AI ChatBot")

user_input = st.text_input("Ask a question:")

if st.button("Submit") and user_input:
    with st.spinner("Thinking..."):
        try:
            response = requests.post(
                "https://6aae8d6c0fae.ngrok-free.app/query",
                json={"question": user_input}
            )
            data = response.json()
            st.success("✅ Answer:")
            st.write(data["answer"])
            #st.markdown(f"**Source:** {data['source']}")
        except Exception as e:
            st.error(f"Error: {e}")



