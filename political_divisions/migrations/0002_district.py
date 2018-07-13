# Generated by Django 2.0.7 on 2018-07-12 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('political_divisions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('population', models.IntegerField(verbose_name='Total Population')),
                ('voters', models.IntegerField(verbose_name='Total Voters')),
                ('area', models.IntegerField()),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='political_divisions.Province')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
