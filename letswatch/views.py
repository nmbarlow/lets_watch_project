from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from letswatch.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from letswatch.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.staticfiles.templatetags.staticfiles import static

def index(request):
    context_dict = {'boldmessage': "Testing"}
    response = render(request, 'letswatch/index.html', context=context_dict)
    return response

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered=True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'letswatch/register.html', {'user_form':user_form, 'profile_form':profile_form, 'registered':registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your Let's Watch! account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'letswatch/login.html', {})

@login_required
def restricted(request):
    return render(request, 'letswatch/restricted.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

# @login_required
# def profile(request):
#
#     if request.method == 'POST':
#
#         user_form = ProfileForm(data=request.POST)
#         profile_form = UserProfileForm(data=request.POST)
#
#         if user_form.is_valid() and profile_form.is_valid():
#             # Get the current logged in User
#             user = User.objects.get(username=request.user.username)
#             user_profile = UserProfile.objects.get(user=user)
#
#         else:
#             user_form = ProfileForm()
#             profile_form = UserProfileForm()
#
#       return render(request, 'letswatch/profile.html', {'user_form': user_form,'profile_form': profile_form})


def search(request):
    if request.method == 'GET':
        query = request.GET.get('q')

        submitbutton = request.GET.get('submit')

        if query is not None:
            lookups = Q(title__icontains=query) | Q(content__icontains=query)

            results = Post.objects.filter(lookups).distinct()

            context = {'results': results,
                       'submitbutton': submitbutton}

            return render(request, 'search/search.html', context)

        else:
            return render(request, 'search/search.html')

    else:
        return render(request, 'search/search.html')


def about(request):
    return HttpResponse("About us page")
