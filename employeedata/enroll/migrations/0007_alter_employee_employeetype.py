# Generated by Django 4.1.6 on 2023-02-25 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0006_alter_employee_employeetype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employeetype',
            field=models.TextField(),
        ),
    ]
