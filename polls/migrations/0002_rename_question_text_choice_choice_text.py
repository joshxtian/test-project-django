# Generated by Django 3.2 on 2021-05-03 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='question_text',
            new_name='choice_text',
        ),
    ]
