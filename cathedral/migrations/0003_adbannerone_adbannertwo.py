# Generated by Django 3.2.13 on 2022-04-22 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cathedral', '0002_homebanners'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdBannerOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner', models.ImageField(default='/banners/300x600.png', upload_to='banners/')),
            ],
        ),
        migrations.CreateModel(
            name='AdBannerTwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner', models.ImageField(default='/banners/300x600.png', upload_to='banners/')),
            ],
        ),
    ]
