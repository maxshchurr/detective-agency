from django.core.exceptions import ValidationError
from django.db import models


class Clients(models.Model):

    class Meta:
        db_table = 'clients'
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    full_name = models.CharField(verbose_name="Имя", max_length=70)
    email = models.EmailField(verbose_name="Почта", max_length=50, unique=True)
    client_login = models.CharField(verbose_name="Логин", max_length=30, unique=True)
    client_password = models.CharField(verbose_name="Пароль", max_length=30)
    tel_number = models.CharField(verbose_name="Телефон", max_length=13, unique=True)

    def __str__(self):
        return f"{self.full_name} {self.email} {self.client_login} {self.client_password} {self.tel_number}"


class TypeOfOrder(models.Model):
    type_of_order = (
                    ('Наблюдение', 'Наблюдение'),
                    ('Сбор информации', 'Сбор информации'),
                    ('Розыск человека', 'Розыск человека')
                     )

    type = models.CharField(verbose_name='Тип заказа', max_length=50, choices=type_of_order, unique=True)
    price = models.IntegerField(verbose_name='Цена')
    expected_days = models.IntegerField(verbose_name='Ожидаемое количество дней')

    class Meta:
        db_table = 'type_of_order'
        verbose_name = 'Тип заказа'
        verbose_name_plural = 'Типы заказов'

    def __str__(self):
        return f'Type - {self.type} Price - {self.price}, TYPEOFORDER PK - {self.pk}'


class Order(models.Model):
    orders_status = (
        ('Closed', 'Закрыта'),
        ('In process', 'На рассмотрении менеджера'),
        ('Payed', 'Оплачена'),
        ('Rejected by client', 'Отклонена клиентом'),
        ('Rejected by manager', 'Отклонена менеджером'),
        ('In work', 'В работе')
    )

    client_comment = models.TextField(verbose_name='Комментарий', max_length=500, default='', null=True)
    created_at = models.DateField(verbose_name='Дата создания', default=2022, null=True)
    status = models.CharField(verbose_name='Статус заказа', choices=orders_status, max_length=50, default='In process', null=True)
    rate = models.IntegerField(verbose_name='Рейтинг', default=1, null=True)
    type_of_order = models.ForeignKey(TypeOfOrder, verbose_name='Тип заказа', on_delete=models.PROTECT)
    client = models.ForeignKey(Clients, verbose_name='Клиент', on_delete=models.CASCADE)
    # У ЗАЯВКИ ВСЕГДА ДОЛЖЕН БЫТЬ КЛИЕНТ, НО DJANGO НЕ РАЗРЕШАЕТ СОЗДАТЬ ПОЛЕ client БЕЗ ЗНАЧЕНИЯ ДЛЯ default,
    # ХОТЯ type_of_order СОЗДАЛСЯ...ПОКА НЕ КРИТИЧНО НО НЕОБХОДИМО РАЗОБРАТЬСЯ

    class Meta:
        db_table = 'order'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Type - {self.type_of_order}, Status - {self.status}, ORDER PK - {self.pk}'


class Employees(models.Model):

    class Meta:
        db_table = 'employees'
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    employees_status = (('Busy', 'Занят'),
                        ('Available', 'Свободен'))

    employees_position = (('Admin', 'Администратор'),
                          ('Chief', 'Начальник'),
                          ('Detective', 'Детектив'),
                          ('Assistant', 'Помощник детектива'),
                          ('Manager', 'Менеджер'))

    first_name = models.CharField(verbose_name="Имя", max_length=30)
    surname = models.CharField(verbose_name="Фамилия", max_length=30)
    date_of_birth = models.DateField(verbose_name="Дата рождения")
    e_email = models.EmailField(verbose_name="Почта")
    employees_password = models.CharField(verbose_name="Пароль", max_length=30)
    experience = models.IntegerField(verbose_name="Стаж")
    salary = models.IntegerField(verbose_name="Зарплата")
    tel_number = models.CharField(verbose_name="Номер телефона", max_length=13)
    position = models.CharField(verbose_name="Должность", max_length=30, choices=employees_position)
    status = models.CharField(verbose_name="Статус сотрудника", max_length=30, choices=employees_status)

    def __str__(self):
        return f'{self.first_name} {self.surname} {self.date_of_birth} {self.e_email}' \
               f'{self.employees_password} {self.experience} {self.salary} ' \
               f'{self.tel_number} {self.position} {self.status}'


class Tasks(models.Model):
    class Meta:
        db_table = 'tasks'
        verbose_name = "Задание"
        verbose_name_plural = "Задания"