from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from author.decorators import with_author
from django.urls import reverse

# Create your models here.





class Shop(models.Model):
    title = models.CharField(max_length=10000, verbose_name='اسم المحل')
    num = models.CharField(max_length=1000, verbose_name='رقم جهاز مدي')
    mobile = models.CharField(max_length=1000, verbose_name='رقم الهاتف')

    def __str__(self):
        a = str(self.title)
        return a

    class Meta:
        ordering = ('-id',)
        verbose_name = ('محل')
        verbose_name_plural = ('المحلات')

    def get_absolute_url(self):
        # return '/detail/{}'.format(self.pk)
        return reverse('detail', args=[self.id])





@with_author
class Bond(models.Model):
    shop = models.ManyToManyField(Shop,related_name='posts', verbose_name='المحل')
    responsible = models.CharField(max_length=10000, verbose_name='المسؤول عن القبض ')
    operation_number = models.CharField(max_length=10000, unique=True,error_messages ={ "unique":"عزيزي الموظف رقم العمليه مكرر يرجى مراجعة البحث وشكرا."} ,verbose_name='رقم العمليه')
    deserved_amount = models.FloatField(verbose_name='المبلغ المستحق')
    paid_amount = models.FloatField(verbose_name='المبلغ المدفوع')
    residual = models.FloatField(verbose_name='المبلغ المتبقي')
    discount = models.FloatField(verbose_name='الخصم')
    bond_date = models.DateTimeField(auto_now=True, verbose_name='تاريخ القبض')
    peration_date = models.DateTimeField(default=timezone.now, verbose_name='تاريخ العمليه')
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        a = str(self.operation_number)
        return a

    class Meta:
        ordering = ('-bond_date',)
        verbose_name = ('سند')
        verbose_name_plural = ('السندات')







