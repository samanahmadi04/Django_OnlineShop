# Generated by Django 4.1 on 2022-12-29 15:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('production', '0005_productbrand_url_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductVisit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=30, verbose_name='ای پی کاربر')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production.product', verbose_name='محصول')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'بازدید محصول',
                'verbose_name_plural': 'بازدیدهای محصول',
            },
        ),
    ]
