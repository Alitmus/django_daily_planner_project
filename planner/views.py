from typing import Any
from django.views.generic import TemplateView,ListView ,DetailView ,CreateView ,UpdateView, DeleteView
from .models import Activity , Category ,Action
from django.shortcuts import render 
import datetime
from .forms import CustomDateForm ,ActionForm 
from django.contrib import messages
from django.urls import reverse_lazy


class HomeView(TemplateView):
    template_name='planner/home.html'
      

class ActivityTemplateView(TemplateView):
    model =Activity
    template_name = 'planner/activity.html'


class ActivityCreateView(CreateView):
    model =Activity 
    fields='__all__'
    success_url='/planner/activity_list/'


class ActivityListView(ListView):
    model=Activity


class ActivityUpdateView(UpdateView):
    model=Activity
    fields='__all__'
    success_url=reverse_lazy('planner:activity_list')


class ActivityDeleteView(DeleteView):
    model=Activity
    success_url=reverse_lazy('planner:activity_list')


class CategoryCreateView(CreateView):
    model =Category 
    fields='__all__'
    success_url='/planner/activity_form/'


class CategoryListView(ListView):
    model=Category


class CategoryUpdateView(UpdateView):
    model=Category
    fields='__all__'
    success_url=reverse_lazy('planner:category_list')


class CategoryDeleteView(DeleteView):
    model=Category
    success_url=reverse_lazy('planner:category_list')


class ActionListView(ListView):
    model=Action
    today=datetime.date.today()
    today_actions=Action.objects.filter(date=today).order_by('start_time')

    def get_queryset(self):
        return self.today_actions
        

class ActionUpdateView(UpdateView):
    model=Action
    fields='__all__'
    success_url='/planner/action_list/'


class ActionDeleteView(DeleteView):
    model=Action
    success_url=reverse_lazy('planner:action_list')


def activity_report_view(request):
    activity=request.GET.get('action')
    report=None
    if activity:
        report=Action.objects.all()
        report = report.filter(action=activity)
        
    context={'form':ActionForm(),
             'actions':report ,
             }
    
    return render (request,'planner/activity_report.html',context)


def custom_date_view(request):
    user_date=request.GET.get('date')
    actions=None
    if user_date:
        actions=Action.objects.all()
        actions = actions.filter(date=user_date)
        
    context={'form':CustomDateForm(),
             'actions':actions,
               }
    
    return render (request,'planner/custom_date.html',context)


def action_form_view(request):
    if request.method == "POST":
        form=ActionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'The action added') 
            form=ActionForm()
    else:
        form=ActionForm()  
        
    return render(request,'planner/action_form.html',context={'form':form})    


