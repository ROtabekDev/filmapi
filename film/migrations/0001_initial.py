# Generated by Django 4.0.2 on 2022-03-03 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Ismi')),
                ('last_name', models.CharField(max_length=50, verbose_name='Familiyasi')),
                ('birthdate', models.DateTimeField(verbose_name='Tug`ilgan sanasi')),
                ('gender', models.CharField(choices=[('Male', 'Erkak'), ('Female', 'Ayol')], max_length=30, verbose_name='Jinsi')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Sarlavhasi')),
                ('year', models.PositiveIntegerField(verbose_name='Chiqarilgan yili')),
                ('imdb', models.IntegerField(verbose_name='IMDB')),
                ('genre', models.CharField(choices=[('Horror', 'Qo`rqinchli'), ('Comedy', 'Komediya'), ('Adventure', 'Sarguzasht'), ('Romace', 'Romantika'), ('Historical', 'Tarixiy')], max_length=30, verbose_name='Kino janri')),
                ('actors', models.ManyToManyField(to='film.Actor')),
            ],
        ),
    ]
