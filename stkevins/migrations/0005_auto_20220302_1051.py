# Generated by Django 3.2.11 on 2022-03-02 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stkevins', '0004_alter_event_managers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contribution',
            name='parishioner',
        ),
        migrations.RemoveField(
            model_name='levy',
            name='parishioner',
        ),
        migrations.RemoveField(
            model_name='parishioner',
            name='community',
        ),
        migrations.RemoveField(
            model_name='parishioner',
            name='sacraments',
        ),
        migrations.RemoveField(
            model_name='parishioner',
            name='societies',
        ),
        migrations.DeleteModel(
            name='Community',
        ),
        migrations.DeleteModel(
            name='Contribution',
        ),
        migrations.DeleteModel(
            name='Levy',
        ),
        migrations.DeleteModel(
            name='Parishioner',
        ),
        migrations.DeleteModel(
            name='Sacrament',
        ),
        migrations.DeleteModel(
            name='Society',
        ),
    ]
