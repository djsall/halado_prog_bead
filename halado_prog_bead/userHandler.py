from django.contrib.auth.models import User

def register(data):
    if email not in data or \
    username not in data or \
    lastname not in data or \
    firstname not in data or \
    pass1 not in data or \
    pass2 not in data:
        return false

    if data['pass1'] != data['pass2']:
        return False

    User.objects.create_user(data['username'], data['email'], data['pass1'])