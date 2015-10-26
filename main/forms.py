from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML, Layout, Div
from crispy_forms.bootstrap import FormActions
from main.models import Cereal, Manufacturer

class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)
    #args are variables, key-word arguments are variables and a value
    #val, val2='something'
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/contact/'
        
        self.helper.layout = Layout(
            Div('name', 'email', 'message',css_class="col-md-9"),)

        self.helper.layout.append(
            FormActions(
                Submit('submit', 'Submit', css_class='btn-primary', style='background:#89CCB1; width:20%; margin-left:28%; margin-top:0px')
                )
            )
class CerealNewForm(forms.ModelForm):
    class Meta:
        model = Cereal
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CerealNewForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/cereal_new/'
        self.helper.layout.append(
            FormActions(
                Submit('save_changes', 'Save Changes', css_class='btn-primary', style='background:#89CCB1'),
                )
            )
class ManNewForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ManNewForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/man_new/'
        self.helper.layout.append(
            FormActions(
                Submit('save_changes', 'Save Changes', css_class='btn-primary', style='background:#89CCB1'),
                )
            )
class CerealEditForm(forms.ModelForm):
    class Meta:
        model = Cereal
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CerealEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/cereal_edit/%s/' % self.instance.pk
        self.helper.layout.append(
            FormActions(
                Submit('save_changes', 'Save Changes', css_class='btn-primary', style='background:#89CCB1'),
                )
            )

class ManEditForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ManEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/man_edit/%s/' % self.instance.pk
        self.helper.layout.append(
            FormActions(
                Submit('save_changes', 'Save Changes', css_class='btn-primary', style='background:#89CCB1'),
                )
            )
class CerealRemoveForm(forms.ModelForm):
    class Meta:
        model = Cereal
        fields = []

    def __init__(self, *args, **kwargs):
        super(CerealRemoveForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/cereal_remove/%s/' % self.instance.pk
        self.helper.layout.append(
            FormActions(
                Submit('remove_cereal', 'Remove Cereal', css_class='btn-primary', style='margin-left:42%; background:#89CCB1'),
                )
            )
class ManRemoveForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = []

    def __init__(self, *args, **kwargs):
        super(ManRemoveForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/man_remove/%s/' % self.instance.pk
        self.helper.layout.append(
            FormActions(
                Submit('remove_man', 'Remove Manufacturer', css_class='btn-primary', style='margin-left:41.5%; background:#89CCB1'),
                )
            )
class UserLogin(forms.Form):  
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())

    # def __init__(self, *args, **kwargs):
    #     super(UserLogin, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper(self)
    #     self.helper.form_action = '/login/'
    #     self.helper.layout = Layout(
    #                 'username',
    #                 'password',
    #                 )

class UserSignUp(forms.Form): 
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)

    # def __init__(self, *args, **kwargs):
    #     super(UserSignUp, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper(self)
    #     self.helper.form_action = '/signup/'
    #     self.helper.layout = Layout(
    #                 'username',
    #                 'email',
    #                 'password',
    #                 )
    #     self.helper.layout.append(
    #         FormActions(
    #             Submit('submit', 'Create New User', css_class="btn-primary")
    #             )
    #         )

