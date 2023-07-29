import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# list of chat history.
# 'role' can be 'system', 'user', or 'assistant'
# 'system' gives the high-level instructions on how the model should answer questions
# 'user' specifies input messages (i.e., user input)
# 'assistant' specifies a prior message from the model
messages = [
    {"role": "system",
     "content": "You are a privacy policy analyst for mobile applications. The following portion"
                "of a privacy policy is for a mobile application. Analyze the paragraph and respond"
                "with a python list of labels where each label index corresponds to the same word in the"
                "privacy policy. The labels should be 'v' for verbs describing a data practice of "
                "the app with regard to the app user's data; 'i' for the information that is being"
                "accessed in any way by the app; and 'o' for any other terms."}
]

while True:
    # read from stdin
    message = input(">> ")
    if message:
        messages.append({"role": "user", "content": message})
        chat = openai.ChatCompletion.create(model=os.getenv("GPT_MODEL"), messages=messages)
        reply = chat.choices[0].message.content
        print(f"Model: {reply}")

        # remove the last message from history
        messages.pop(len(messages) - 1)
        # Only use the line below if the model should "remember" its reply
        #messages.append({"role": "assistant", "content": reply})

