def get_rating(movie):

    return movie[1]


def sort_movies_by_rating(movies):

    return sorted(movies, key=get_rating)


movies = [("Toy Story 4", 8.2),("Captain Marvel", 7.0),("Avengers: Endgame", 8.7),("Aladdin", 7.4), ]

sorted_movies = sort_movies_by_rating(movies)
print(sorted_movies)