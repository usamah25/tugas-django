import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

# Populate fake scripts 
import random
from first_app.models import Topic, Webpage, Accessrecord
from faker import Faker

fakegen = Faker()
topics = ['Social', 'Search', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N = 5):

    for entry in range(N):

        # get  the topic for the entry
        top = add_topic()

        # create fake data for the entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.name()

        # create a new webpage entry
        webpg = Webpage.objects.get_or_create(topic = top, url=fake_url, name=fake_name)[0]

        # create a new fake access record
        acc_rec = Accessrecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == '__main__':
    print ("Populating script...")
    populate(20)
    print('Populating Completed')