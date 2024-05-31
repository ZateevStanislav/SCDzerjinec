from django.db import models

class Student(models.Model):
    FOOTBALL_GROUPS = [
        ("1", "Oldest"),
        ("2", "Middle"),
        ("3", "Youngest"),
        ("N", "No"),
    ]
    GROUPS = [
        ("1", "Oldest"),
        ("2", "Youngest"),
        ("N", "No"),
    ]
    GROUPS_FITNESS = [
        ("Y", "Yes"),
        ("N", "No"),
    ]
    surname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    birthdate = models.DateField()
    football = models.CharField(max_length=1, blank=True, choices=FOOTBALL_GROUPS)
    box = models.CharField(max_length=1, blank=True, choices=GROUPS)
    dances = models.CharField(max_length=1, blank=True, choices=GROUPS)
    fitness = models.CharField(max_length=1, blank=True, choices=GROUPS_FITNESS)

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)