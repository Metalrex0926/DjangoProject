# Generated by Django 3.0.5 on 2020-04-28 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eway', '0003_auto_20200428_1126'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
