import media
import fresh_tomatoes

'''Here you can create new movie objects
with help of the media.Movie Class'''

if __name__ == "__main__":
    print("Thanks for using this program")

# Movie creation with media.py as template

toy_story = media.Movies(
                        "Toy Story",
                        "81 min",
                        "A Story of a boy and his toys that come to life",
                        "https://images-na.ssl-images-amazon.com/images/I/81zWx2fQ5vL._SY550_.jpg",  #NOQA
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movies(
                        "Avatar",
                        "162 min",
                        "A marine on AlienPlanat",
                        "http://t1.gstatic.com/images?q=tbn:ANd9GcSTpa51SkJFKdByZ27eU4z0IqcP5mhbHkEHWN26lDpss4rhMk5W",  #NOQA
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")

die_hard_two = media.Movies(
                            "Die Hard II",
                            "125 min",
                            "John McLane saving the day once again",
                            "https://upload.wikimedia.org/wikipedia/en/2/2c/Die_Hard_2.jpg",  #NOQA
                            "https://www.youtube.com/watch?v=gUg4gWjOgXs")

kingsman = media.Movies(
                        "Kingsman - Secret Service",
                        "129 min",
                        "Secret Agency in the UK build out of the wealth of a "
                        "tailor dynasty",
                        "http://t0.gstatic.com/images?q=tbn:ANd9GcTQ3kwZJAWdN9AVklIzO1JxcdCley8CmApSrtMw4uJrAySuMOMk",  #NOQA
                        "https://www.youtube.com/watch?v=xkX8jKeKUEA")

hitmans_bodyguard = media.Movies(
                                "Hitman\'s Bodyguard",
                                "118 min",
                                "Bodyguard have to protect his enemie",
                                "https://assets.cdn.moviepilot.de/files/5150061998ba3e4e30b121d6735dc941d927ca40ead8cc8fdcc52edd7f09/RZ_KillersBodyguard_PosterLaunch_3Cast_Druck_A4.jpg",  #NOQA
                                "https://www.youtube.com/watch?v=l_5bGJogDNM")

#Array for all the movies to display on the website
movies = [toy_story, avatar, die_hard_two, kingsman, hitmans_bodyguard]

#command to run the site
fresh_tomatoes.open_movies_page(movies)
