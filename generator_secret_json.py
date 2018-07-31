import os

if not os.path.isfile('secret.json'):
    import json
    from django.core.management.utils import get_random_secret_key

    secret = {}
    secret['SECRET_KEY'] = get_random_secret_key()
    secret['DB_HOST'] = ''
    secret['DB_USER'] = ''
    secret['DB_DATABASE'] = ''
    secret['DB_PASSWORD'] = ''

    secret = json.dumps(secret)

    f = open('secret.json', 'w')
    f.write(secret)
    f.close()
