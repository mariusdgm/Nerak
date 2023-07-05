from django import forms


class MessageForm(forms.Form):
    message_text = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'placeholder': 'Send a message', 'autocomplete': 'off'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['message_text'].widget.attrs['oninput'] = 'updateSubmitButton(this)'

    def is_submit_disabled(self):
        return not self.is_bound or self.cleaned_data['message_text'].strip() == ''
