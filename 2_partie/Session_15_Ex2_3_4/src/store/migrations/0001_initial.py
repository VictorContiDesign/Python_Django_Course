# Generated by Django 3.1.7 on 2021-03-30 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=150)),
                ('lastname', models.CharField(max_length=150)),
                ('wikipedia', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('price', models.FloatField(blank=True)),
                ('summary', models.TextField(blank=True)),
                ('category', models.CharField(blank=True, choices=[('AV', 'Aventure'), ('TR', 'Thriller'), ('FS', 'Fantastique'), ('RM', 'Romance'), ('HR', 'Horreur'), ('SF', 'Science-fiction')], max_length=25)),
                ('stock', models.IntegerField(default=0)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.author')),
            ],
        ),
    ]
