# Generated by Django 5.0.2 on 2024-02-18 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://cdn-icons-png.flaticon.com/512/4901/4901689.png', max_length=500),
        ),
    ]
