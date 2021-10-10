import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","proxyModelProject.settings")

import django

django.setup()

import random

from faker import Faker

from proxyModelApp.models import Employee


fake=Faker("en-IN")

def populate(n):
    for i in range(n):
        eno=random.randint(0000,9999)
        ename=fake.name()
        esal=random.uniform(0000.0, 9999.9)
        eaddr=fake.address()
        Employee.objects.get_or_create(eno=eno,ename=ename,esal=esal,eaddr=eaddr)

populate(30)
