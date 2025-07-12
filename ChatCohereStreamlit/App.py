import streamlit as st
from model import LLM_Chat

class App:
    def __init__(self):
        st.set_page_config(page_title="Langchain: Chat With Cohere", page_icon="content/logo.png")
        st.title("🦜 Langchain: Chat With Cohere")
        st.markdown(f"""
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;500&display=swap');
                * {{font-family: 'Vazirmatn', sans-serif;}}
            </style>
        """, unsafe_allow_html=True)

    def display_sidebar(self):
        # Get Cohere API key from sidebar input
        st.sidebar.markdown("""
            <div style="padding:10px; background-color:#e0f7fa; border-radius:5px; margin-bottom:10px;">
                To use this app, you need a free API key from <a href="https://cohere.com/" target="_blank" style="color:#0077cc; text-decoration:none;">Cohere</a>. 
                Please enter your API key below after that press 'Enter'.
            </div>
        """, unsafe_allow_html=True)

        api_key = st.sidebar.text_input("Cohere API Key", type="password")
        if not api_key:
            st.info("Please enter Cohere API key to continue.")
            st.stop()
        if st.sidebar.button("Reset chat history"):
            return api_key, True
        return api_key, False

    def is_farsi(self, text):
        if not isinstance(text, str):
            return False
        for ch in text:
            if '\u0600' <= ch <= '\u06FF' or '\u0750' <= ch <= '\u077F' or '\u08A0' <= ch <= '\u08FF':
                return True
        return False

    def display_message(self, role, text):
        # Display a chat message with correct text direction and color
        direction = "rtl" if self.is_farsi(text) else "ltr"
        align = "right" if direction == "rtl" else "left"
        bg_color = "#ffeb3b" if role == "assistant" else "#f44336"
        with st.chat_message(role):
            st.markdown(f'''
                <div style="
                    direction: {direction};
                    text-align: {align};
                    background-color: {bg_color};
                    padding: 8px;
                    border-radius: 5px;
                    max-width: 80%;
                ">{text}</div>
            ''', unsafe_allow_html=True)

    def display_chat(self, chat_history):
        # Loop through chat history and display messages
        for role, content in chat_history:
            self.display_message(role, content)

    def run(self):
        # Main app logic
        api_key, reset = self.display_sidebar()

        if "chat_history" not in st.session_state:
            # Initialize chat history with a welcome message in English
            st.session_state.chat_history = [("assistant", "Hello! How can I help you today?")]


        backend = LLM_Chat(api_key)

        if reset:
            # Reset chat history to initial message
            st.session_state.chat_history = [("assistant", "Hello! How can I help you today?")]


        self.display_chat(st.session_state.chat_history)

        user_input = st.chat_input("Type your message here...")
        if user_input:
            st.session_state.chat_history.append(("user", user_input))
            response = backend.process_input(user_input)

            if hasattr(response, "content"):
                answer = response.content
            elif isinstance(response, dict) and "content" in response:
                answer = response["content"]
            else:
                answer = str(response)

            st.session_state.chat_history.append(("assistant", answer))

            self.display_message("user", user_input)
            self.display_message("assistant", answer)

if __name__ == "__main__":
    app = App()
    app.run()
