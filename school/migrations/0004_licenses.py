# Generated by Django 3.2.13 on 2024-08-16 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_teachers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Licenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]
