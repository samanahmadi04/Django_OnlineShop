# Generated by Django 4.1 on 2022-12-20 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0004_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='productbrand',
            name='url_title',
            field=models.CharField(db_index=True, default='url', max_length=200, verbose_name='عنوان در url'),
            preserve_default=False,
        ),
    ]
