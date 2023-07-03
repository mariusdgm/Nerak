from django.shortcuts import render, redirect
from datetime import datetime

BOT_EMOTICON = '&#129302;'
HUMAN_EMOTICON = "( ͡° ͜ʖ ͡°)"

messages = [
    {'sender': 'Bot', 'emoticon': BOT_EMOTICON, 'content': 'Hello!', 'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M")},   
]

def chat_page(request):
    if request.method == 'POST':
        # Retrieve the user's message from the form
        message = request.POST['message']
        
        # Add the user's message to the list of messages
        messages.append({'sender': 'User', 'emoticon': HUMAN_EMOTICON, 'content': message, 'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M")})

        # Redirect to the chat page to display the updated messages
        return redirect('chat_page')
    
    return render(request, 'chat_page.html', {'messages': messages})
