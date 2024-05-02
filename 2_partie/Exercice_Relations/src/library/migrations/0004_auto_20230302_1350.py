# Generated by Django 3.1.6 on 2023-03-02 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20230302_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='book',
            name='category',
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(to='library.Category'),
        ),
    ]
