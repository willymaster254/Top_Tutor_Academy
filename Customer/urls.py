
from django.urls import path
from Customer import views
from .views import TaskList
from .views import TaskDetail
from .views import TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, LogoutView, RegisterPage, user_views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasklist/', views.tasklist, name='tasklist'),
    path('success/', views.success, name='success'),
    path('taskupload/', views.taskupload, name='taskupload'),
    path('about/', views.about, name='about'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('terms/', views.terms, name='terms'),
    path('ordering/', views.Ordering, name='ordering'),
    path('tasks/', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('account/', views.accountSettings, name="account"),

]