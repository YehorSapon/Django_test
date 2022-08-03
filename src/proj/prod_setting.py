import secrets

length = 50
chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'

SECRET_KEY = ''.join(secrets.choice(chars) for i in range(length))
