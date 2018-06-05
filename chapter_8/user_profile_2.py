def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()
    for key, value in user_info.items():
        profile[key] = value.upper()
        return profile

user_profile = build_profile('chris', 'leader', style = 'dark chocolate')
print(user_profile)
