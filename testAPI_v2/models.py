from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class ProductSet(models.Model):
    title = models.CharField(max_length=512)
    description = models.CharField(max_length=512)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'набор'
        verbose_name_plural = 'наборы'


class Recipient(models.Model):
    surname = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    patronymic = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=64)

    def __str__(self):
        return self.surname

    class Meta:
        verbose_name = 'получатель'
        verbose_name_plural = 'получатели'


class Order(models.Model):
    order_created_datetime = models.DateTimeField(verbose_name='Дата размещения', default=timezone.now)
    delivery_datetime = models.DateTimeField(verbose_name='Дата доставки', default=timezone.now)
    delivery_address = models.CharField(verbose_name='Адрес доставки', max_length=500)
    recipient = models.ForeignKey('Recipient', on_delete=models.CASCADE, verbose_name='Получатель',
                                  related_name='recipient')
    product_set = models.ForeignKey('ProductSet', on_delete=models.CASCADE, verbose_name='Набор',
                                    related_name='product_set')

    class OrderStatus(models.TextChoices):
        CREATED = 'created', _('Создан')
        DELIVERED = 'delivered', _('Доставлен')
        PROCESSED = 'processed', _('Обрабатывается')
        CANCELLED = 'cancelled', _('Отменен')

    status = models.CharField(verbose_name='Статус', max_length=10, choices=OrderStatus.choices,
                              default=OrderStatus.CREATED)

    def __str__(self):
        return self.delivery_address

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
