from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML, Layout, Div
from crispy_forms.bootstrap import FormActions

class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    print '678'
    email = forms.CharField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)
    #args are variables, key-word arguments are variables and a value
    #val, val2='something'
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/contact/'
        
        self.helper.layout = Layout(
            Div('name', 'email', 'message', css_class="col-md-6"),)

        self.helper.layout.append(
            FormActions(
                Submit('submit', 'Submit', css_class='btn-primary', style='background:#89CCB1')
                )
            )