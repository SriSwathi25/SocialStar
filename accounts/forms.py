from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()
        labels = {
            'username' : 'Display Name'
        }
        def __init__(self, *args, **kwargs):
            super(UserCreateForm,self).__init__(*args, **kwargs)
            self.fields['username'].label = "Display Name"
            self.fields['password1'].label = "Password"
            self.fields['password2'].label = "Confirm Password"