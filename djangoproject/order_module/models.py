from django.db import models
from production.models import Product
from account_module.models import User


# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    is_paid = models.BooleanField(blank=True, null=True, verbose_name='نهایی شده/نشده')
    payment_date = models.DateField(blank=True, null=True, verbose_name='تاریخ پرداخت')

    def calculate_total_price(self):
        total_amount = 0
        if self.is_paid:
            for order_detail in self.detailorder_set.all():
                total_amount += order_detail.final_price * order_detail.count
        else:
            for order_detail in self.detailorder_set.all():
                total_amount += order_detail.product.price * order_detail.count

        return total_amount

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبدهای خرید کاربران'


class DetailOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سبد خرید')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    final_price = models.IntegerField(blank=True, null=True, verbose_name='قیمت نهایی تکی محصول')
    count = models.IntegerField(verbose_name='تعداد')

    def get_total_price(self):
        return self.count * self.product.price

    def __str__(self):
        return str(self.order)

    class Meta:
        verbose_name = 'جزییات سبد خرید'
        verbose_name_plural = 'لیست جزییات سبدهای خرید'
