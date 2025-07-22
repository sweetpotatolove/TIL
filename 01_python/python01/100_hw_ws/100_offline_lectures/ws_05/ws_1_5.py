movies = ['Inception', 'Interstellar', 'Dunkirk', 'Tenet']
ratings = [9, 8.5, 7.5, 6]

# movies리스트를 순회하며 영화 제목과 평점을 가진 딕셔너리 객체로 만들고 새로운 리스트에 담는다.
new_movies_list = []
for title, rating in zip(movies, ratings):
    temp_dict = {'title': title, 'rating': rating}
    new_movies_list.append(temp_dict)
print(new_movies_list)

com_movies = [{'title': title, 'rating': rating} for title, rating in zip(movies, ratings) ]

def get_high_rated_movies(threshold):
    high_rated_movies = []
    for i in range(len(movies)):
        if ratings[i] >= threshold:
            high_rated_movies.append(movies[i])
    return high_rated_movies

threshold = float(input('Enter the rating threshold : '))
high_rated_movies = get_high_rated_movies(threshold)
print(f'Movies with a rating of {threshold} or higher')
for movie in high_rated_movies:
    print(movie)