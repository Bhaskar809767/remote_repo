# Generated by Django 3.0.5 on 2021-02-14 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savithripuram', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='phonenumber',
            field=models.IntegerField(max_length=11),
        ),
    ]
