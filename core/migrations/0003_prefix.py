# Generated by Django 3.2.5 on 2021-07-05 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prefix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rule', models.CharField(max_length=100, verbose_name='Rule Name')),
                ('homepage', models.SlugField(verbose_name='Homeage')),
                ('posts', models.SlugField(verbose_name='Posts List')),
                ('post', models.SlugField(verbose_name='Single Post')),
                ('page', models.SlugField(verbose_name='Page')),
                ('author', models.SlugField(verbose_name='Author')),
                ('category', models.SlugField(verbose_name='Category')),
                ('tag', models.SlugField(verbose_name='Tag')),
                ('is_active', models.BooleanField(default=False, verbose_name='Active')),
            ],
        ),
    ]
