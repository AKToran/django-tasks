# Generated by Django 4.2.7 on 2023-12-17 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyerhistory',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
