# Cohere Langchain Chat Streamlit

A simple and interactive AI chat application built with Langchain, Cohere API, and Streamlit.  
This project allows you to chat with Cohere’s conversational model in real-time and save your chat history.

---

## Features

- Uses Cohere conversational model with streaming responses  
- Saves and displays chat history in the Streamlit UI  
- Reset chat history and start a new conversation  
- Supports both English and Persian languages with automatic text direction  
- Clean and simple UI styled with the Vazirmatn font (great for Persian)  

---

## Live Demo

Check out the live demo of this app here:  
[Cohere Langchain Chat on Streamlit](https://cohere-langchain-chat-app-dwhraurbr6gz5jwwab3t2g.streamlit.app/)

---

## Requirements

- Python 3.8 or higher  
- A Cohere API key (Sign up at [Cohere](https://cohere.com/) to get your free API key)  

---

## Installation

First, clone the repository:

```bash
git clone https://github.com/alis110/cohere-langchain-chat-streamlit.git
cd cohere-langchain-chat-streamlit
```

Then install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the App

Run the Streamlit app with the following command:

```bash
streamlit run ChatCohereStreamlit/App.py
```

---

## Usage

- Enter your Cohere API key in the sidebar after launching the app.  
- Start chatting with the model interactively.  
- Click the **Reset chat history** button in the sidebar to start a new conversation.  

---

## Important Notes

- Keep your API key confidential and avoid pushing it to public repositories.  
- The model automatically detects the language of your input and responds in the same language (English or Persian).  
- Streaming responses are currently disabled but can be enabled for a better chat experience.  

---

## Documentation & Resources

- [Cohere API Documentation](https://docs.cohere.ai)  
- [Streamlit Documentation](https://docs.streamlit.io)  
- [Langchain Documentation](https://python.langchain.com)  

---

## License

This project is licensed under the MIT License.

---

## Contact & Contribution

Feel free to open issues or pull requests if you have suggestions or improvements.

---

##### Developed by AliSajad | 2025
