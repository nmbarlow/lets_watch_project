from django import forms
from django.contrib.auth.models import User
from letswatch.models import Genre, Movie, UserProfile

class GenreForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the genre name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Genre
        fields = ('name',)

class MovieForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the movie.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the movie.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        # If url is not empty and doesn't start with 'http://',
        # then prepend 'http://'.
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

            return cleaned_data

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Movie

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them.
        # Here, we are hiding the foreign key.
        # we can either exclude the genre field from the form,
        exclude = ('genre',)
        # or specify the fields to include (i.e. not include the genre field)
        # fields = ('title', 'url', 'views')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

#An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False, label="")

    class Meta:
        model = UserProfile
        fields = ('profile_picture',)

class ProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        # Provide an association between the ModelForm and a model
        model = User
        fields = ('password',)
