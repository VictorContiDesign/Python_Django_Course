# Generated by Django 3.1.7 on 2023-03-13 19:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['title'], 'verbose_name': 'Article'},
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='centent',
            new_name='content',
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Auteur'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='created_on',
            field=models.DateField(blank=True, null=True, verbose_name='Création'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Actualisation'),
        ),
    ]
