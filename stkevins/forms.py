from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Div, Field

class GroupForm(forms.Form):
    name = forms.CharField(required=True, label='Name', widget=forms.TextInput())
    parishioner_id = forms.CharField(required=False, label='Parishioner ID', widget=forms.TextInput())
    group = forms.CharField(required=True, label='Group', widget=forms.TextInput())
    email = forms.EmailField(required=False, label='Email', widget=forms.TextInput())
    phone = forms.CharField(required=False, label='Phone', widget=forms.TextInput())
    motivation = forms.CharField(widget=forms.Textarea(), required=True, label='Reason For Joining')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = True
        self.helper.layout = Layout(
            Field('name', id="name", css_class="h-full-width", title="Your Name"),
            Field('parishioner_id', id="parishioner_id", css_class="h-full-width", title="Parish ID"),
            Field('group', id="group", css_class="h-full-width", title="Group To Join"),
            Field('email', id="email", css_class="h-full-width", title="Your Email"),
            Field('phone', id="phone", css_class="h-full-width", title="Phone No"),
            Field('motivation', id="motivation", css_class="h-full-width", title="Motivation For Joining"),
            #Field('name', id="name", css_class="h-full-width", title="Your name")
            Submit('submit', 'Submit', css_class='btn--primary h-full-width')
        )


class SocietyForm(forms.Form):
    name = forms.CharField(required=True, label='Name', widget=forms.TextInput())
    parishioner_id = forms.CharField(required=False, label='Parishioner ID', widget=forms.TextInput())
    society = forms.CharField(required=True, label='Pius Society To Join', widget=forms.TextInput())
    email = forms.EmailField(required=False, label='Email', widget=forms.TextInput())
    phone = forms.CharField(required=False, label='Phone', widget=forms.TextInput())
    motivation = forms.CharField(widget=forms.Textarea(), required=True, label='Reason For Joining')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = True
        self.helper.layout = Layout(
            Field('name', id="name", css_class="h-full-width", title="Your Name"),
            Field('parishioner_id', id="parishioner_id", css_class="h-full-width", title="Parish ID"),
            Field('society', id="society", css_class="h-full-width", title="Pius Society To Join"),
            Field('email', id="email", css_class="h-full-width", title="Your Email"),
            Field('phone', id="phone", css_class="h-full-width", title="Phone No"),
            Field('motivation', id="motivation", css_class="h-full-width", title="Motivation For Joining"),
            #Field('name', id="name", css_class="h-full-width", title="Your name")
            Submit('submit', 'Submit', css_class='btn--primary h-full-width')
        )



"""
def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div('first_name', css_class='form-group col-4'),
                Div('last_name', css_class='form-group col-4'),
                Div('email', css_class='form-group col-4'),
                css_class='form-row'
            ),
            Div(
                Div('password', css_class='form-group col-4'),
                Div('confirm_password', css_class='form-group col-4'),
                css_class='form-row'
            ),
            Div(
                Div('gender', css_class='form-group col-4'),
                Div('phone_number', css_class='form-group col-8'),
                css_class='form-row'
            ),
            'about_you',
            Submit('submit', 'Sign up', css_class='mt-4')
        )
        
        Div('name', css_class='h-full-width', title="Your name")
        Field('name', id="name", css_class="h-full-width", title="Your name")
        <div>
            <label for="sampleInput">Your email</label>
            <input class="h-full-width" type="email" placeholder="test@mailbox.com" id="sampleInput">
        </div>
"""