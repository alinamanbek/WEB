# Generated by Django 4.1.5 on 2023-04-12 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0032_alter_profile_created_courses_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='created_courses',
            field=models.ManyToManyField(blank=True, related_name='my_created', to='course.course'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='taken_courses',
            field=models.ManyToManyField(blank=True, related_name='taken_by_me', to='course.course'),
        ),
    ]