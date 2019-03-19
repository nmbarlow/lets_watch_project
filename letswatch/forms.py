from django import forms
from django.contrib.auth.models import User
from letswatch.models import Genre, Movie, UserProfile, Review, Hotel

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
    yeah = forms.CharField(max_length=4, help_text="Please enter the year of the movie.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    picture=forms.ImageField(required=False, label="Picture")
    thumb=forms.ImageField(required=False, label="thumb")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

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
    email=forms.CharField(widget=forms.TextInput(attrs=
        {'name':'email',
        'class':'form-control my-input',
        'id':'email',
        'placeholder':'Email',
        }),label=""
    )
    username=forms.CharField(widget=forms.TextInput(attrs=
        {'name':'name',
        'class':'form-control my-input',
        'id':'name',
        'placeholder':'Name',
        }),label=""
    )
    password = forms.CharField(widget=forms.PasswordInput(
        attrs=
        {'name':'password',
        'class':'form-control my-input',
        'id':'password',
        'placeholder':'Password',
        'min':'0',

        }),label="")

#An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    picture = forms.ImageField(required=True, label="")

    class Meta:
        model = UserProfile
        fields = ('picture',)

class ProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        # Provide an association between the ModelForm and a model
        model = User
        fields = ('password',)

class HotelForm(forms.ModelForm):

    class Meta:
        model = Hotel
        fields = ['name', 'hotel_Main_Img']

class ReviewForm(forms.ModelForm):

    # date = forms.DateField(widget=forms.HiddenInput(), initial = datetime,required=False)
    rating = forms.IntegerField(widget=forms.HiddenInput(), initial =0)
    content = forms.TextInput()

    class Meta:
        model = Review
        fields = ['date','rating', 'content',]
