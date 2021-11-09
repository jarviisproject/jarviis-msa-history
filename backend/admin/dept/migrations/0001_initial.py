# Generated by Django 3.2.5 on 2021-11-06 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeptVo',
            fields=[
                ('dept_no', models.AutoField(primary_key=True, serialize=False)),
                ('dname', models.TextField()),
                ('loc', models.TextField()),
            ],
            options={
                'db_table': 'dept',
                'managed': True,
            },
        ),
    ]
