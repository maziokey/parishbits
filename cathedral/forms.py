from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class ContactForm(forms.Form):
    name = forms.CharField(required=True, label='Your Name', widget=forms.TextInput())
    email = forms.EmailField(required=True, label='Your Email', widget=forms.TextInput())
    subject = forms.CharField(required=True, label='Subject', widget=forms.TextInput())
    message = forms.CharField(widget=forms.Textarea(), required=True, label='Message')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False