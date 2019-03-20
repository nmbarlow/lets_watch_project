from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from letswatch.models import Genre, Movie, Review
from letswatch.forms import GenreForm, MovieForm, UserForm, UserProfileForm, ReviewForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from letswatch.models import UserProfile
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.staticfiles.templatetags.staticfiles import static

from letswatch.models import Hotel
from letswatch.forms import HotelForm

@login_required
def home(request):
    return render(request, 'letswatch/home.html')

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
    return render(request, 'letswatch/gallery.html', context_dict)


def show_movie(request, movie_title_slug):
    #Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a genre name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        movie = Movie.objects.get(slug=movie_title_slug)

        # Retrieve all of the associated movies.
        # Note that filter() will return a list of movie objects or an empty list

        #Adds our results list to the template context under name movies.
        context_dict['movie'] = movie
        # We also add the genre object from
        # the database to the context dictionary.
        # We'll use this in the template to verify that the genre exists.

    except Movie.DoesNotExist:
        # We get here if we didn't find the specified genre.
        # Don't do anything -
        # the template will display the "no genre" message for us.

        context_dict['movie'] = None

    # Go render the response and return it to the client.
    return render(request, 'letswatch/show_movie.html', context_dict)


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

    #form = MovieForm(data=request.POST)
    if request.method == 'POST':
        form = MovieForm(request.POST,request.FILES)
        if form.is_valid():
            if genre:
                movie = form.save(commit=False)
                movie.genre = genre
                movie.views = 0
                
                if 'picture' in request.FILES:
                    movie.picture=request.FILES['picture']
                if 'thumb' in request.FILES:
                    movie.thumb=request.FILES['thumb']
                movie.save()
                return show_genre(request, genre_name_slug)
        else:
            print(form.errors)
    else:
        form=MovieForm()
    context_dict = {'form':form, 'genre':genre}
    return render(request, 'letswatch/add_movie.html', context_dict)

def register(request):
	registered=False
	if request.method == 'POST':
		user_form = UserForm(request.POST,request.FILES)
		profile_form = UserProfileForm(request.POST,request.FILES)

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

# def profile(request, username):
#     try:
#         user = User.objects.get(username=username)
#     except User.DoesNotExist:
#         return redirect('home')

#     userprofile = UserProfile.objects.get_or_create(user=user)[0]

#     profile_form = UserProfileForm({'picture': userprofile.picture})


#     if request.method == 'POST':
#         profile_form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
#         if profile_form.is_valid():
#             profile_form.save(commit=True)
#             return redirect('profile', user.username)
#         else:
#             print(profile_form.errors)

#     return render(request, 'letswatch/userprofile.html',
#                   {'userprofile': userprofile, 'user': user, 'form': profile_form})
#the one i created
# def profile(request, username):
#     try:
#         user = User.objects.get(username=username)
#     except User.DoesNotExist:
#         return redirect('home')

#     userprofile = UserProfile.objects.get_or_create(user=user)[0]

#     form=UserProfileForm()
#     if request.method == 'POST':
#         form=UserProfileForm(request.POST,request.FILES,instance=user)
#         if form.is_valid():
#             if user:
#                 userform=form.save(commit=False)
#                 userform.user=user
#                 picture=request.FILES['picture']
#                 userform.picture=picture
#                 userform.save()
#                 # form.save()
#                 return redirect('profile', user.username)
#                 #return profile(request, user.username)
#         else:
#             print(form.errors)

#     context_dict={'form':form,'user':user,'userprofile':userprofile}
#     return render(request, 'letswatch/userprofile.html', context_dict)

@login_required
def add_review(request, movie_name_slug):
    movie = Movie.objects.get(slug=movie_name_slug)
    reviewer = request.user.userprofile

    if request.method == 'POST':
        form = ReviewForm(data=request.POST)
        response_data = {}

        if form.is_valid():
            if movie and reviewer:
                review, created = Review.objects.get_or_create(user=author, movie=movie)
                review.movie = movie
                review.user = reviewer
                review.content = form.cleaned_data.get('content')
                review.rating = form.cleaned_data.get('rating')
                review.date = form.cleaned_data.get('date')

                review.save()
                response_data['result'] = 'Review successful'
                return HttpResponse(
                    json.dumps(response_data),
                    content_type="application/json"
                )
            else:
                print(form.errors)
        else:
            pass


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


@login_required
def my_reviews(request, username):
    reviewer = User.objects.filter(username=username).first()
    reviews = reviewer.userprofile.reviews.all()

    context = {
        "reviews": reviews,
        "reviewer": reviewer
    }

    return render(request, 'letswatch/my_reviews.html', context)

# Create your views here.
def hotel_image_view(request):

    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = HotelForm()
    return render(request, 'letswatch/list.html', {'form' : form})


def success(request):
    return HttpResponse('successfuly uploaded')



def search(request):
    if request.method == 'GET':
        query = request.GET.get('q')

        submitbutton = request.GET.get('submit')

        if query is not None:
            lookups = Q(title__icontains=query)

            results = Movie.objects.filter(lookups).distinct()

            context ={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'letswatch/search.html', context)

        else:
            return render(request, 'letswatch/search.html')

    else:
        return render(request, 'letswatch/search.html')

@login_required
def register_profile(request):
    form=UserProfileForm()
    if request.method=='POST':
        form=UserProfileForm(request.POST,request.FILES)
        if form.is_valid():
            user_profile=form.save(commit=False)
            user_profile.user=request.user
            user_profile.save()

            return redirect('index')
        else:
            print(form.errors)
    context_dict={'form':form}
    return render(request,'letswatch/profile_registeration.html',context_dict)
    
@login_required
def profile(request, username): 
    try:
        user = User.objects.get(username=username) 
    except User.DoesNotExist:
        return redirect('index')
    userprofile = UserProfile.objects.get_or_create(user=user)[0]
    form = UserProfileForm({'picture': userprofile.picture})
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=userprofile) 
        if form.is_valid():
            form.save(commit=True)
            return redirect('profile', user.username) 
        else:
            print(form.errors)
    return render(request, 'letswatch/profile_registeration.html',{'userprofile': userprofile, 'selecteduser': user, 'form': form}) 

