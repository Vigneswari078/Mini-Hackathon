# Generated by Django 3.0.5 on 2021-01-26 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeAccounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=100)),
                ('EmployeeID', models.IntegerField()),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
