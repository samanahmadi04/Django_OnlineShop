# Generated by Django 4.1 on 2022-11-03 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0002_remove_user_mobile_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about_user',
            field=models.TextField(blank=True, null=True, verbose_name='درباره کاربر'),
        ),
    ]