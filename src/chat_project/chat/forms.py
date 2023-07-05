from django import forms

class MessageForm(forms.Form):
    message_text = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'placeholder': 'Send a message', 'autocomplete': 'off'}))  