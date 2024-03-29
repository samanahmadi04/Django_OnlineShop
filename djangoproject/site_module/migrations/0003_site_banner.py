# Generated by Django 4.1 on 2022-12-29 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0002_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='site_banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('url', models.CharField(blank=True, max_length=400, null=True, verbose_name='ادرس بنر')),
                ('image', models.ImageField(upload_to='images/banners', verbose_name='تصویر بنر')),
                ('is_active', models.BooleanField(verbose_name='فعال/غیرفعال')),
                ('position', models.CharField(choices=[('product_list', 'صفحه لیست محصولات'), ('product_detail', 'صفحه جزییات محصولات'), ('about_us', 'صفحه درباره ما')], max_length=200, verbose_name='جایگاه نمایشی')),
            ],
            options={
                'verbose_name': 'بنر سایت',
                'verbose_name_plural': 'بنر های سایت',
            },
        ),
    ]
