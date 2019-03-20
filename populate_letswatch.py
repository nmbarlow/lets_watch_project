import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
 'lets_watch_project.settings') # Must do this first

# Must do this way else will get an exception as infrastructure not been initialised yet
import django
django.setup() # Import Django project's settings
from letswatch.models import Genre, Movie, Review

def populate():
    # First, we will create lists of dictionaries containing the movies
    # we want to add into each genre.
    # Then we will create a dictionary of dictionaries for our movies.
    # This might seem a little bit confusing, but it allows us to iterate
    # through each data structure, and add the data to our models.

    comedy_movies = [
        {"title" : "The Wolf of Wall Street",
         "url" : "https://www.youtube.com/watch?v=iszwuX1AK6A",
         "year" : "2013",
         "description" : ""},
        {"title" : "Bridesmaids",
         "url" : "https://www.youtube.com/watch?v=FNppLrmdyug",
         "year" : "2011",
         "description" : ""},
        {"title" : "Mean Girls",
         "url" : "https://www.youtube.com/watch?v=KAOmTMCtGkI",
         "year" : "2004",
         "description" : ""},
        {"title" : "Super Bad",
         "url" : "https://www.youtube.com/watch?v=4eaZ_48ZYog",
         "year" : "2007",
         "description" : ""}
    ]

    horror_movies =[
        {"title" : "Get Out",
         "url" : "https://www.youtube.com/watch?v=DzfpyUB60YY",
         "year" : "2017",
         "description" : ""},
        {"title" : "IT",
         "url" : "https://www.youtube.com/watch?v=FnCdOQsX5kc",
         "year" : "2017",
         "description" : ""}

    ]
    action_movies =[
        {"title" : "Wonder Woman",
         "url" : "https://www.youtube.com/watch?v=1Q8fG0TtVAY",
         "year" : "2017",
         "description" : ""},
        {"title" : "Mad Max: Fury Road",
         "url" : "https://www.youtube.com/watch?v=hEJnMQG9ev8",
         "year" : "2015",
         "description" : ""}

    ]
    romance_movies =[
        {"title" : "The Notebook",
         "url" : "https://www.youtube.com/watch?v=FC6biTjEyZw",
         "year" : "2004",
         "description" : ""},
        {"title" : "A Star is Born",
         "url" : "https://www.youtube.com/watch?v=nSbzyEJ8X9E",
         "year" : "2018",
         "description" : ""},
        {"title" : "Love Actually",
         "url" : "https://www.youtube.com/watch?v=fOS-HMiVejo",
         "year" : "2003",
         "description" : ""}

    ]
    family_movies =[
        {"title" : "Mary Poppins",
         "url" : "https://www.youtube.com/watch?v=nOfH7uEojKk",
         "year" : "1964",
         "description" : ""},
        {"title" : "Mary Poppins Returns",
         "url" : "https://www.youtube.com/watch?v=gZgUW88D15w",
         "year" : "2018",
         "description" : ""},
        {"title" : "Mrs Doubtfire",
         "url" : "https://www.youtube.com/watch?v=i8bONcsjaVo",
         "year" : "1993",
         "description" : ""}


    ]
    western_movies =[
        {"title" : "Django Unchained",
         "url" : "https://www.youtube.com/watch?v=_iH0UBYDI4g",
         "year" : "2012",
         "description" : ""},
        {"title" : "The Magnificent Seven (2016)",
         "url" : "https://www.youtube.com/watch?v=q-RBA0xoaWU",
         "year" : "2016",
         "description" : ""},
        {"title" : "The Magnificent Seven (1960)",
         "url" : "https://www.youtube.com/watch?v=bG-ZxrG7htU",
         "year" : "1960",
         "description" : ""}

    ]

    scifi_movies =[
        {"title" : "Interstellar",
         "url" : "https://www.youtube.com/watch?v=zSWdZVtXT7E",
         "year" : "2014",
         "description" : ""},
        {"title" : "Star Wars: The Force Awakens",
         "url" : "https://www.youtube.com/watch?v=sGbxmsDFVnE",
         "year" : "2015",
         "description" : ""}

    ]
    animation_movies =[
        {"title" : "Shrek 2",
         "url" : "https://www.youtube.com/watch?v=V6X5ti4YlG8",
         "year" : "2004",
         "description" : "Shrek has rescued Princess Fiona, got married, and now is time to meet the parents. Shrek, Fiona, and Donkey set off to Far, Far Away to meet Fiona's mother and father. But not everyone is happy. Shrek and the King find it hard to get along, and there's tension in the marriage."},
        {"title" : "Incredibles 2",
         "url" : "https://www.youtube.com/watch?v=i5qOzqD9Rms",
         "year" : "2018",
         "description" : ""},
        {"title" : "Frozen",
         "url" : "https://www.youtube.com/watch?v=TbQm5doF_Uc",
         "year" : "2013",
         "description" : ""}

    ]

    gens = {"comedy" : {"movies" : comedy_movies,},
            "horror" : {"movies" : horror_movies,},
            "action" : {"movies" : action_movies,},
            "romance" : {"movies" : romance_movies,},
            "family" : {"movies" : family_movies,},
            "western" : {"movies" : western_movies,},
            "scifi" : {"movies" : scifi_movies,},
            "animation" : {"movies" : animation_movies,},}

    for gen, gen_data in gens.items():
        g = add_gen(gen) # Do genre first as movie needs genre reference
        for m in gen_data["movies"]:
            add_movie(g, m["title"], m["url"], m["year"], m["description"])

    for g in Genre.objects.all():
        for m in Movie.objects.filter(genre=g):
            print( "- {0} - {1}". format(str(g), str(m)))

def add_movie(genre, title, url, year, description):
    m = Movie.objects.get_or_create(genre=genre, title=title, year=year)[0]
    m.url=url
    m.year=year
    m.description=description
    m.save()
    return m

def add_gen(name,):
    g = Genre.objects.get_or_create(name=name)[0]
    g.save()
    return g

def add_review(movie):
    r = Review.objects.create(
                user=user,
                movie=movie,
                date=data['date'],
                rating=data['rating'],
                content=data['content'],)
    r.save()
    return r

# Execution will start here as the others are 'methods' and therefore will not run
# unless they are called specifically.
# This will only be executed when the module is run as a standalone python script.
if __name__ == '__main__':
    print("Starting Let's Watch! population script...")
    populate()
