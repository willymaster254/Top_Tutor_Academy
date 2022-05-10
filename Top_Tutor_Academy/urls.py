"""Top_Tutor_Academy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from Customer import views
from django.conf import settings
from django.conf.urls.static import static
from Customer.views import OrderingList
from Customer.views import TaskList
from Customer.views import TaskDetail
from Customer.views import TaskCreate
from Customer.views import TaskUpdate, TaskDelete,CustomLoginView,LogoutView, RegisterPage
from Customer import views as user_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('checkout/', views.checkout, name='checkout'),
    path('terms/', views.terms, name='terms'),
    path('ordering/', views.Ordering, name='ordering'),
    path('order/', OrderingList.as_view(), name='Order'),
    path('tasks/', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page= '/'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('account/', views.accountSettings, name="account"),
    path('tasklist/', views.tasklist, name='tasklist'),
    path('taskupload/', views.taskupload, name='taskupload'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success'),



]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)