# Generated by Django 2.0.7 on 2018-07-23 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complain',
            name='url',
            field=models.URLField(editable=False),
        ),
    ]
