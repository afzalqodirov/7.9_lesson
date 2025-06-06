# Generated by Django 5.2.1 on 2025-06-01 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lugat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('unique_identificator', models.PositiveIntegerField()),
                ('language', models.IntegerField()),
                ('relateds', models.ManyToManyField(blank=True, to='lugat.lugat')),
                ('sinonim', models.ManyToManyField(blank=True, to='lugat.lugat')),
            ],
            options={
                'db_table': 'lugat',
                'unique_together': {('name', 'language')},
            },
        ),
    ]
