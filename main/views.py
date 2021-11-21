from typing import List, Any, Union

from django.forms import NumberInput, TextInput, Textarea
from django.shortcuts import render, redirect
from .models import Task, Sales, Shortages, Clients, Employee
from .forms import TaskForm, SaleForm, ShortageForm, ClientsForm, EmployeeForm
from django.views.generic import UpdateView, DeleteView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


def products(request):
    if request.user.is_anonymous:
        return redirect('login')
    if request.user.is_authenticated:
        global el
        search_query = request.GET.get('search', '')
        if search_query:
            tasks = Task.objects.filter(Q(title=search_query) | Q(brand=search_query))
        else:
            tasks = Task.objects.all()

        for el in tasks:
            el.FinishPrice = el.price - el.price * el.discount / 100
        return render(request, 'main/products.html',
                      {'title': 'Список товаров', 'tasks': tasks})


def LogError(request):
    return render(request, 'main/LogError.html')


def BrandDiscount(request):
    OurDiscount = request.GET.get('ChangingDiscount', '')
    OurBrand = request.GET.get('ChangingBrand', '')
    if request.user.is_anonymous:
        return redirect('login')
    if not request.user.has_perm('admin_permission'):
        return redirect('LogError')
    if request.user.is_authenticated:

        if OurDiscount and OurBrand:
            for el in Task.objects.filter(brand=OurBrand):
                el.discount = OurDiscount
                el.save(update_fields=['discount'])
            return redirect('products')

        return render(request, 'main/BrandDiscount.html')


def SectionDiscount(request):
    OurDiscount = request.GET.get('ChangingDiscount', '')
    OurSection = request.GET.get('ChangingSection', '')
    if request.user.is_anonymous:
        return redirect('login')
    if not request.user.has_perm('admin_permission'):
        return redirect('LogError')
    if request.user.is_authenticated:
        if OurDiscount and OurSection:
            for el in Task.objects.filter(section=OurSection):
                el.discount = OurDiscount
                el.save(update_fields=['discount'])
            return redirect('products')

        return render(request, 'main/SectionDiscount.html')


def menu(request):
    return render(request, 'main/menu.html')


def create(request):
    if request.user.is_anonymous:
        return redirect('login')
    if not request.user.has_perm('admin_permission'):
        return redirect('LogError')
    if request.user.is_authenticated:
        error = ''
        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('products')
            else:
                error = 'Форма была неверной'

        form = TaskForm()
        context = {
            'form': form,
            'error': error
        }
        return render(request, 'main/create.html', context)


