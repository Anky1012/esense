# Generated by Django 4.1.6 on 2023-02-25 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0004_alter_employee_employee_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='employeetype',
            field=models.TextField(default=0),
        ),
    ]
