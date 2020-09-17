# Generated by Django 3.1.1 on 2020-09-17 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('study', '0004_students_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='scores',
            name='reg_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.user'),
            preserve_default=False,
        ),
    ]
