import random

students_list = ['이선영', '최준형', '김은주', '김은수', '김승수', '유동훈']

def choice(array):
    return random.choice(array)

def add(item):
    students_list.append(item)