# Generated by Django 3.2rc1 on 2021-03-23 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_panel', '0002_doctor_degree'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='degree',
            field=models.CharField(default='omoomi', max_length=50),
        ),
    ]
