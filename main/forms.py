from .models import Task, Sales, Shortages, Clients, Employee
from django.forms import ModelForm, TextInput, Textarea, NumberInput, DateInput, Select


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'task', 'quantity', 'brand', 'price', 'discount', 'section']
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
            "quantity": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите количество'
            }),

            "brand": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название бренда'
            }),
            "price": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите цену'
            }),
            "discount": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите скидку'
            }),
            "section": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите номер отдела'
            }),
        }


class SaleForm(ModelForm):
    class Meta:
        model = Sales
        fields = ['SaleData', 'idSeller', 'quantitySale', 'employee', 'client']
        widgets = {
            "SaleData": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату'
            }),
            "idSeller": Select(attrs={
                'class': 'table table-sm',
                'placeholder': 'Выберите товар'
            }),
            "quantitySale": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите количество'
            }),
            "employee": Select(attrs={
                'class': 'table table-sm',
                'placeholder': 'Выберите продавца'
            }),
            "client": Select(attrs={
                'class': 'table table-sm',
                'placeholder': 'Выберите клиента'
            }),

        }


class ShortageForm(ModelForm):
    class Meta:
        model = Shortages
        fields = ['ShortageData', 'idSeller', 'quantityShortage', 'employee']
        widgets = {
            "SaleData": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату'
            }),
            "idSeller": Select(attrs={
                'class': 'table table-sm',
                'placeholder': 'Выберите товар'
            }),
            "quantityShortage": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите количество'
            }),
            "employee": Select(attrs={
                'class': 'table table-sm',
                'placeholder': 'Выберите продавца'
            }),
        }


class ClientsForm(ModelForm):
    class Meta:
        model = Clients
        fields = ['surname', 'name', 'middlename', 'number', 'mail']
        widgets = {
            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите фамилию'
            }),
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            "middlename": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите отчество'
            }),
            "number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите номер'
            }),
            "mail": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите почту'
            }),
        }


##Список сотрудников


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['surname', 'name', 'middlename', 'number', 'mail', 'salary', 'points']
        widgets = {
            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите фамилию'
            }),
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            "middlename": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите отчество'
            }),
            "number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите номер'
            }),
            "mail": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите почту'
            }),
            "salary": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите зарплату'
            }),
            "points": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите баллы'
            }),

        }
