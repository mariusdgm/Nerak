import json
import time

from chat_project.gpt4all_instance import gptj, chat_history

from django.shortcuts import render, redirect
from .forms import MessageForm
from datetime import datetime
from django.http import JsonResponse

BOT_EMOTICON = "¯\_(ツ)_/¯"
HUMAN_EMOTICON = "( ͡° ͜ʖ ͡°)"

prompt_message = {"role": "user", "content": "You play the role of a sarcastic and grumpy person called Nerak. You always answer in a sarcastic manner and provide no useful responses. Make sure that you never answer with the same answer consecutively. Start the conversation by welcoming the user and introducing yourself."}
chat_history.append(prompt_message)
returned_answer = gptj.chat_completion(chat_history, verbose=False, streaming=False)
# returned_answer = gptj.chat_completion([prompt_message], verbose=False, streaming=False)
chat_history.append(returned_answer["choices"][0]["message"])

displayed_messages = [
    {
        "sender": "bot",
        "emoticon": BOT_EMOTICON,
        "content": returned_answer["choices"][0]["message"]["content"],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
    },
]

def chat_page(request):
    form = MessageForm()
    if request.method == "POST":
        form = MessageForm(request.POST)
       
        if form.is_valid():

            user_message_text = form.cleaned_data['message_text']
            built_message = {"role": "user", "content": user_message_text}
            chat_history.append(built_message)

            returned_answer = gptj.chat_completion(chat_history, verbose=False, streaming=False)
            # returned_answer = gptj.chat_completion([built_message], verbose=False, streaming=False)
            
            chat_history.append(returned_answer["choices"][0]["message"])

            displayed_messages.append(
                {
                    "sender": "user",
                    "emoticon": HUMAN_EMOTICON,
                    "content": user_message_text,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
                }
            )

            displayed_messages.append(
                {
                    "sender": "bot",
                    "emoticon": BOT_EMOTICON,
                    "content": returned_answer["choices"][0]["message"]["content"],
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
                }
            )

            form = MessageForm()

            response_data = {
                    "user_message": user_message_text,
                    "bot_message": returned_answer["choices"][0]["message"]["content"],  # Replace with actual bot response
                }
            return JsonResponse(response_data)

    return render(request, "chat_page.html", {"messages": displayed_messages, "message_form": form})