class UpdateProducts(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Task
    permission_required = 'admin_permission'
    form = TaskForm
    template_name = 'main/UpdateProducts.html'
    fields = ['title', 'price', 'discount', 'task', 'quantity', 'brand', 'section']


class DeleteProducts(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Task
    permission_required = 'admin_permission'
    success_url = '/products'
    template_name = 'main/DeleteProducts.html'
    fields = ['title', 'task', 'quantity', 'brand']


## Журнал продаж


def sale(request):
    if request.user.is_anonymous:
        return redirect('login')
    if request.user.is_authenticated:
        search_query = request.GET.get('search', '')
        if search_query:
            tasks = Sales.objects.filter(SaleData=search_query)
        else:
            tasks = Sales.objects.all()
        return render(request, 'main/sale.html',
                      {'SaleData': 'Список товаров', 'tasks': tasks})


def createSale(request):
    if request.user.is_anonymous:
        return redirect('login')
    if request.user.is_authenticated:
        error = ''
        if request.method == 'POST':
            form = SaleForm(request.POST)

            if form.is_valid():
                idSeller = form.cleaned_data['idSeller']
                for el in Task.objects.filter(title=idSeller):
                    el.quantity = el.quantity - form.cleaned_data['quantitySale']
                    el.save(update_fields=['quantity'])

                    ThisEmployee = form.cleaned_data['employee']
                    for el in Employee.objects.filter(surname=ThisEmployee):
                        el.points = el.points + form.cleaned_data['quantitySale']
                        el.save(update_fields=['points'])



                form.save()
                return redirect('sale')
            else:
                error = 'Форма была неверной'

        form = SaleForm()
        context = {
            'form': form,
            'error': error
        }
        return render(request, 'main/createSale.html', context)

    ##Журнал Недостач


def shortage(request):

    if request.user.is_anonymous:
        return redirect('login')
    if request.user.is_authenticated:
        search_query = request.GET.get('search', '')
        if search_query:
            tasks = Shortages.objects.filter(SaleData=search_query)
        else:
            tasks = Shortages.objects.all()
        return render(request, 'main/shortage.html',
                      {'SaleData': 'Журнал недостач', 'tasks': tasks})


def createShortage(request):
    if request.user.is_anonymous:
        return redirect('login')
    if not request.user.has_perm('admin_permission'):
        return redirect('LogError')
    if request.user.is_authenticated:
        error = ''
        if request.method == 'POST':
            form = ShortageForm(request.POST)

            if form.is_valid():
                idShortage = form.cleaned_data['idSeller']
                for el in Task.objects.filter(title=idShortage):
                    el.quantity = el.quantity - form.cleaned_data['quantityShortage']
                    el.save(update_fields=['quantity'])

                ThisEmployee = form.cleaned_data['employee']
                for el in Employee.objects.filter(surname=ThisEmployee):
                    el.points = el.points - form.cleaned_data['quantityShortage']
                    el.save(update_fields=['points'])

                form.save()
                return redirect('shortage')
            else:
                error = 'Форма была неверной'

        form = ShortageForm()
        context = {
            'form': form,
            'error': error
        }
        return render(request, 'main/createShortage.html', context)




def client(request):
    if request.user.is_anonymous:
        return redirect('login')
    if request.user.is_authenticated:
        search_query = request.GET.get('search', '')
        if search_query:
            tasks = Clients.objects.filter(surname=search_query)
        else:
            tasks = Clients.objects.all()
        return render(request, 'main/client.html',
                      {'title': 'Список клиентов', 'tasks': tasks})


def createClient(request):
    if request.user.is_anonymous:
        return redirect('login')
    if request.user.is_authenticated:
        error = ''
        if request.method == 'POST':
            form = ClientsForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('client')
            else:
                error = 'Форма была неверной'

        form = ClientsForm()
        context = {
            'form': form,
            'error': error
        }
        return render(request, 'main/createClient.html', context)


class DeleteClient(LoginRequiredMixin, DeleteView):
    model = Clients
    success_url = '/client'
    template_name = 'main/DeleteClient.html'
    fields = ['surname', 'name', 'middlename', 'number', 'mail']


class UpdateClient(LoginRequiredMixin,UpdateView):
    model = Clients
    form = ClientsForm
    template_name = 'main/UpdateClient.html'
    fields = ['surname', 'name', 'middlename', 'number', 'mail']


## Список сотрудников


def employee(request):
    if request.user.is_anonymous:
        return redirect('login')
    if request.user.is_authenticated:
        search_query = request.GET.get('search', '')
        if search_query:
            tasks = Employee.objects.filter(surname=search_query)
        else:
            tasks = Employee.objects.all()
        return render(request, 'main/employee.html',
                      {'title': 'Список сотрудников', 'tasks': tasks})


def createEmployee(request):
    if request.user.is_anonymous:
        return redirect('login')
    if not request.user.has_perm('admin_permission'):
        return redirect('LogError')
    if request.user.is_authenticated:
        error = ''
        if request.method == 'POST':
            form = EmployeeForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('employee')
            else:
                error = 'Форма была неверной'

        form = EmployeeForm()
        context = {
            'form': form,
            'error': error
        }
        return render(request, 'main/createEmployee.html', context)


class DeleteEmployee(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Employee
    permission_required = 'admin_permission'
    success_url = '/employee'
    template_name = 'main/DeleteEmployee.html'
    fields = ['surname', 'name', 'middlename', 'number', 'mail', 'points', 'salary']


class UpdateEmployee(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Employee
    permission_required = 'admin_permission'
    form = EmployeeForm
    template_name = 'main/UpdateEmployee.html'
    fields = ['surname', 'name', 'middlename', 'number', 'mail', 'points', 'salary']




