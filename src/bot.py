import os
from gpt4all import GPT4All

gptj = GPT4All("ggml-gpt4all-j-v1.3-groovy", model_path=os.path.join(".", "gpt4all_models"))
prompt_message = [{"role": "user", "content": "You play the role of a sarcastic and grumpy person called Nerak. You refuse to give any helpful answers, and instead answer with a sarcastic response while making fun of any question or task given to you. Start the conversation by welcoming the user as if you are working a call center support and you are having a bad day."},]
returned_answer = gptj.chat_completion(prompt_message, verbose=False, streaming=False)
print(f'🤖: { returned_answer["choices"][0]["message"]["content"] }')
print()

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        messages = [{"role": "user", "content": query}]
        returned_answer = gptj.chat_completion(messages, verbose=False, streaming=False)
        print(f'🤖: { returned_answer["choices"][0]["message"]["content"] }')
        print()
