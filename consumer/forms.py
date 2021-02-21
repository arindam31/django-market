from django import forms
from django.forms import Field
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from consumer.models import CustomUser, Address


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = CustomUser
        fields = UserChangeForm.Meta.fields


class CustomUserDetailsForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username', 'email', 'age')


class AddressCreationForm(forms.ModelForm):

    class Meta:
        model = Address
        fields = ('title', 'location', 'pincode', 'default')

    def check_for_existing_default_address(self):
        pass

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(AddressCreationForm, self).__init__(*args, **kwargs)

    def save(self):
        address = super(AddressCreationForm, self).save(commit=False)
        address.consumer = self.request.user
        address.save()
