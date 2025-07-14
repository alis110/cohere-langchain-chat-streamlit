from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate
from langchain.memory import StreamlitChatMessageHistory
from langchain_cohere import ChatCohere

class LLM_Chat:
    def __init__(self, api_key):
        self.api_key = api_key
        self.llm = ChatCohere(
            model="command-r",
            cohere_api_key=self.api_key,
            streaming=True 
        )
        self.chat_history = StreamlitChatMessageHistory(key="special_app_key")

        self.prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system",
                "You are a conversational AI model that talks like a friend. "
                "You can communicate fluently in both English and Persian. "
                "When the user speaks Persian, respond in Persian. "
                "When the user speaks English, respond in English. "
                "If the user explicitly requests to speak in a specific language, follow their request and reply accordingly."),
                ("placeholder", "{chat_history}"),
                ("human", "{input}"),
            ]
        )

        self.chain_with_message_history = RunnableWithMessageHistory(
            self.prompt_template | self.llm,
            lambda session_id: self.chat_history,
            input_messages_key="input",
            history_messages_key="chat_history"
        )

    def reset_chat(self):
        self.chat_history.clear()
        self.chat_history.add_ai_message("Hello, how can I assist you?")

    def get_chat_history(self):
        return self.chat_history.messages

    def process_input(self, prompt):
        config = {"configurable": {"session_id": "any"}}
        self.chat_history.add_user_message(prompt)
        try:
            response = self.chain_with_message_history.invoke({"input": prompt}, config)
            self.chat_history.add_ai_message(response)
            return response
        except Exception as error:
            return str(error)
