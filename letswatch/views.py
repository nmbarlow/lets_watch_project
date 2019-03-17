from django.shortcuts import render
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
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True
        else:

            print(user_form.errors, profile_form.errors)
    else:

        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'letswatch/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

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
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@ login_required
def deactivate_profile(request):

    user = request.user
    user.is_active= False
    user.save()

    context_dict = 'Profile successfully deactivated'

    return render(request, 'letswatch/deactivate_profile.html', context=context_dict)

def profile(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('home')

    userprofile = UserProfile.objects.get_or_create(user=user)[0]

    form = UserProfileForm({'picture': userprofile.picture})


    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if form.is_valid():
            form.save(commit=True)
            return redirect('user_profile', user.username)
        else:
            print(form.errors)

    return render(request, 'letswatch/userprofile.html',
                  {'userprofile': userprofile, 'user': user, 'form': form})


@login_required
def movie_review(request):

    context_dict = {}
    rate = Rate.objects.filter()

    context_dict['rate'] = rate

    return render(request, 'letswatch/review_movie.html', context_dict)

@login_required
def review_movie(request):

    if request.method == 'GET':

        movie_id = request.GET['movieid']
        likes = 0

        if movie_id:
            movie = Movie.objects.get(id=int(movie_id))

            if movie:
                likes = movie.likes + 1
                movive.likes = likes
                movie.save()

            return HttpResponse(likes)

# def search(request):
#     if request.method == 'GET':
#         query = request.GET.get('q')
#
#         submitbutton = request.GET.get('submit')
#
#         if query is not None:
#             lookups = Q(title__icontains=query) | Q(content__icontains=query)
#
#             results = Post.objects.filter(lookups).distinct()
#
#             context = {'results': results,
#                        'submitbutton': submitbutton}
#
#             return render(request, 'search/search.html', context)
#
#         else:
#             return render(request, 'search/search.html')
#
#     else:
#         return render(request, 'search/search.html')

def about(request):
    return HttpResponse("About us page")
