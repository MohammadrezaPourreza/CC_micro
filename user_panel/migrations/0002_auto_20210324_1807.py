# Generated by Django 3.2rc1 on 2021-03-24 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='commment',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='commment_date',
            new_name='comment_date',
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='is_payed',
            new_name='is_paid',
        ),
    ]
