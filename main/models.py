from django.db import models
from django.urls import reverse


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
    surname = models.CharField(max_length=255, verbose_name="Фамилия")
    name = models.CharField(max_length=255, verbose_name="Имя")
    birthdate = models.DateField(verbose_name="Дата рождения")
    football = models.CharField(max_length=1, blank=True, choices=FOOTBALL_GROUPS, verbose_name="Футбол")
    box = models.CharField(max_length=1, blank=True, choices=GROUPS, verbose_name="Бокс")
    dances = models.CharField(max_length=1, blank=True, choices=GROUPS, verbose_name="Танцы")
    fitness = models.CharField(max_length=1, blank=True, choices=GROUPS_FITNESS, verbose_name="Фитнесс")
    phone_number = models.CharField(max_length=11, verbose_name="Телефонный номер")

    def __str__(self):
        return self.surname

    def get_absolute_url(self):
        return reverse('post', kwargs={'student_id': self.pk})

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'news_id': self.pk})