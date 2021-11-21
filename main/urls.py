
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('products', views.products, name='products'),
    path('BrandDiscount', views.BrandDiscount, name='BrandDiscount'),
    path('SectionDiscount', views.SectionDiscount, name='SectionDiscount'),
    path('create', views.create, name='create'),
    path('<int:pk>/UpdateProducts', views.UpdateProducts.as_view(), name='UpdateProducts'),
    path('<int:pk>/DeleteProducts', views.DeleteProducts.as_view(), name='DeleteProducts'),
    path('LogError', views.LogError, name='LogError'),
    path('sale', views.sale, name='sale'),
    path('createSale', views.createSale, name='createSale'),
    path('shortage', views.shortage, name='shortage'),
    path('createShortage', views.createShortage, name='createShortage'),
    path('client', views.client, name='client'),
    path('createClient', views.createClient, name='createClient'),
    path('<int:pk>/DeleteClient', views.DeleteClient.as_view(), name='DeleteClient'),
    path('<int:pk>/UpdateСlient', views.UpdateClient.as_view(), name='UpdateClient'),
    path('employee', views.employee, name='employee'),
    path('createEmployee', views.createEmployee, name='createEmployee'),
    path('<int:pk>/DeleteEmployee', views.DeleteEmployee.as_view(), name='DeleteEmployee'),
    path('<int:pk>/UpdateEmployee', views.UpdateEmployee.as_view(), name='UpdateEmployee'),
]


#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]