from django import forms
from django.contrib.auth.models import User
from rango.models import Page, Category, UserProfile,Movie

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,help_text="Please enter the category name.")
    views =forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    likes =forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    slug =forms.CharField(widget=forms.HiddenInput(),required=False)
    class Meta:
        model=Category
        fields=('name',)

class PageForm (forms.ModelForm):

    title =forms.CharField(max_length=128,help_text="Please enter the title of the page.")
    url=forms.URLField(max_length=200,help_text="Please enter the URL of the page.")
    views =forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    #check for correct url
    def clean(self):
    	cleaned_data=self.cleaned_data
    	url=cleaned_data.get('url')
    	if url and not url.startswith('http://'):
    		url='http://'+url
    		cleaned_data['url']=url
    		return cleaned_data
    		
    class Meta:
        model=Page

        exclude=('category',)

class MovieForm (forms.ModelForm):

    title =forms.CharField(max_length=128,help_text="Please enter the name of the movie.")
    trailer=forms.URLField(max_length=200,help_text="Please enter the URL of the movie.")
    genre= forms.ChoiceField(choices={"comedy","action","horror"})
    views =forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    image=forms.ImageField()
    #check for correct url
    def clean(self):
        cleaned_data=self.cleaned_data
        url=cleaned_data.get('url')
        
    class Meta:
        model=Page

     


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
    password=forms.CharField(widget=forms.PasswordInput(
        attrs=
        {'name':'password',
        'class':'form-control my-input',
        'id':'password',
        'placeholder':'Password',
        'min':'0',

        }),label=""
    )

    class Meta:
        model=User
        fields=('username','email','password')

class UserProfileForm(forms.ModelForm):
    picture=forms.ImageField()
    class Meta:
        model=UserProfile
        fields=('website','picture')
        