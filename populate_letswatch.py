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
         "description" : "Jordan Belfort is a Long Island penny stockbroker who served 22 months in prison for defrauding investors in a massive 1990s securities scam that involved widespread corruption on Wall Street and in the corporate banking world, including shoe designer Steve Madden."},
        {"title" : "Bridesmaids",
         "url" : "https://www.youtube.com/watch?v=FNppLrmdyug",
         "year" : "2011",
         "description" : "Annie (Kristen Wiig), is a maid of honor whose life unravels as she leads her best friend, Lillian (Maya Rudolph), and a group of colorful bridesmaids (Rose Byrne, Melissa McCarthy, Wendi McLendon-Covey and Ellie Kemper) on a wild ride down the road to matrimony."},
        {"title" : "Mean Girls",
         "url" : "https://www.youtube.com/watch?v=KAOmTMCtGkI",
         "year" : "2004",
         "description" : "Cady is unprepared for her first day of public high school. With the help of Janis (Lizzy Caplan) and Damien (Daniel Franzese), Cady learns about the various cliques. She is warned to avoid the school's most exclusive clique, the Plastics, the reigning trio of girls led by the queen bee Regina George (Rachel McAdams)."},
        {"title" : "Superbad",
         "url" : "https://www.youtube.com/watch?v=4eaZ_48ZYog",
         "year" : "2007",
         "description" : "Secure in their friendship, Seth and Evan are finally comfortable being apart. Summary: Two high school best friends forever (Jonah Hill, Michael Cera) go on a mission to provide alcohol for a graduation party in hopes of losing their virginity."}
    ]

    horror_movies =[
        {"title" : "Get Out",
         "url" : "https://www.youtube.com/watch?v=DzfpyUB60YY",
         "year" : "2017",
         "description" : "A young African-American visits his white girlfriend's parents for the weekend, where his simmering uneasiness about their reception of him eventually reaches a boiling point."},
        {"title" : "IT",
         "url" : "https://www.youtube.com/watch?v=FnCdOQsX5kc",
         "year" : "2017",
         "description" : "In October 1988, Bill Denbrough gives his six-year-old brother, Georgie, a paper sailboat. ... As he attempts to retrieve it, Georgie sees a clown in the sewer, who introduces himself as Pennywise. ... The synopsis below may give away important plot points."}

    ]
    action_movies =[
        {"title" : "Wonder Woman",
         "url" : "https://www.youtube.com/watch?v=1Q8fG0TtVAY",
         "year" : "2017",
         "description" : "Diana, princess of the Amazons, trained to be an unconquerable warrior. Raised on a sheltered island paradise, when a pilot crashes on their shores and tells of a massive conflict raging in the outside world, Diana leaves her home, convinced she can stop the threat. Fighting alongside man in a war to end all wars, Diana will discover her full powers and her true destiny."},
        {"title" : "Mad Max: Fury Road",
         "url" : "https://www.youtube.com/watch?v=hEJnMQG9ev8",
         "year" : "2015",
         "description" : "Years after the collapse of civilization, the tyrannical Immortan Joe enslaves apocalypse survivors inside the desert fortress the Citadel. When the warrior Imperator Furiosa (Charlize Theron) leads the despot's five wives in a daring escape, she forges an alliance with Max Rockatansky (Tom Hardy), a loner and former captive. Fortified in the massive, armored truck the War Rig, they try to outrun the ruthless warlord and his henchmen in a deadly high-speed chase through the Wasteland."}

    ]
    romance_movies =[
        {"title" : "The Notebook",
         "url" : "https://www.youtube.com/watch?v=FC6biTjEyZw",
         "year" : "2004",
         "description" : "A poor yet passionate young man falls in love with a rich young woman, giving her a sense of freedom, but they are soon separated because of their social differences."},
        {"title" : "A Star is Born (2018)",
         "url" : "https://www.youtube.com/watch?v=nSbzyEJ8X9E",
         "year" : "2018",
         "description" : "Seasoned musician Jackson Maine (Bradley Cooper) discovers-and falls in love with-struggling artist Ally (Gaga). She has just about given up on her dream to make it big as a singer - until Jack coaxes her into the spotlight. But even as Ally's career takes off, the personal side of their relationship is breaking down, as Jack fights an ongoing battle with his own internal demons."},
        {"title" : "Love Actually",
         "url" : "https://www.youtube.com/watch?v=fOS-HMiVejo",
         "year" : "2003",
         "description" : "Christmas time in England, and unusual things going on round. Some people are falling in love, then breaking up or some people just desperately lonely and still looking for that someone special. This is a story about 8 people who follow their hearts and show love or anger. If you look carefully around 'Love Actually' is all around you..."}

    ]
    family_movies =[
        {"title" : "Mary Poppins",
         "url" : "https://www.youtube.com/watch?v=nOfH7uEojKk",
         "year" : "1964",
         "description" : "When Jane and Michael, the children of the wealthy and uptight Banks family, are faced with the prospect of a new nanny, they are pleasantly surprised by the arrival of the magical Mary Poppins. Embarking on a series of fantastical adventures with Mary and her Cockney performer friend, Bert, the siblings try to pass on some of their nanny's sunny attitude to their preoccupied parents."},
        {"title" : "Mary Poppins Returns",
         "url" : "https://www.youtube.com/watch?v=gZgUW88D15w",
         "year" : "2018",
         "description" : "Decades after her original visit, the magical nanny returns to help the Banks siblings and Michael's children through a difficult time in their lives."},
        {"title" : "Mrs Doubtfire",
         "url" : "https://www.youtube.com/watch?v=i8bONcsjaVo",
         "year" : "1993",
         "description" : "Troubled that he has little access to his children, divorced Daniel Hillard (Robin Williams) hatches an elaborate plan. With help from his creative brother Frank (Harvey Fierstein), he dresses as an older British woman and convinces his ex-wife, Miranda (Sally Field), to hire him as a nanny. 'Mrs. Doubtfire' wins over the children and helps Daniel become a better parent -- but when both Daniel and his nanny persona must meet different parties at the same restaurant, his secrets may be exposed."}


    ]
    western_movies =[
        {"title" : "Django Unchained",
         "url" : "https://www.youtube.com/watch?v=_iH0UBYDI4g",
         "year" : "2012",
         "description" : "Two years before the Civil War, Django (Jamie Foxx), a slave, finds himself accompanying an unorthodox German bounty hunter named Dr. King Schultz (Christoph Waltz) on a mission to capture the vicious Brittle brothers. Their mission successful, Schultz frees Django, and together they hunt the South's most-wanted criminals. Their travels take them to the infamous plantation of shady Calvin Candie (Leonardo DiCaprio), where Django's long-lost wife (Kerry Washington) is still a slave."},
        {"title" : "The Magnificent Seven (2016)",
         "url" : "https://www.youtube.com/watch?v=q-RBA0xoaWU",
         "year" : "2016",
         "description" : "Looking to mine for gold, greedy industrialist Bartholomew Bogue seizes control of the Old West town of Rose Creek. With their lives in jeopardy, Emma Cullen and other desperate residents turn to bounty hunter Sam Chisolm (Denzel Washington) for help. Chisolm recruits an eclectic group of gunslingers to take on Bogue and his ruthless henchmen. With a deadly showdown on the horizon, the seven mercenaries soon find themselves fighting for more than just money once the bullets start to fly."},
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
