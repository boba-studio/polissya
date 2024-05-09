from django.contrib import admin
from django.urls import path
from catalog import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('authors_add/', views.authors_add, name='authors_add'),
    path('edit1/<int:id>/', views.edit1, name='edit1'),
    path('admin/', admin.site.urls),
    url(r'^employee/(?P<pk>\d+)$', views.EmployeeDetailView(), name='employee_detail'),
    url(r'^employees/$', views.EmployeeListView.as_view(), name='employees'),
    url(r'^mypersons/$', views.LoanedPersonByUserListView.as_view(), name='my-borrowed'),
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += [
    url(r'^employee/create/$', views.EmployeeCreate.as_view(),
        name='employee_create'),
    url(r'^employee/update/(?P<pk>\d+)$', views.EmployeeUpdate.as_view(),
        name='book_update'),
    url(r'^employee/delete/(?P<pk>\d+)$', views.EmployeeDelete.as_view(),
        name='employee_delete'),
]