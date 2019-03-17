import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
 'lets_watch_project.settings') # Must do this first

# Must do this way else will get an exception as infrastructure not been initialised yet
import django
django.setup() # Import Django project's settings
from letswatch.models import Genre, Movie

def populate():
    # First, we will create lists of dictionaries containing the movies
    # we want to add into each genre.
    # Then we will create a dictionary of dictionaries for our movies.
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure, and add the data to our models.

    comedy_movies = [
        {"title" : "The Wolf of Wall Street",
         "url" : "https://www.youtube.com/watch?v=iszwuX1AK6A"},
    ]

    horror_movies =[
        {"title" : "Get Out",
         "url" : "https://www.youtube.com/watch?v=DzfpyUB60YY"}

    ]

    gens = {"comedy" : {"movies" : comedy_movies,},
            "horror" : {"movies" : horror_movies,}}

    for gen, gen_data in gens.items():
        g = add_gen(gen) # Do genre first as movie needs genre reference
        for m in gen_data["movies"]:
            add_movie(g, m["title"], m["url"],)

    for g in Genre.objects.all():
        for m in Movie.objects.filter(genre=g):
            print( "- {0} - {1}". format(str(g), str(m)))

def add_movie(gen, title, url,):
    m = Movie.objects.get_or_create(genre=gen, title=title)[0]
    m.url=url
    m.save()
    return m

def add_gen(name,):
    g = Genre.objects.get_or_create(name=name)[0]
    g.save()
    return g

# Execution will start here as the others are 'methods' and therefore will not run
# unless they are called specifically.
# This will only be executed when the module is run as a standalone python script.
if __name__ == '__main__':
    print("Starting Let's Watch! population script...")
    populate()
