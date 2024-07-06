# Generated by Django 5.0.6 on 2024-06-27 14:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('singer', '0002_alter_singer_debut'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('release', models.CharField(max_length=50)),
                ('content', models.TextField(max_length=200)),
                ('singer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='singer.singer')),
            ],
        ),
    ]