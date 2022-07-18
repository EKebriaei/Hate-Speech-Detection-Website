# Generated by Django 4.0.3 on 2022-07-18 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_remove_message_hatecategory_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='hateCategory',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='isHatefulInModelView',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='isHatefulInUserView',
            field=models.BooleanField(null=True),
        ),
    ]
