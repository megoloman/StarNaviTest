import random
import requests

from StarNaviTest.celery_app import app as celery
from StarNaviTest.bot_config import NUMBER_OF_USERS, MAX_POSTS_PER_USER, MAX_LIKES_PER_USER
from apps.user.models import User


@celery.task(default_retry_delay=30 * 60, retry_kwargs={'max_retries': 5})
def post_bot():
    users = []
    posts = []

    # signup users
    for user in range(NUMBER_OF_USERS):
        user = User.objects.create(
            username='test_user_{}'.format(user),
            email='test_user_{}@ukr.net'.format(user),
            password='password'
        )
        users.append(user)

    # each user creates random number of posts
    for user in users:
        response = requests.post(
            'http://127.0.0.1:8000/auth/login/',
            json={'username': user.username, 'password': 'password'}
        )
        jwt_token = response.json().get('key')

        for post in range(random.randint(1, MAX_POSTS_PER_USER)):
            response = requests.post(
                'http://127.0.0.1:8000/post/',
                json={'text': 'post text', },
                headers={'Authorization': 'Token {}'.format(jwt_token)}
            )
            posts.append(response.json().get('id'))

    # posts should be liked randomly
    for post_id in random.sample(posts, 4):
        user = random.choice(users)
        response = requests.post(
            'http://127.0.0.1:8000/auth/login/',
            json={'username': user.username, 'password': 'password'}
        )
        jwt_token = response.json().get('key')

        for like in range(random.randint(1, MAX_LIKES_PER_USER)):
            requests.post(
                'http://127.0.0.1:8000/post-detail/{}/'.format(post_id),
                json={'like': True, },
                headers={'Authorization': 'Token {}'.format(jwt_token)}
            )
