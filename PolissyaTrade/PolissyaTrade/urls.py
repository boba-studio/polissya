"""
URL configuration for PolissyaTrade project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from catalog import views
from django.urls import re_path

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('edit1/<int:id>/', views.edit1, name='edit1'),
    path('create/', views.create, name='create'),
    path('delete/<int:id>/', views.delete, name='delete'),
    re_path(r'^employees/$', views.EmployeeListView.as_view(), name='employees'),
    re_path(r'^employee/(?P<pk>\d+)$', views.EmployeeDetailView.as_view(), name='employee-detail'),
    re_path(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    path('authors_add/', views.authors_add, name='authors_add'),
    re_path(r'^mypersons/$', views.LoanedPersonsByUserListView.as_view(), name='my-borrowed'),

]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]