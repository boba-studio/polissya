from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee, Author, Person, Abilities
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import *
from .forms import AuthorsForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Employee
# Create your views here.

def index(request):
    num_employees = Employee.objects.all().count()
    num_persons = Person.objects.all().count()
    num_persons_available = Person.objects.filter(status__exact=2).count()
    num_authors = Author.objects.count()
    num_visits =request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(request, 'index.html',
                  context={'num_employees': num_employees,
                           'num_persons': num_persons,
                           'num_persons_available': num_persons_available,
                           'num_authors': num_authors,
                           'num_visits': num_visits
                           },
                  )
class EmployeeListView(generic.ListView):
    model = Employee
    paginate_by = 10
    
class EmployeeDetailView(generic.DetailView):
    model = Employee

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10

class LoanedPersonsByUserListView(LoginRequiredMixin, generic.ListView):
    '''
    Універсальний клас для представлення списку книг,
    які знаходяться в замовленні поточного користувача.
    '''
    model = Person
    template_name = 'catalog/person_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return Person.objects.filter(
            borrower=self.request.user).filter(status_exact='2').order_by('due_back')

def authors_add(request):
    author = Author.objects.all()
    authorsform = AuthorsForm()
    return render(request, "catalog/authors_add.html",
                  {"form": authorsform, "author": author})

def create(request):
    if request.method == "POST":
        author = Author()
        author.first_name = request.POST.get("first_name")
        author.last_name = request.POST.get("last_name")
        author.date_of_birth = request.POST.get("date_of_birth")
        author.date_of_enrollment = request.POST.get("date_of_enrollment")
        author.save()
        return HttpResponseRedirect("/authors_add/")

def delete(request, id):
    try:
        author = Author.objects.get(id=id)
        author.delete()
        return HttpResponseRedirect("/authors_add/")
    except Author.DoesNotExist:
        return HttpResponseNotFound("<h2>Працівник не знайдений!</h2>")

def edit1(request, id):
    author = Author.objects.get(id=id)
    if request.method == "POST":
        author.first_name = request.POST.get("first_name")
        author.last_name = request.POST.get("last_name")
        author.date_of_birth = request.POST.get("date_of_birth")
        author.date_of_enrollment = request.POST.get("date_of_enrollment")
        author.save()
        return HttpResponseRedirect("/authors_add/")
    else:
        return render(request, "edit1.html", {"author": author})

class EmployeeCreator(CreateView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('employees')

class EmployeeUpdate(UpdateView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('employee')

class EmployeeDelete(DeleteView):
    model = Employee
    success_url = reverse_lazy('employee')