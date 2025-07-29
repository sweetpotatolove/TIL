def filter_adults(users):
    return [user for user in users if user['age'] >= 18]

def filter_active_users(users):
    return [user for user in users if user['is_active']]

def filter_adult_active_users(users):
    return [user for user in users if user['age'] >= 18 and user['is_active']]
