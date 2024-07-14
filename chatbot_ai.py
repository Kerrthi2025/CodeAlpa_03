import nltk
from nltk.chat.util import Chat, reflections

list = [
    [
        r"My name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot and I'm here to assist you.",]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you!",]
    ],
    [
        r"sorry (.*)",
        ["Apologies are not needed. How can I help you today?",]
    ],
    [
        r"(.*) thank you (.*)",
        ["You're welcome!",]
    ],
]

def chatbotai():
    print("Hello! I am Chatbot. How may I assist you today?")
    chat = Chat(list, reflections)
    while True:
        input = input("User: ")
        response = chat.respond(user_input)
        print("Chatbot:", response)
        if input == "exit":
            break

if __name__ == "__main__":
    chatbotai()
