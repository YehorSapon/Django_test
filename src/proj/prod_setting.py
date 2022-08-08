import secrets

SERVER = 'prod'
length = 50
chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'

SECRET_KEY = ''.join(secrets.choice(chars) for i in range(length))
ALLOWED_HOSTS = ['egorsapon.pythonanywhere.com']
DEBUG = False
