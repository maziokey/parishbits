# Generated by Django 3.2.11 on 2022-03-02 09:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reflection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('sub_title', models.CharField(blank=True, max_length=250, null=True)),
                ('name', models.CharField(max_length=250)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, default='/banners/user.png', null=True, upload_to='banners/')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('slug', models.SlugField(max_length=250, unique_for_date='publish')),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
    ]