from django.db import models


# Create your models here.


class Task(models.Model):
    title = models.CharField('Название', max_length=20)
    task = models.TextField('Описание')
    quantity = models.IntegerField('Количество')
    brand = models.CharField('Бренд', max_length=20)
    price = models.IntegerField('Цена')
    discount = models.IntegerField('Скидка', default=0)
    section = models.IntegerField('Номер отдела')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        permissions = (("admin_permission", "admin permission"),)

    def get_absolute_url(self):
        return f'/products'


##Список сотрудников


class Employee(models.Model):
    surname = models.CharField('Фамилия', max_length=20)
    name = models.CharField('Имя', max_length=20)
    middlename = models.CharField('Отчество', max_length=20)
    number = models.CharField('Номер телефона', max_length=20)
    mail = models.CharField('Почтовый адрес', max_length=20)
    salary = models.IntegerField('Запрплата')
    points = models.IntegerField('Баллы', default=0)

    def __str__(self):
        return self.surname

    class Meta:
        verbose_name = 'сотрудник'
        verbose_name_plural = 'сотрудники'
        permissions = (("admin_permission", "admin permission"),)

    def get_absolute_url(self):
        return f'/employee'


##Список клиентов


class Clients(models.Model):
    surname = models.CharField('Фамилия', max_length=20)
    name = models.CharField('Имя', max_length=20)
    middlename = models.CharField('Отчество', max_length=20)
    number = models.CharField('Номер телефона', max_length=20)
    mail = models.CharField('Почтовый адрес', max_length=20)

    def __str__(self):
        return self.surname

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        permissions = (("admin_permission", "admin permission"),)

    def get_absolute_url(self):
        return f'/client'


# ЖурналПродаж

class Sales(models.Model):
    SaleData = models.DateField('Дата')
    idSeller = models.ForeignKey(Task, on_delete=models.CASCADE)
    quantitySale = models.IntegerField('Количество')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)

    def __str__(self):
        name = str(self.idSeller) + " " + str(self.SaleData)
        return name

    class Meta:
        verbose_name = 'Продажа'
        verbose_name_plural = 'Продажи'
        permissions = (("admin_permission", "admin permission"),)

    def get_absolute_url(self):
        return f'/sale'


##Журнал недостач

class Shortages(models.Model):
    ShortageData = models.DateField('Дата')
    idSeller = models.ForeignKey(Task, on_delete=models.CASCADE)
    quantityShortage = models.IntegerField('Количество')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        name = str(self.idSeller) + " " + str(self.ShortageData)
        return name

    class Meta:
        verbose_name = 'Недостача'
        verbose_name_plural = 'Недостачи'
        permissions = (("admin_permission", "admin permission"),)

    def get_absolute_url(self):
        return f'/sale'
