# Generated by Django 3.2rc1 on 2021-03-24 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_panel', '0003_alter_doctor_degree'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='degree',
            field=models.CharField(default='omomi', max_length=50),
        ),
    ]