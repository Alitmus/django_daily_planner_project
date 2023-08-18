from django.urls import path
from .views import (HomeView,
                    ActivityCreateView,ActivityListView,ActivityUpdateView,ActivityDeleteView,
                    CategoryCreateView,CategoryListView,CategoryUpdateView,CategoryDeleteView,
                    ActionListView,ActionUpdateView,ActionDeleteView,
                    custom_date_view,action_form_view,activity_report_view)

app_name= 'planner'

urlpatterns=[
    path('',HomeView.as_view(),name='home'),

    path('category_create/',CategoryCreateView.as_view(),name='category_create'),
    path('category_list/',CategoryListView.as_view(),name='category_list'),
    path('category_update/<int:pk>',CategoryUpdateView.as_view(),name='category_update'),
    path('category_delete/<int:pk>',CategoryDeleteView.as_view(),name='category_delete'),
    
    path('activity_form/',ActivityCreateView.as_view(),name='activity_form'),
    path('activity_list/',ActivityListView.as_view(),name='activity_list'),
    path('activity_update/<int:pk>/',ActivityUpdateView.as_view(),name='activity_update'),
    path('delete_activity/<int:pk>',ActivityDeleteView.as_view(),name='delete_activity'),
    path('activity_report/',activity_report_view,name='activity_report'),

    path('action_form/',action_form_view,name='action_form'),
    path('action_list/',ActionListView.as_view(),name='action_list'),
    path('action_update/<int:pk>',ActionUpdateView.as_view(),name='action_update'),
    path('action_delete/<int:pk>',ActionDeleteView.as_view(),name='action_delete'),
    path('custom_date/',custom_date_view,name='custom_date'),
]