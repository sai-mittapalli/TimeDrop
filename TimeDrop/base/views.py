from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from datetime import datetime, timedelta, date
import calendar
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import *
from .models import Event
from .models import CalendarSave
from .forms import TodoForm
from .forms import CalendarForm
from .utils import Calendar

from .forms import SignUpForm

# Create your views here.

#calendarsModel = [
 #   {'id': 1, 'name': 'School'},
  #  {'id': 2, 'name': 'Social'},
   # {'id': 3, 'name': 'health'},
#]

# todos = [
#{'id': 1, 'name': 'work on homework'},
#{'id': 2, 'name': 'workout'},
#{'id': 3, 'name': 'go to an event'},
# ]


def home(request):
    todos = Event.objects.all()
    calendars = CalendarSave.objects.all()
    context = {
        'calendars': calendars, 
        'todos': todos}
    return render(request, 'base/templates/HomePage.html', context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username = username, password = password)   

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password does not exist')  

    context = {'loginPage': loginPage}
    return render(request, 'base/templates/Login.html', context)


def logoutPage(request):
    logout(request)
    context = {}
    return render(request, 'base/templates/Logout.html', context)
    #return redirect('login')

def signUpPage(request):

    #user = request.user

    #if user.is_authenticated:
        #return HttpResponse("You are already authenticated as {user.username}.")

    context = {'signUpPage': signUpPage}

    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        #user.refresh_from_db()
        #user.profile.first_name = form.cleaned_date.get("firstName")
        #user.profile.last_name = form.cleaned_date.get("lastName")
        #user.profile.email = form.cleaned_date.get("email")
        #user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        #user.save()
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')

    return render(request, 'base/templates/SignUpPage.html', {'form': form})    


# def calendar(request, pk):
    # calendar = None
    # for i in calendars:
    # if i['id'] == int(pk):
    # calendar = i
    # context = {'calendar': calendar}
    # return render(request, 'base/templates/CalendarPage.html', context)'

def todo(request, pk):
    todos = Event.objects.all()
    calendars = CalendarSave.objects.all()
    context = {'todos': todos, 'calendars': calendars}
    return render(request, 'base/templates/todo.html', context)

def calendarType(request, pk):
    monthlyCal = CalendarView.as_view()
    todos = Event.objects.all()
    calendarTypes = CalendarSave.objects.get(id=pk)
    context = {'calendarType': calendarType, 'todos': todos, 'monthlyCal': monthlyCal}
    return render(request, 'base/templates/calendar.html', context)


def addTask(request):
    calendars = CalendarSave.objects.all()
    context = {'calendars': calendars}

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TodoForm()
        
    return render(request, 'base/templates/AddEvent.html', {'form': form})


def addCalendar(request):

    if request.method == 'POST':
        form = CalendarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CalendarForm()
        
    return render(request, 'base/templates/AddCalendar.html', {'form': form})


def deleteTask(request, pk):
    event = Event.objects.get(id=pk)
    event.delete()
    return redirect('home')

def deleteCal(request, pk):
    cal = CalendarSave.objects.get(id=pk)
    cal.delete()
    return redirect('home')



class CalendarView(generic.ListView):
    model = Event
    template_name = 'base/templates/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        todos = Event.objects.all()

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)

        d = get_date(self.request.GET.get('month', None))
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        context['todos'] = todos
        return context


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month