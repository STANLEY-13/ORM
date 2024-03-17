# Generated by Django 5.0.3 on 2024-03-04 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='books_DB',
            fields=[
                ('refno', models.IntegerField(primary_key='refno', serialize=False)),
                ('bookname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('Doissued', models.DateField()),
                ('reviews', models.CharField(max_length=20)),
            ],
        ),
    ]