# Generated by Django 4.1 on 2023-02-16 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('birthday', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('annual_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('first_day', models.DateField()),
            ],
        ),
    ]
