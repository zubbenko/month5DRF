# Generated by Django 4.2.5 on 2023-09-20 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.FloatField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('phone', models.CharField(max_length=20)),
                ('created', models.TimeField(auto_now_add=True)),
                ('update', models.TimeField(auto_now=True)),
            ],
        ),
    ]
