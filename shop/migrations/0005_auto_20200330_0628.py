# Generated by Django 3.0.4 on 2020-03-30 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='screenshot',
            field=models.ImageField(default='', upload_to='shop/contact/'),
        ),
    ]
