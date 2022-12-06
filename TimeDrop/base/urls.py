from django.urls import path
from .import views


urlpatterns = [
    path('', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),
    path('signUpPage/', views.signUpPage, name="signup"),


    path('home/', views.home, name="home"),

    path('calendar/<str:pk>/', views.CalendarView.as_view(), name="calendar"),
    path('todo/<str:pk>/', views.todo, name="todo"),


    path('addTask/', views.addTask, name="addTask"),
    path('addCalendar/', views.addCalendar, name="addCalendar"),

    path('deleteTask/<str:pk>/', views.deleteTask, name="deleteTask"),
    path('deleteCal/<str:pk>/', views.deleteCal, name="deleteCal"),

]
