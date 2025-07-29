from filters import filter_adults, filter_active_users, filter_adult_active_users


users = [
    {"username": "alice", "age": 25, "is_active": True},
    {"username": "bob", "age": 17, "is_active": False},
    {"username": "charlie", "age": 30, "is_active": True},
    {"username": "david", "age": 22, "is_active": False},
    {"username": "eve", "age": 29, "is_active": True}
]



adults = filter_adults(users)
active_users = filter_active_users(users)
adult_active_users = filter_adult_active_users(users)
print("Adults:", adults)
print("Active Users:", active_users)
print("Adult Active Users:", adult_active_users)