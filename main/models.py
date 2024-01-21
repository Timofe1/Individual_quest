from django.db import models
import pymysql

class Atributs(models.Model):
    nameProduct = models.CharField('Название продукта', max_length=50)
    productPrice = models.CharField('Цена продукта', max_length=50)
    description = models.TextField('Описание продукта')
    typeProduct = models.CharField('Тип продукта', max_length=50)

    def __str__(self):
        return self.nameProduct