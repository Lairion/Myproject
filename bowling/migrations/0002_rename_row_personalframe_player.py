# Generated by Django 3.2.3 on 2021-07-17 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bowling', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personalframe',
            old_name='row',
            new_name='player',
        ),
    ]
