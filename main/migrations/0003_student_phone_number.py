# Generated by Django 4.2.13 on 2024-05-31 09:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_news_student_box_student_dances_student_fitness_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='phone_number',
            field=models.CharField(default=django.utils.timezone.now, max_length=11),
            preserve_default=False,
        ),
    ]
