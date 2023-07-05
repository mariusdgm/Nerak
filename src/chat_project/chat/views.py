from django.shortcuts import render, redirect
from .forms import MessageForm
from datetime import datetime

from chat_project.gpt4all_instance import gptj

BOT_EMOTICON = "¯\_(ツ)_/¯"
HUMAN_EMOTICON = "( ͡° ͜ʖ ͡°)"

prompt_message = [{"role": "user", "content": "You play the role of a sarcastic and grumpy person called Nerak. You always answer in a sarcastic manner and provide no useful responses. Make sure that you never answer with the same answer consecutively. Start the conversation by welcoming the user and introducing yourself."},]
returned_answer = gptj.chat_completion(prompt_message, verbose=False, streaming=False)

messages = [
    {
        "sender": "bot",
        "emoticon": BOT_EMOTICON,
        "content": returned_answer["choices"][0]["message"]["content"],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
    },
]


def chat_page(request):
    message_form = MessageForm()

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            user_message_text = form.cleaned_data['message_text']
            built_message = [{"role": "user", "content": user_message_text}]
            returned_answer = gptj.chat_completion(built_message, verbose=False, streaming=False)

            messages.append(
                {
                    "sender": "user",
                    "emoticon": HUMAN_EMOTICON,
                    "content": user_message_text,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
                }
            )

            messages.append(
                {
                    "sender": "bot",
                    "emoticon": BOT_EMOTICON,
                    "content": returned_answer["choices"][0]["message"]["content"],
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
                }
            )


    return render(request, "chat_page.html", {"messages": messages, "message_form": message_form})
