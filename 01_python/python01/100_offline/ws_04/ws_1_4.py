movies = ['Inception', 'Interstellar', 'Dunkirk', 'Tenet']

def get_movie_recommendation(rating):
    if rating >= 9:
        return 'Inception'
    elif rating >= 8:
        return 'Interstellar'
    elif rating >= 7:
        return 'Dunkirk'
    else:
        return 'Tenet'

user_rating = float(input("Enter your movie rating (0-10): "))
recommended_movie = get_movie_recommendation(user_rating)
print("Recommended movie:", recommended_movie)