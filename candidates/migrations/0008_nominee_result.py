# Generated by Django 2.0.7 on 2018-07-19 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0002_auto_20180719_0652'),
        ('candidates', '0007_auto_20180706_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='nominee',
            name='result',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='results.Result'),
            preserve_default=False,
        ),
    ]
