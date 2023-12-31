# Generated by Django 5.0 on 2023-12-07 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_management', '0002_alter_user_is_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=100, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.TextField(max_length=50, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='Admin Account'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.TextField(max_length=50, verbose_name='Last name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.TextField(max_length=13, verbose_name='Phone Number'),
        ),
    ]
