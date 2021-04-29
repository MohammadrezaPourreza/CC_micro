# Generated by Django 3.1.7 on 2021-03-22 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor_panel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=20)),
                ('family_name', models.CharField(max_length=30)),
                ('phone_number', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submit_date', models.DateTimeField()),
                ('reservation_date', models.DateTimeField()),
                ('is_paid', models.BooleanField(default=False)),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor_panel.doctor')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_panel.user')),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteDoctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateField()),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor_panel.doctor')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_panel.user')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('comment_date', models.DateTimeField()),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor_panel.doctor')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_panel.user')),
            ],
        ),
    ]
