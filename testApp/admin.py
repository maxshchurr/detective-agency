from django.contrib import admin

from .models import Employees, Clients, Order, TypeOfOrder

class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'surname', 'date_of_birth', 'e_email',
                    'employees_password', 'experience', 'salary', 'tel_number',
                    'position', 'status')

class ClientsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'client_login', 'client_password', 'tel_number')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('client_comment', 'created_at', 'status', 'rate', 'type_of_order', 'client_id')

class TypeOfOrderAdmin(admin.ModelAdmin):
    list_display = ('type', 'price', 'expected_days')


admin.site.register(Employees, EmployeesAdmin)
admin.site.register(Clients, ClientsAdmin)
admin.site.register(TypeOfOrder, TypeOfOrderAdmin)
admin.site.register(Order, OrderAdmin)


