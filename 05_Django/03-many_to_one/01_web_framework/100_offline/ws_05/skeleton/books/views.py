from rest_framework.decorators import api_view
from django.http import JsonResponse
import random

books = [
    {
        "pk": 1,
        "title": "Python Programming for Beginners",
        "description": "An introductory guide to Python programming.",
        "published_date": "2020-05-15",
        "rating": 8.2
    },
    {
        "pk": 2,
        "title": "Advanced Python Techniques",
        "description": "Explore advanced features and techniques in Python.",
        "published_date": "2021-08-22",
        "rating": 9.0
    },
    {
        "pk": 3,
        "title": "Data Science with Python",
        "description": "Learn data science concepts and tools using Python.",
        "published_date": "2019-11-30",
        "rating": 5.5
    },
    {
        "pk": 4,
        "title": "Machine Learning with Python",
        "description": "A comprehensive guide to machine learning with Python.",
        "published_date": "2018-07-10",
        "rating": 7.2
    },
    {
        "pk": 5,
        "title": "Web Development with Django",
        "description": "Build powerful web applications using Django and Python.",
        "published_date": "2022-01-15",
        "rating": 8.1
    },
    {
        "pk": 6,
        "title": "Python for Data Analysis",
        "description": "Techniques and tools for data analysis with Python.",
        "published_date": "2017-03-20",
        "rating": 6.6
    },
    {
        "pk": 7,
        "title": "Automate the Boring Stuff with Python",
        "description": "Automate common tasks and improve productivity with Python.",
        "published_date": "2015-04-14",
        "rating": 9.4
    },
    {
        "pk": 8,
        "title": "Fluent Python",
        "description": "Write efficient, high-quality Python code.",
        "published_date": "2019-09-05",
        "rating": 5.5
    },
    {
        "pk": 9,
        "title": "Effective Python",
        "description": "59 specific ways to improve your Python skills.",
        "published_date": "2017-12-11",
        "rating": 7.7
    },
    {
        "pk": 10,
        "title": "Python Crash Course",
        "description": "A hands-on, project-based introduction to Python.",
        "published_date": "2016-06-17",
        "rating": 6.5
    }
]

# Create your views here.
@api_view(['GET'])
def recommend_books(request):
    high_rated_books = [book for book in books if book['rating'] >= 6.0]
    recommended_books = random.sample(high_rated_books, 1)
    return JsonResponse(recommended_books[0])

@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'POST':  # 새 책을 추가하는 경우
        data = request.POST
        book = {
            "pk": auto_increment_pk(),
            "title": data['title'],
            "description": data['description'],
            "published_date": data['published_date'],
            "rating": data.get('rating', 0)  # rating이 없는 경우 기본값 0
        }
        books.append(book)
        return JsonResponse(book, status=201)
    page = int(request.GET.get('page', 1)) # 페이지 번호를 가져옴 (기본값: 1)
    data = books[(page - 1) * 5:page * 5]  # 한 페이지에 5개의 책만 표시

    return JsonResponse(data, safe=False)


def auto_increment_pk():
    return max([book['pk'] for book in books]) + 1
