from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from letswatch.models import Genre, Movie
from letswatch.forms import GenreForm, MovieForm, UserForm, UserProfileForm
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

def show_genre(request, genre_name_slug):
    #Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a genre name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        genre = Genre.objects.get(slug=genre_name_slug)

        # Retrieve all of the associated movies.
        # Note that filter() will return a list of movie objects or an empty list
        movies = Movie.objects.filter(genre=genre)

        #Adds our results list to the template context under name movies.
        context_dict['movies'] = movies
        # We also add the genre object from
        # the database to the context dictionary.
        # We'll use this in the template to verify that the genre exists.
        context_dict['genre'] = genre
    except Genre.DoesNotExist:
        # We get here if we didn't find the specified genre.
        # Don't do anything -
        # the template will display the "no genre" message for us.
        context_dict['genre'] = None
        context_dict['movies'] = None

    # Go render the response and return it to the client.
    return render(request, 'letswatch/genre.html', context_dict)

@login_required
def add_genre(request):
    form = GenreForm()

    # A HTTP POST?
    if request.method == 'POST':
        form = GenreForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new genre to the database.
            form.save(commit=True)
            # Now that the genre is saved
            # We could give a confirmation message
            # But since the most recent genre addded is on the index page
            # Then we can direct the user back to the index page.
            return index(request)
        else:
            # The supplied form contained errors -
            # just print them to the terminal.
            print(form.errors)

    # Will handle the bad form, new form, or no form supplied cases.
    # Render the form with error messages (if any).
    return render(request, 'letswatch/add_genre.html', {'form': form})

@login_required
def add_movie(request, genre_name_slug):
    try:
        genre = Genre.objects.get(slug=genre_name_slug)
    except Genre.DoesNotExist:
        genre = None

    form = MovieForm()
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            if genre:
                movie = form.save(commit=False)
                movie.genre = genre
                movie.views = 0
                movie.save()
                return show_genre(request, genre_name_slug)
        else:
            print(form.errors)
    context_dict = {'form':form, 'genre':genre}
    return render(request, 'letswatch/add_movie.html', context_dict)

def register(request):
	registered=False
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
			user = user_login(request)
			return HttpResponseRedirect(reverse('index'))
		else:
			print(user_form.errors, profile_form.errors)
	else:
		user_form = UserForm()
		profile_form=UserProfileForm()

	return render(request,'letswatch/register.html', {'user_form': user_form,
'profile_form': profile_form,
'registered': registered})

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
				return HttpResponse("Your letswatch account is disabled.")
		else:
			print("Invalid login details: {0}, {1}".format(username, password))
			return HttpResponse("Invalid login details supplied.")
	else:
		return render(request, 'letswatch/login.html', {})

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))


def page_not_found(request):
	data = {}
	return render(request, 'letswatch/404.html', data)

def server_error(request):
	data = {}
	return render(request, 'letswatch/500.html', data)

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
def movie_rate(request):

    context_dict = {}
    rate = Rate.objects.filter()

    context_dict['rate'] = rate

    return render(request, 'letswatch/rate_movie.html', context_dict)

@login_required
def rate_movie(request):

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

def search(request):
    return HttpResponse("Search page")

def about(request):
    return HttpResponse("About us page")
