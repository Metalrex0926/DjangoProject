# Generated by Django 3.0.5 on 2020-04-28 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eway', '0004_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='eway.Tag'),
        ),
    ]