# Generated by Django 4.1 on 2022-09-22 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('productora', models.CharField(max_length=40)),
                ('genero', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('actorprincipal', models.CharField(max_length=40)),
                ('anio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('actorprincipal', models.CharField(max_length=40)),
                ('anio', models.IntegerField()),
            ],
        ),
    ]
