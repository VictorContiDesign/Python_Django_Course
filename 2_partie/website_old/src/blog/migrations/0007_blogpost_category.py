# Generated by Django 3.1.6 on 2023-03-02 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blogpost_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='Category',
            field=models.ManyToManyField(to='blog.Category'),
        ),
    ]
