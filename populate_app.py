import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','UserActivity.settings')

import django
django.setup()


import os
import hashlib
import random
from activity_app.models import User,ActivityPeriod
from faker import Faker

fakegen = Faker()
topics = ['Asia/Kabul','Europe/Tirane','Africa/Algiers','Europe/Andorra','Africa/Luanda','America/Anguilla','Antarctica/Davis']

def user_d():
    # create User entry
    fake_name = fakegen.name()
    time_zone = random.choice(topics)
    random_data = os.urandom(128)
    hashl = hashlib.md5(random_data).hexdigest()[:9]
    t_id = hashl.upper()
    usr = User.objects.get_or_create(c_id=t_id, real_name=fake_name, tz=time_zone)[0]
    usr.save()
    return t_id

def populate(N = 5):

    for entry in range(N):

        top = user_d()

        fake_start = fakegen.date_time()
        fake_end = fakegen.date_time()


        #create activityPeriod entry
        actvp = ActivityPeriod.objects.get_or_create(c_id=top,start_time=fake_start,end_time=fake_end)[0]


if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populating complete")