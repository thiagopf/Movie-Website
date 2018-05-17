import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "Woody (Tom Hanks), a good-hearted cowboy doll who belongs to a young boy named "
                                     "Andy (John Morris), sees his position as Andy's favorite toy jeopardized when "
                                     "his parents buy him a Buzz Lightyear (Tim Allen) action figure. Even worse, "
                                     "the arrogant Buzz thinks he's a real spaceman on a mission to return to his home "
                                     "planet. When Andy's family moves to a new house, Woody and Buzz must escape the "
                                     "clutches of maladjusted neighbor Sid Phillips (Erik von Detten) and reunite with "
                                     "their boy.", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                                     "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "On the lush alien world of Pandora live the Na'vi, beings who appear primitive but "
                               "are highly evolved. Because the planet's environment is poisonous, human/Na'vi "
                               "hybrids, called Avatars, must link to human minds to allow for free movement on "
                               "Pandora. Jake Sully (Sam Worthington), a paralyzed former Marine, becomes mobile "
                               "again through one such Avatar and falls in love with a Na'vi woman (Zoe Saldana). As "
                               "a bond with her grows, he is drawn into a battle for the survival of her world.",
                               "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                               "https://www.youtube.com/watch?v=5PSNL1qE6VY")

interstellar = media.Movie("Interstellar", "In Earth's future, a global crop blight and second Dust Bowl are slowly "
                                           "rendering the planet uninhabitable. Professor Brand (Michael Caine), "
                                           "a brilliant NASA physicist, is working on plans to save mankind by "
                                           "transporting Earth's population to a new home via a wormhole. But first, "
                                           "Brand must send former NASA pilot Cooper (Matthew McConaughey) and a team "
                                           "of researchers through the wormhole and across the galaxy to find out "
                                           "which of three planets could be mankind's new home.",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=zSWdZVtXT7E")
movies = [toy_story, avatar, interstellar]
fresh_tomatoes.open_movies_page(movies)
