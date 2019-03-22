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
    "url" : "https://www.youtube.com/embed/iszwuX1AK6A",
    "year" : "2013",
    "picture" : "movies/the_wolf_of_wall_street.jpg",
    "thumb" : "movies/the_wolf_of_wall_street.jpg",
    "description" : "Jordan Belfort is a Long Island penny stockbroker who served 22 months in prison for defrauding investors in a massive 1990s securities scam that involved widespread corruption on Wall Street and in the corporate banking world, including shoe designer Steve Madden."},
    {"title" : "Bridesmaids",
    "url" : "https://www.youtube.com/embed/FNppLrmdyug",
    "year" : "2011",
    "picture" : "movies/bridesmaids.jpg",
    "thumb" : "movies/bridesmaids.jpg",
    "description" : "Annie (Kristen Wiig), is a maid of honor whose life unravels as she leads her best friend, Lillian (Maya Rudolph), and a group of colorful bridesmaids (Rose Byrne, Melissa McCarthy, Wendi McLendon-Covey and Ellie Kemper) on a wild ride down the road to matrimony."},
    {"title" : "Mean Girls",
    "url" : "https://www.youtube.com/embed/KAOmTMCtGkI",
    "year" : "2004",
    "picture" : "movies/meangirls.jpg",
    "thumb" : "movies/meangirls.jpg",
    "description" : "Cady is unprepared for her first day of public high school. With the help of Janis (Lizzy Caplan) and Damien (Daniel Franzese), Cady learns about the various cliques. She is warned to avoid the school's most exclusive clique, the Plastics, the reigning trio of girls led by the queen bee Regina George (Rachel McAdams)."},
    {"title" : "Superbad",
    "url" : "https://www.youtube.com/embed/4eaZ_48ZYog",
    "year" : "2007",
    "picture" : "movies/superbad.jpg",
    "thumb" : "movies/superbad.jpg",
    "description" : "Secure in their friendship, Seth and Evan are finally comfortable being apart. Summary: Two high school best friends forever (Jonah Hill, Michael Cera) go on a mission to provide alcohol for a graduation party in hopes of losing their virginity."}
    ]

    horror_movies =[
    {"title" : "Get Out",
    "url" : "https://www.youtube.com/embed/DzfpyUB60YY",
    "year" : "2017",
    "picture" : "movies/get_out.jpg",
    "thumb" : "movies/get_out.jpg",
    "description" : "A young African-American visits his white girlfriend's parents for the weekend, where his simmering uneasiness about their reception of him eventually reaches a boiling point."},
    {"title" : "IT",
    "url" : "https://www.youtube.com/embed/FnCdOQsX5kc",
    "year" : "2017",
    "picture" : "movies/it_(2017).jpg",
    "thumb" : "movies/it_(2017).jpg",
    "description" : "In October 1988, Bill Denbrough gives his six-year-old brother, Georgie, a paper sailboat. ... As he attempts to retrieve it, Georgie sees a clown in the sewer, who introduces himself as Pennywise. ... The synopsis below may give away important plot points."},
    {"title" : "The Nun",
    "url" : "https://www.youtube.com/embed/zwAM5UnGd2s",
    "year" : "2018",
    "picture" : "movies/the_nun.jpg",
    "thumb" : "movies/the_nun.jpg",
    "description" : "When a young nun at a cloistered abbey in Romania takes her own life, a priest with a haunted past and a novitiate on the threshold of her final vows are sent by the Vatican to investigate. Together, they uncover the order's unholy secret. Risking not only their lives but their faith and their very souls, they confront a malevolent force in the form of a demonic nun."},
    {"title" : "The Conjuring",
    "url" : "https://www.youtube.com/embed/k10ETZ41q5o",
    "year" : "2013",
    "picture" : "movies/the_conjuring.jpg",
    "thumb" : "movies/the_conjuring.jpg",
    "description" : "In 1970, paranormal investigators and demonologists Lorraine (Vera Farmiga) and Ed (Patrick Wilson) Warren are summoned to the home of Carolyn (Lili Taylor) and Roger (Ron Livingston) Perron. The Perrons and their five daughters have recently moved into a secluded farmhouse, where a supernatural presence has made itself known. Though the manifestations are relatively benign at first, events soon escalate in horrifying fashion, especially after the Warrens discover the house's macabre history."}
    ]
    action_movies =[
    {"title" : "Wonder Woman",
    "url" : "https://www.youtube.com/embed/1Q8fG0TtVAY",
    "year" : "2017",
    "picture" : "movies/wonder_woman.jpg",
    "thumb" : "movies/wonder_woman.jpg",
    "description" : "Diana, princess of the Amazons, trained to be an unconquerable warrior. Raised on a sheltered island paradise, when a pilot crashes on their shores and tells of a massive conflict raging in the outside world, Diana leaves her home, convinced she can stop the threat. Fighting alongside man in a war to end all wars, Diana will discover her full powers and her true destiny."},
    {"title" : "Mad Max: Fury Road",
    "url" : "https://www.youtube.com/embed/hEJnMQG9ev8",
    "year" : "2015",
    "picture" : "movies/mad_max_fury_road.jpg",
    "thumb" : "movies/mad_max_fury_road.jpg",
    "description" : "Years after the collapse of civilization, the tyrannical Immortan Joe enslaves apocalypse survivors inside the desert fortress the Citadel. When the warrior Imperator Furiosa (Charlize Theron) leads the despot's five wives in a daring escape, she forges an alliance with Max Rockatansky (Tom Hardy), a loner and former captive. Fortified in the massive, armored truck the War Rig, they try to outrun the ruthless warlord and his henchmen in a deadly high-speed chase through the Wasteland."},
    {"title" : "John Wick",
    "url" : "https://www.youtube.com/embed/2AUmvWm5ZDQ",
    "year" : "2014",
    "picture" : "movies/john_wick.jpg",
    "thumb" : "movies/john_wick.jpg",
    "description" : "Legendary assassin John Wick (Keanu Reeves) retired from his violent career after marrying the love of his life. Her sudden death leaves John in deep mourning. When sadistic mobster Iosef Tarasov (Alfie Allen) and his thugs steal John's prized car and kill the puppy that was a last gift from his wife, John unleashes the remorseless killing machine within and seeks vengeance. Meanwhile, Iosef's father (Michael Nyqvist) -- John's former colleague -- puts a huge bounty on John's head."},
    {"title" : "Taken",
    "url" : "https://www.youtube.com/embed/uPJVJBm9TPA",
    "year" : "2008",
    "picture" : "movies/taken.jpg",
    "thumb" : "movies/taken.jpg",
    "description" : "Bryan Mills (Liam Neeson), a former government operative, is trying to reconnect with his daughter, Kim (Maggie Grace). Then his worst fears become real when sex slavers abduct Kim and her friend shortly after they arrive in Paris for vacation. With just four days until Kim will be auctioned off, Bryan must call on every skill he learned in black ops to rescue her."}

    ]
    romance_movies =[
    {"title" : "The Notebook",
    "url" : "https://www.youtube.com/embed/FC6biTjEyZw",
    "year" : "2004",
    "picture" : "movies/the_notebook.jpg",
    "thumb" : "movies/the_notebook.jpg",
    "description" : "A poor yet passionate young man falls in love with a rich young woman, giving her a sense of freedom, but they are soon separated because of their social differences."},
    {"title" : "A Star is Born (2018)",
    "url" : "https://www.youtube.com/embed/nSbzyEJ8X9E",
    "year" : "2018",
    "picture" : "movies/a_star_is_born_(2018).jpg",
    "thumb" : "movies/a_star_is_born_(2018).jpg",
    "description" : "Seasoned musician Jackson Maine (Bradley Cooper) discovers-and falls in love with-struggling artist Ally (Gaga). She has just about given up on her dream to make it big as a singer - until Jack coaxes her into the spotlight. But even as Ally's career takes off, the personal side of their relationship is breaking down, as Jack fights an ongoing battle with his own internal demons."},
    {"title" : "Love Actually",
    "url" : "https://www.youtube.com/embed/fOS-HMiVejo",
    "year" : "2003",
    "picture" : "movies/love_actually.jpg",
    "thumb" : "movies/love_actually.jpg",
    "description" : "Christmas time in England, and unusual things going on round. Some people are falling in love, then breaking up or some people just desperately lonely and still looking for that someone special. This is a story about 8 people who follow their hearts and show love or anger. If you look carefully around 'Love Actually' is all around you..."},
    {"title" : "Pride and Prejudice (2005)",
    "url" : "https://www.youtube.com/embed/1dYv5u6v55Y",
    "year" : "2005",
    "picture" : "movies/pride_and_prejudice_(2005).jpg",
    "thumb" : "movies/pride_and_prejudice_(2005).jpg",
    "description" : "Pride and Prejudice is a humorous story of love and life among English gentility during the Georgian era. Mr Bennet is an English gentleman living in Hartfordshire with his overbearing wife. The Bennets 5 daughters; the beautiful Jane, the clever Elizabeth, the bookish Mary, the immature Kitty and the wild Lydia."}
    ]


    family_movies =[
    {"title" : "Mary Poppins",
    "url" : "https://www.youtube.com/embed/nOfH7uEojKk",
    "year" : "1964",
    "picture" : "movies/mary_poppins_(1964).jpg",
    "thumb" : "movies/mary_poppins_(1964).jpg",
    "description" : "When Jane and Michael, the children of the wealthy and uptight Banks family, are faced with the prospect of a new nanny, they are pleasantly surprised by the arrival of the magical Mary Poppins. Embarking on a series of fantastical adventures with Mary and her Cockney performer friend, Bert, the siblings try to pass on some of their nanny's sunny attitude to their preoccupied parents."},
    {"title" : "Mary Poppins Returns",
    "url" : "https://www.youtube.com/embed/gZgUW88D15w",
    "year" : "2018",
    "picture" : "movies/mary_poppins_returns.jpg",
    "thumb" : "movies/mary_poppins_returns.jpg",
    "description" : "Decades after her original visit, the magical nanny returns to help the Banks siblings and Michael's children through a difficult time in their lives."},
    {"title" : "Mrs Doubtfire",
    "url" : "https://www.youtube.com/embed/i8bONcsjaVo",
    "year" : "1993",
    "picture" : "movies/mrs_doubtfire.jpg",
    "thumb" : "movies/mrs_doubtfire.jpg",
    "description" : "Troubled that he has little access to his children, divorced Daniel Hillard (Robin Williams) hatches an elaborate plan. With help from his creative brother Frank (Harvey Fierstein), he dresses as an older British woman and convinces his ex-wife, Miranda (Sally Field), to hire him as a nanny. 'Mrs. Doubtfire' wins over the children and helps Daniel become a better parent -- but when both Daniel and his nanny persona must meet different parties at the same restaurant, his secrets may be exposed."},
    {"title" : "Paddington",
    "url" : "https://www.youtube.com/embed/7bZFr2IA0Bo",
    "year" : "2014",
    "picture" : "movies/paddington.jpg",
    "thumb" : "movies/paddington.jpg",
    "description" : "After a deadly earthquake destroys his home in Peruvian rainforest, a young bear (Ben Whishaw) makes his way to England in search of a new home. The bear, dubbed 'Paddington' for the london train station, finds shelter with the family of Henry (Hugh Bonneville) and Mary Brown (Sally Hawkins). Although Paddington's amazement at urban living soon endears him to the Browns, someone else has her eye on him: Taxidermist Millicent Clyde (Nicole Kidman) has designs on the rare bear and his hide."}

    ]
    western_movies =[
    {"title" : "Django Unchained",
    "url" : "https://www.youtube.com/embed/_iH0UBYDI4g",
    "year" : "2012",
    "picture" : "movies/django_unchained.jpg",
    "thumb" : "movies/django_unchained.jpg",
    "description" : "Two years before the Civil War, Django (Jamie Foxx), a slave, finds himself accompanying an unorthodox German bounty hunter named Dr. King Schultz (Christoph Waltz) on a mission to capture the vicious Brittle brothers. Their mission successful, Schultz frees Django, and together they hunt the South's most-wanted criminals. Their travels take them to the infamous plantation of shady Calvin Candie (Leonardo DiCaprio), where Django's long-lost wife (Kerry Washington) is still a slave."},
    {"title" : "The Magnificent Seven (2016)",
    "url" : "https://www.youtube.com/embed/q-RBA0xoaWU",
    "year" : "2016",
    "picture" : "movies/the_magnificent_seven_(2016).jpg",
    "thumb" : "movies/the_magnificent_seven_(2016).jpg",
    "description" : "Looking to mine for gold, greedy industrialist Bartholomew Bogue seizes control of the Old West town of Rose Creek. With their lives in jeopardy, Emma Cullen and other desperate residents turn to bounty hunter Sam Chisolm (Denzel Washington) for help. Chisolm recruits an eclectic group of gunslingers to take on Bogue and his ruthless henchmen. With a deadly showdown on the horizon, the seven mercenaries soon find themselves fighting for more than just money once the bullets start to fly."},
    {"title" : "The Magnificent Seven (1960)",
    "url" : "https://www.youtube.com/embed/bG-ZxrG7htU",
    "year" : "1960",
    "picture" : "movies/the_magnificent_seven_(1960).jpg",
    "thumb" : "movies/the_magnificent_seven_(1960).jpg",
    "description" : "A Mexican village is at the mercy of Calvera, the leader of a band of outlaws. The townspeople, too afraid to fight for themselves, hire seven American gunslingers to free them from the bandits' raids. The professional gunmen train the villagers to defend themselves, then plan a trap for the evil Calvera."},
    {"title" : "Pale Rider",
    "url" : "https://www.youtube.com/embed/SGzz3hh1jHc",
    "year" : "1985",
    "picture" : "movies/pale_rider.jpg",
    "thumb" : "movies/pale_rider.jpg",
    "description" : "When property owner Coy LaHood (Richard Dysart) starts using a band of hooligans to terrorize a group of small-town gold miners into giving up their territory, an enigmatic man named 'Preacher' (Clint Eastwood) arrives in town. Preacher fends off the attacks, and then goes directly to LaHood to negotiate. When the miners, led by Hull Barret (Michael Moriarty), refuse the terms, LaHood sends in Marshall Stockburn (John Russell) to take down Preacher and the others."},

    ]

    scifi_movies =[
    {"title" : "Interstellar",
    "url" : "https://www.youtube.com/embed/zSWdZVtXT7E",
    "year" : "2014",
    "picture" : "movies/interstellar.jpg",
    "thumb" : "movies/interstellar.jpg",
    "description" : "Earth's future has been riddled by disasters, famines, and droughts. There is only one way to ensure mankind's survival: Interstellar travel. A newly discovered wormhole in the far reaches of our solar system allows a team of astronauts to go where no man has gone before, a planet that may have the right environment to sustain human life."},
    {"title" : "Star Wars: The Force Awakens",
    "url" : "https://www.youtube.com/embed/sGbxmsDFVnE",
    "year" : "2015",
    "picture" : "movies/star_wars_the_force_awakens.jpg",
    "thumb" : "movies/star_wars_the_force_awakens.jpg",
    "description" : "Thirty years after the defeat of the Galactic Empire, the galaxy faces a new threat from the evil Kylo Ren (Adam Driver) and the First Order. When a defector named Finn (John Boyega) crash-lands on a desert planet, he meets Rey (Daisy Ridley), a tough scavenger whose droid contains a top-secret map. Together, the young duo joins forces with Han Solo (Harrison Ford) to make sure the Resistance receives the intelligence concerning the whereabouts of Luke Skywalker (Mark Hamill), the last of the Jedi Knights."},
    {"title" : "Avatar",
    "url" : "https://www.youtube.com/embed/5PSNL1qE6VY",
    "year" : "2009",
    "picture" : "movies/avatar.jpg",
    "thumb" : "movies/avatar.jpg",
    "description" : "On the lush alien world of Pandora live the Na'vi, beings who appear primitive but are highly evolved. Because the planet's environment is poisonous, human/Na'vi hybrids, called Avatars, must link to human minds to allow for free movement on Pandora. Jake Sully (Sam Worthington), a paralyzed former Marine, becomes mobile again through one such Avatar and falls in love with a Na'vi woman (Zoe Saldana). As a bond with her grows, he is drawn into a battle for the survival of her world."},
    {"title" : "Ex Machina",
    "url" : "https://www.youtube.com/embed/PI8XBKb6DQk",
    "year" : "2014",
    "picture" : "movies/ex_machina.jpg",
    "thumb" : "movies/ex_machina.jpg",
    "description" : "Caleb Smith (Domhnall Gleeson) a programmer at a huge Internet company, wins a contest that enables him to spend a week at the private estate of Nathan Bateman (Oscar Isaac), his firm's brilliant CEO. When he arrives, Caleb learns that he has been chosen to be the human component in a Turing test to determine the capabilities and consciousness of Ava (Alicia Vikander), a beautiful robot. However, it soon becomes evident that Ava is far more self-aware and deceptive than either man imagined."},

    ]
    animation_movies =[
    {"title" : "Shrek 2",
    "url" : "https://www.youtube.com/embed/V6X5ti4YlG8",
    "year" : "2004",
    "picture" : "movies/shrek_2.jpg",
    "thumb" : "movies/shrek_2.jpg",
    "description" : "Shrek has rescued Princess Fiona, got married, and now is time to meet the parents. Shrek, Fiona, and Donkey set off to Far, Far Away to meet Fiona's mother and father. But not everyone is happy. Shrek and the King find it hard to get along, and there's tension in the marriage."},
    {"title" : "Incredibles 2",
    "url" : "https://www.youtube.com/embed/i5qOzqD9Rms",
    "year" : "2018",
    "picture" : "movies/incredibles_2.jpg",
    "thumb" : "movies/incredibles_2.jpg",
    "description" : "The Incredibles hero family takes on a new mission, which involves a change in family roles: Bob Parr (Mr Incredible) must manage the house while his wife Helen (Elastigirl) goes out to save the world."},
    {"title" : "Frozen",
    "url" : "https://www.youtube.com/embed/TbQm5doF_Uc",
    "year" : "2013",
    "picture" : "movies/frozen.jpg",
    "thumb" : "movies/frozen.jpg",
    "description" : "When the newly-crowned Queen Elsa accidentally uses her power to turn things into ice to curse her home in infinite winter, her sister Anna teams up with a mountain man, his playful reindeer, and a snowman to change the weather condition."},
    {"title" : "Up",
    "url" : "https://www.youtube.com/embed/ORFWdXl_zJ4",
    "year" : "2009",
    "picture" : "movies/up.jpg",
    "thumb" : "movies/up.jpg",
    "description" : "Carl Fredricksen, a 78-year-old balloon salesman, is about to fulfill a lifelong dream. Tying thousands of balloons to his house, he flies away to the South American wilderness. But curmudgeonly Carl's worst nightmare comes true when he discovers a little boy named Russell is a stowaway aboard the balloon-powered house. A Pixar animation."},
    ]


    gens = {"Comedy" : {"movies" : comedy_movies,},
    "Horror" : {"movies" : horror_movies,},
    "Action" : {"movies" : action_movies,},
    "Romance" : {"movies" : romance_movies,},
    "Family" : {"movies" : family_movies,},
    "Western" : {"movies" : western_movies,},
    "Scifi" : {"movies" : scifi_movies,},
    "Animation" : {"movies" : animation_movies,},}

    for gen, gen_data in gens.items():
        g = add_gen(gen) # Do genre first as movie needs genre reference
        for m in gen_data["movies"]:
            add_movie(g, m["title"], m["url"], m["year"], m["thumb"], m["picture"], m["description"])

            for g in Genre.objects.all():
                for m in Movie.objects.filter(genre=g):
                    print( "- {0} - {1}". format(str(g), str(m)))

def add_movie(genre, title, url, year, thumb, picture,description):
    m = Movie.objects.get_or_create(genre=genre, title=title, year=year, url=url, thumb=thumb, description=description)[0]
    m.url=url
    m.year=year
    m.thumb=thumb
    m.picture=picture
    m.description=description
    m.save()
    return m

def add_gen(name,):
    g = Genre.objects.get_or_create(name=name)[0]
    g.save()
    return g

# def add_review(movie):
#     r = Review.objects.create(
#                 user=user,
#                 movie=movie,
#                 date=data['date'],
#                 rating=data['rating'],
#                 content=data['content'],)
#     r.save()
#     return r

# Execution will start here as the others are 'methods' and therefore will not run
# unless they are called specifically.
# This will only be executed when the module is run as a standalone python script.
if __name__ == '__main__':
    print("Starting Let's Watch! population script...")
    populate()
