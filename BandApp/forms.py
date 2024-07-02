from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class SignUpForm(forms.Form):
    """This class will create a sign up form

    Parameters:
        forms.form: form

    Attributes:
        username: Char
        password: Char
        first_name: Char
    """
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=100)


    def clean_username(self):
        """This function will check if the username is available

        Parameters:
            self: SignUpForm object

        Returns:
            username: str
        """
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("A user with this username already exists. Please choose a different username.")
        return username
    

    def save(self):
        """This method will save the user to the database

        Parameters:
            self: SignUpForm object
            
        Returns:
            None
        """
        user = User.objects.create_user(
            self.cleaned_data['username'],
            None,
            self.cleaned_data['password']
        )
        user.first_name = self.cleaned_data['first_name']
        user.save()
        return user