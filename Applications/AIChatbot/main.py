from openai import OpenAI
key = "" #use your OpenAI API Key

messages = []

client = OpenAI(
    api_key=key,  # This is the default and can be omitted
)

def completion(message):
    global messages
    messages.append(
        {
            "role": "user",
            "content": message
        }
    )

    chat_completion = client.chat.completions.create( messages=messages,
                        model="gpt-4o"
                        )
    
    # print(chat_completion)
    message = {
        "role": "assistant",
        "content": chat_completion.choices[0].message.content
    }
    messages.append(message)
    print(f"\nAIBot: {message["content"]}\n")
    


while True:
        print(f"AIBot: Hi I am AIBot, How may I help you\n")
        user_question = input("User: ")
        completion(user_question)
