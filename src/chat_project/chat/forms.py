from django import forms


class MessageForm(forms.Form):
    message_text = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'placeholder': 'Send a message', 'autocomplete': 'off'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['message_text'].widget.attrs['oninput'] = 'updateSubmitButton(this)'

    def is_submit_disabled(self):
        if self.is_bound and 'message_text' in self.cleaned_data:
            return self.cleaned_data['message_text'].strip() == ''
        return True

    def clear_input_field(self):
        self.cleaned_data['message_text'] = ''