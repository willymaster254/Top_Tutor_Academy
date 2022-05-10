from multiprocessing import context
from django.shortcuts import redirect, render
from .forms import OrderingForm, ProfileForm, TaskForm
from .models import Ordering, Task
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import random



# Create your views here.
class RegisterPage(FormView):
    template_name = 'Customer/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)


class CustomLoginView(LoginView):
    template_name= 'Customer/login.html'
    fields = '__all__' 
    redirect_authenticated_user= True


    

    def get_success_url(self):
        return reverse_lazy('tasks')




def home(request):
    return render(request, 'Customer/index.html')

def checkout(request):
    return render(request, 'Customer/checkout.html')

def success(request):
    return render(request, 'Customer/success.html')

def contact(request):
    return render(request, 'Customer/contact.html')

def about(request):
    return render(request, 'Customer/about.html')
def terms(request):
    return render(request, 'Customer/terms.html')

def Ordering(request):
    if request.method == 'POST':
        form = OrderingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = OrderingForm()
    return render(request, 'Customer/order.html', {
        'form': form
    })
def OrderingList(request):
    Order=Ordering.objects.all()
    return render(request, 'Customer/OrderingList.html', )

class OrderingList(ListView):
    
    model=Ordering
    context_object_name = 'Customer/Ordering'


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    


    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['completed'] = context['tasks'].filter(progress=False).count()
        context['paid'] = context['tasks'].filter(paid=False).count()

       
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                topic__startswith=search_input)

        context['search_input'] = search_input

        return context


       

        
class TaskDetail(DetailView):
    model = Task
    context_object_name= 'task'
    # template_name= ''

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields=['topic', 'description', 'pages', 
    'style', 'time', 'files', 'budget','answer',
    'invoice', 'progress', 'font_family', 'line_spacing',
    ]
    
   
  
    success_url= reverse_lazy('success')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

    


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields= ['topic', 'description', 'pages', 
    'style', 'time', 'files', 'budget','answer', 'progress'
    ]
    success_url= reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name= 'task'
    success_url= reverse_lazy('tasks')
    

@login_required
def profile(request):
    return render(request, 'Customer/profile.html')

def accountSettings(request):
	profile = request.user.profile
	form = ProfileForm(instance=profile)

	if request.method == 'POST':
		form = ProfileForm(request.POST, request.FILES,instance=profile)
		if form.is_valid():
			form.save()


	context = {'form':form}
	return render(request, 'Customer/account_settings.html', context)


# function based view
def tasklist(request):
    task = Task.objects.all()
    orders=task.count()
    completed= task.objects.filter(PROGRESS='Completed').count()
    paid= task.objects.filter(progress='Completed').count()
    return render(request, 'Customer/task_list.html', {
        'task': task
    })


def taskupload(request):
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tasklist')
    else:
        form = TaskForm()
    return render(request, 'Customer/task-create.html', {
        'form': form
    })
